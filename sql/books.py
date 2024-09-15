import sqlite3
from tabulate import tabulate
import sql.store as store


def run_query(query, params=None):
    try:
        connection = sqlite3.connect("../db/bookstore.db")
        cursor = connection.cursor()
        if params:
            cursor.execute(query, params)
        else:
            cursor.execute(query)
        connection.commit()
        results = cursor.fetchall()
        cursor.close()
        connection.close()
        return results
    except sqlite3.Error as e:
        print(e)

def create_books_table():
    query = """CREATE TABLE IF NOT EXISTS books (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    author TEXT,
    publisher TEXT,
    published_date TEXT,
    description TEXT,
    isbn TEXT UNIQUE  -- Add UNIQUE constraint
    );
    """
    
    result = run_query(query)
    return result
def create_category_table():
    query = """CREATE TABLE IF NOT EXISTS category (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT UNIQUE NOT NULL
    );
    """
    result = run_query(query)
    return result

def create_book_category_table():
    query = """CREATE TABLE IF NOT EXISTS book_category (
    book_id INTEGER,
    category_id INTEGER,
    PRIMARY KEY (book_id, category_id),
    
    -- Foreign key constraint for book_id referencing book table
    FOREIGN KEY (book_id) REFERENCES book(id) ON DELETE CASCADE ON UPDATE NO ACTION,
        
    -- Foreign key constraint for category_id referencing category table
    FOREIGN KEY (category_id) REFERENCES category(id) ON DELETE CASCADE ON UPDATE NO ACTION
    );
    """
    result = run_query(query)
    return result



def insert_book_data(title, authors, publisher, published_date, description, isbn, categories):
    try:
        connection = sqlite3.connect("../db/bookstore.db")
        cursor = connection.cursor()    # Check if the book with the same ISBN already exists
        cursor.execute('SELECT id FROM books WHERE isbn = ?', (isbn,))
        existing_book = cursor.fetchone()
    
        if existing_book:
            print(f"Book with ISBN {isbn} already exists. Skipping.")
            return
        
        # Insert the book into the book table if it's not a duplicate
        cursor.execute('''
            INSERT INTO books (title, author, publisher, published_date, description, isbn)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (title, ', '.join(authors), publisher, published_date, description, isbn))
    
        # Get the last inserted book's ID
        book_id = cursor.lastrowid
        
        # Insert categories and link them to the book in the book_category table
        for category in categories:
            category = category.capitalize()
            # Insert the category if it doesn't already exist
            cursor.execute('SELECT id FROM category WHERE name = ?', (category,))
            category_row = cursor.fetchone()
            
            if category_row is None:
                cursor.execute('INSERT INTO category (name) VALUES (?)', (category,))
                category_id = cursor.lastrowid
            else:
                category_id = category_row[0]
            
            # Insert into the book_category table
            cursor.execute('INSERT INTO book_category (book_id, category_id) VALUES (?, ?)', (book_id, category_id))
        # add the book to inventory with default
        cursor.execute("INSERT INTO inventory (book_id, quantity) VALUES(?, ?)", (book_id, 1))
        # Commit the changes
        connection.commit()
        cursor.close()
        connection.close()
    except sqlite3.Error as e:
        print(e)
    except Exception:
        print("something went wrong")

def insert_book_from_google(book):    
    title = book.title
    authors = ""
    publisher = ""
    published_date = ""
    description = ""
    isbn = ""
    categories = ""
    if book.authors: 
        authors = book.authors
    else:
        authors = ""
    if book.publisher:
        publisher = book.publisher 
    if book.published_date:
        published_date = book.published_date
    if book.description:
        description = book.description
    if book.ISBN_13:
        isbn = book.ISBN_13
    elif book.ISBN_10:
        isbn = book.ISBN_10
    if book.subjects:
        categories = book.subjects
    insert_book_data(title, authors, publisher, published_date, description, isbn, categories)
    print("Inserted", [title, authors, publisher, published_date, description, isbn, categories])

def insert_books_from_google(books):
    print("in insert", books)
    if isinstance(books, list):
        for book in books:
            insert_book_from_google(book)
    else:
        insert_book_from_google(books)
    
create_books_table()
create_category_table()
create_book_category_table()

def get_books_by_title(title):
    query= "SELECT * FROM books WHERE title LIKE ? COLLATE NOCASE"
    term = f"%{title}%"
    params = (term,)
    results = run_query(query, params)
    return results

def get_books_by_category(category):
    query = "SELECT * from books inner join book_category on books.id = book_category.book_id inner join category on book_category.category_id = category.id WHERE category.name LIKE ? COLLATE NOCASE"
    term = f"%{category}%"
    params = (term,)
    results = run_query(query, params)
    return results

def get_books_by_author(author):
    query = "SELECT * from books WHERE author LIKE ? COLLATE NOCASE"
    term = f"%{author}%"
    params = (term,)
    results = run_query(query, params)
    return results

def get_books_by_publisher(publisher):
    query = "SELECT * from books WHERE publisher LIKE ? COLLATE NOCASE"
    term = f"%{publisher}%"
    params = (term,)
    results = run_query(query, params)
    return results

def get_books_by_isbn(isbn):
    query = "SELECT * from books WHERE isbn LIKE ? COLLATE NOCASE"
    term = f"%{isbn}%"
    params = (term,)
    results = run_query(query, params)
    return results


def get_all_books():
    query = "SELECT * from books inner join book_category on books.id = book_category.book_id inner join category on book_category.category_id = category.id"
    results = run_query(query)
    return results