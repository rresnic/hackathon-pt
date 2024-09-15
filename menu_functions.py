from helper_functions import get_valid_input, show_menu, tabulate_books, get_filtered_table


from API_books import get_all_books_API,get_book_by_isbn,get_book_by_title_API,get_books_by_author_API,get_books_by_category_API,get_books_by_publisher
from customers_editor import CustomerEditor
from tabulate import tabulate
import books as books
import store

# Manage customers menu block

# Add customers menu block
def add_customer():
    CustomerEditor.add_customer()

def get_customer_by_email():
    email = input("Enter an email: ")
    result = CustomerEditor.view_customer_by_email(email)
    if result:
        id = result.id
        menu_string="""
(U)pdate Customer
(D)elete Customer or
(B)ack
"""
        show_menu(menu_string, {"U": (CustomerEditor.update_customer, id), "D": (CustomerEditor.delete_customer, id)}, "B", False)

def show_customer_menu():
    menu_string = """
Manage Customers Menu:
(A)dd customer,
(S)earch for customer by email,
(B)ack
"""
    cm_dict = {"A": (add_customer,), "S": (get_customer_by_email,)}
    show_menu(menu_string, cm_dict, "B")

# Add Books menu block
def add_books_T():
    title = input("Enter a title: ")
    results = get_book_by_title_API(title)
    print(tabulate_books(results))
    user_choice = get_valid_input("Add this book to the library? Y/N ", ["Y", "N"])
    if user_choice == "Y":
        books.insert_book_from_google(results)

def add_books_A():
    author = input("Enter an author: ")
    results = get_books_by_author_API(author)
    results = list(results)
    print(tabulate_books(results))
    user_choice = get_valid_input("Add these books to the library? Y/N ", ["Y", "N"])
    if user_choice == "Y":
        books.insert_books_from_google(results)

def add_books_C():
    category = input("Enter a category: ")
    results = get_books_by_category_API(category)
    results = list(results)
    print(tabulate_books(results))
    user_choice = get_valid_input("Add these books to the library? Y/N ", ["Y", "N"])
    if user_choice == "Y":
        books.insert_books_from_google(results)

def add_books_I():
    ISBN = input("Enter an ISBN: ")
    results = get_book_by_isbn(ISBN)
    results = list(results)
    print(tabulate_books(results))
    user_choice = get_valid_input("Add this book to the library? Y/N ", ["Y", "N"])
    if user_choice == "Y":
        books.insert_books_from_google(results)

def add_books_P():
    publisher = input("Enter a publisher: ")
    results = get_books_by_category_API(publisher)
    results = list(results)
    print(tabulate_books(results))
    user_choice = get_valid_input("Add these books to the library? Y/N ", ["Y", "N"])
    if user_choice == "Y":
        books.insert_books_from_google(results)

def add_books_menu():
    menu_string = """
Search for books to add to your inventory
Search by (T)itle, (A)uthor, (C)ategory, (I)sbn, (P)ublisher, or
(B)ack
"""
    add_books_dict = {"T": (add_books_T,), "A": (add_books_A,), "C": (add_books_C,), "I": (add_books_I,), "P": (add_books_P,)}
    show_menu(menu_string, add_books_dict, "B")




# User Statistics Block
def show_age_distribution():
    CustomerEditor.view_age_distribution()

def show_all_customers():
    CustomerEditor.show_all_customers()

def show_user_statistics_menu():
    menu_string = """
Show (A)ge distribution
(S)how all customers
(B)ack
"""
    us_f_dict = {"A": (show_age_distribution,), "S": (show_all_customers,)}

    show_menu(menu_string, us_f_dict, "B")

# DB Update block
def get_books_emp_cat():
    pass

def edit_title(book_id):
    title = input("Enter new title: ")
    books.edit_title_by_id(book_id, title)

def edit_author(book_id):
    author = input("Enter new author: ")
    books.edit_author_by_id(book_id, author)

def edit_stock(book_id):
    try:
        quantity = int(input("Enter new total stock: "))
        store.update_quantity_book_id(book_id, quantity)
    except Exception as e:
        print(e)

def edit_book_id():
    id = input("Enter a book id: ")
    book = store.get_inv_data_id(id)
    print(get_filtered_table(book, ["ID", "Title", "Author", "ISBN", "Sold", "Stock"]))
    menu_string= """
Edit (T)itle
Edit (A)uthor
Update (S)tock
(B)ack
"""
    book_edit_dict ={"T": (edit_title, id), "A": (edit_author, id), "S": (edit_stock, id)}
    show_menu(menu_string, book_edit_dict, "B")
        # query = """SELECT books.id, books.title, books.author, books.isbn, SUM(sales.quantity) AS total_sales FROM books INNER JOIN sales ON books.id = sales.book_id WHERE sales.book_id IS NOT NULL GROUP BY books.id ORDER BY total_sales LIMIT ?;

def best_sellers_inv():
    results = store.get_best_sellers_emp()
    print(get_filtered_table(results, ["ID", "Title", "Author", "ISBN", "Sold", "In Stock"]))

def get_inv_by_title():
    title = input("Enter a title: ")
    results = store.get_inv_data_title(title)
    print(get_filtered_table(results, ["ID", "Title", "Author", "ISBN", "Sold", "In Stock"]))

def get_inv_by_author():
    author = input("Enter an author: ")
    results = store.get_inv_data_author(author)
    print(get_filtered_table(results, ["ID", "Title", "Author", "ISBN", "Sold", "In Stock"]))

def get_all_inv():
    results = store.get_inv_data_all()
    print(get_filtered_table(results, ["ID", "Title", "Author", "ISBN", "Sold", "In Stock"]))

def search_inv_menu():
    # TODO
    menu_string = """
Search for books by
(A)uthor
(T)itle
Best (S)ellers
A(L)l books
(E)dit book by ID
(B)ack
"""
    s_inv_dict = { "S": (best_sellers_inv,), "A": (get_inv_by_author,), "T": (get_inv_by_title,), "L": (get_all_inv,), "E": (edit_book_id,)}
    show_menu(menu_string, s_inv_dict, "B")
    

def show_inventory_menu():
    menu_string="""
(A)dd new books
(S)earch inventory
(B)ack
"""

    inv_menu_dict = {"A": (add_books_menu,), "S":(search_inv_menu, )}
    show_menu(menu_string, inv_menu_dict, "B")
# DB consult block

def best_sellers_emp():
    results = store.get_best_sellers_emp()
    print(get_filtered_table(results, ["ID", "Title", "Author", "ISBN", "Sales", "In stock"]))

def get_books_by_category_db():
    category = input("Enter a category: ")
    results =books.get_books_by_category(category)
    print(get_filtered_table(results, ["ID", "Title", "Author", "Publisher", "Published Date", "Description", "ISBN"], [0, 5]))

def get_books_by_author_db():
    author = input("Enter an author: ")
    results =books.get_books_by_author(author)
    print(get_filtered_table(results, ["ID", "Title", "Author", "Publisher", "Published Date", "Description", "ISBN"], [0, 5]))

def get_books_by_title_db():
    title = input("Enter a title: ")
    results =books.get_books_by_title(title)
    print(get_filtered_table(results, ["ID", "Title", "Author", "Publisher", "Published Date", "Description", "ISBN"], [0, 5]))

def get_books_by_publisher_db():
    publisher = input("Enter a publisher: ")
    results =books.get_books_by_publisher(publisher)
    print(get_filtered_table(results, ["ID", "Title", "Author", "Publisher", "Published Date", "Description", "ISBN"], [0, 5]))

def get_all_books_db():
    results =books.get_all_books()
    print(get_filtered_table(results, ["ID", "Title", "Author", "Publisher", "Published Date", "Description", "ISBN"], [0, 5]))


def get_categories():
    results = books.get_categories()
    print("Categories: ")
    for category in results.split(","):
        print(category)

def show_consult_menu():
    """
    Shows the menu for retrieving data from the database
    """
    menu_string="""
(U)ser statistics
Best (S)ellers
Books by (C)ategory
Books by (A)uthor
Books by (T)itle
Books by (P)ublisher
A(L)l Books
(V)iew all categories
(B)ack
"""
    consult_menu_dict = {"U": (show_user_statistics_menu,), "S": (best_sellers_emp,), "C": (get_books_by_category_db,), "A": (get_books_by_author_db,), "T": (get_books_by_title_db,), "P":(get_books_by_publisher_db,),  "L": (get_all_books_db,), "V": (get_categories,)}
    show_menu(menu_string, consult_menu_dict, "B")

def make_sale():
    book_id = int(input("Enter book id: "))
    quantity = int(input("Enter number of books to purchase: "))
    customer_id = int(input("Enter customer id: "))
    store.make_sale(book_id, quantity, customer_id)

def show_program_menu():
    menu_string="""
Manage (I)nventory
Manage (U)sers
(C)onsult the db
(S)ell a book
or e(X)it the program
"""
    main_function_dict = {"I": (show_inventory_menu,), "U": (show_customer_menu,), "C": (show_consult_menu,), "S": (make_sale,)} 
    show_menu(menu_string, main_function_dict)

# show_program_menu()