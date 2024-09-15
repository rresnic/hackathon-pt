import sqlite3
from tabulate import tabulate

def run_query(query, params=None):
    try:
        connection = sqlite3.connect("bookstore.db")
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

def create_inventory_table():
    query = """CREATE TABLE IF NOT EXISTS inventory (
    inventory_id INTEGER PRIMARY KEY AUTOINCREMENT,
    quantity INTEGER NOT NULL DEFAULT 1,
    book_id INTEGER,
    FOREIGN KEY (book_id) REFERENCES book(id) ON DELETE CASCADE ON UPDATE NO ACTION
    );
    """
    
    result = run_query(query)
    return result

def create_sales_table():
    query = """CREATE TABLE IF NOT EXISTS sales (
        sales_id INTEGER PRIMARY KEY AUTOINCREMENT,
        inventory_id,
        quantity INTEGER NOT NULL DEFAULT 1,
        book_id INTEGER,
        customer_id INTEGER,
        FOREIGN KEY (book_id) REFERENCES book(id) ON DELETE SET NULL,
        FOREIGN KEY (customer_id) REFERENCES customers(customer_id) ON DELETE SET NULL
        );
        """
    
    result = run_query(query)
    return result


create_inventory_table()
create_sales_table()


def create_inventory_item(book_id):
    query = """INSERT INTO inventory(quantity, book_id) VALUES(?, ?);
    """
    DEFAULT_QUANTITY = 1
    params=(DEFAULT_QUANTITY, book_id)
    result= run_query(query, params)
    return result
# print(run_query("SELECT * FROM inventory;"))
# create_inventory_item(1)

def get_best_sellers_emp(limit=10):
    query = """SELECT books.id, books.title, books.author, books.isbn, SUM(sales.quantity) AS total_sales, inventory.quantity FROM books INNER JOIN sales ON books.id = sales.book_id INNER JOIN inventory ON inventory.book_id = books.id WHERE sales.book_id IS NOT NULL GROUP BY books.id ORDER BY total_sales LIMIT ?;
"""
    params = (limit,)
    result = run_query(query, params)
    return result

def get_best_sellers(limit=10):
    query = """SELECT books.title, books.author, SUM(sales.quantity) AS total_sales FROM books INNER JOIN sales ON books.id = sales.book_id WHERE sales.book_id IS NOT NULL GROUP BY books.id ORDER BY total_sales LIMIT ?;
"""
    params = (limit,)
    result = run_query(query, params)
    return result

def make_sale(id, quantity= 1, customer_id=1):
    query = """SELECT quantity, inventory_id FROM inventory WHERE book_id = ?;"""
    params = (id,)
    result = run_query(query, params)
    if result:
        stock = result[0][0]
        inv_id = result[0][1]
        if quantity <= stock:
            stock -= quantity
            query = """UPDATE inventory SET quantity = ? WHERE book_id = ?;"""
            params= (stock, id)
            result = run_query(query, params)
            query = """INSERT INTO sales (inventory_id, quantity, book_id, customer_id) VALUES (?, ?, ?, ?);"""
            params= (inv_id, quantity, id, customer_id)
            result = run_query(query, params)
        else:
            print(f"Insufficient stock: {stock}")
    else:
        print("An inventory error occurred")

def update_quantity_book_id(id, quantity=1):
    query = """UPDATE inventory SET quantity = ? WHERE book_id = ?;"""
    params = (quantity, id)
    result = run_query(query, params)
    return result

def get_inv_data_id(id):
    query = """SELECT books.id, books.title, books.author, books.isbn, SUM(sales.quantity) as total_sales, inventory.quantity FROM books INNER JOIN inventory ON books.id = inventory.book_id LEFT OUTER JOIN sales on sales.book_id = inventory.book_id WHERE books.id = ? GROUP BY books.id;"""
    params = (id,)
    result = run_query(query, params)
    return result

def get_inv_data_author(author):
    query = """SELECT books.id, books.title, books.author, books.isbn, SUM(sales.quantity) as total_sales, inventory.quantity FROM books INNER JOIN inventory ON books.id = inventory.book_id LEFT OUTER JOIN sales on sales.book_id = inventory.book_id WHERE books.author like ? GROUP BY books.id;"""
    term = f"%{author}%"
    params = (term,)
    result = run_query(query, params)
    return result

def get_inv_data_title(title):
    query = """SELECT books.id, books.title, books.author, books.isbn, SUM(sales.quantity) as total_sales, inventory.quantity FROM books INNER JOIN inventory ON books.id = inventory.book_id LEFT OUTER JOIN sales on sales.book_id = inventory.book_id WHERE books.title like ? GROUP BY books.id;"""
    term = f"%{title}%"
    params = (term,)
    result = run_query(query, params)
    return result

def get_inv_data_all():
    query = """SELECT books.id, books.title, books.author, books.isbn, SUM(sales.quantity) as total_sales, inventory.quantity FROM books INNER JOIN inventory ON books.id = inventory.book_id LEFT OUTER JOIN sales on sales.book_id = inventory.book_id GROUP BY books.id;"""
    result = run_query(query)
    return result
# print(get_inv_data_all())
# update_quantity_book_id(2, 10)
# print(get_inv_data_id(2))