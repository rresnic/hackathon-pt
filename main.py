# This is going to be the main python file for the project
from helper_functions import get_valid_input
from API_books import get_all_books_API,get_book_by_isbn,get_book_by_title_API,get_books_by_author_API,get_books_by_category_API,get_books_by_publisher
from customers_editor import CustomerEditor
from tabulate import tabulate
import books

def add_book():
    pass

def add_user():
    CustomerEditor.add_customer()

def make_sale():
    pass


def show_age_distribution():
    CustomerEditor.view_age_distribution()

def show_all_customers():
    CustomerEditor.show_all_customers()

def show_user_statistics_menu():
    us_f_dict = {"A": show_age_distribution, "S": show_all_customers}
    menu_string = """
Show (A)ge distribution
(S)how all customers
(B)ack
"""
    valid_input = ["A", "S", "B"]
    while True:
        user_choice = get_valid_input(menu_string, valid_input)
        if user_choice == "B":
            break
        my_func = us_f_dict[user_choice]
        my_func()

def tabulate_books(books):
    headers = ["Title", "Authors"]
    data = [[book.title, ','.join(book.authors) if isinstance(book.authors, list) else (book.authors or '')] for book in books]
    return tabulate(data, headers, tablefmt="grid")

def best_sellers():
    pass

def books_by_category_API():
    category = input("Enter a category: ")
    results =get_books_by_category_API(category)
    print(tabulate_books(results))

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

def get_all_books():
    results = get_all_books_API()
    print(tabulate_books(results))

def add_books_T():
    title = input("Enter a title: ")
    results = get_book_by_title_API(title)
    results = list(results)
    print(tabulate_books(list(results)))
    user_choice = get_valid_input("Add this book to the library? Y/N ", ["Y", "N"])
    if user_choice == "Y":
        books.insert_book_from_google(results)

def add_books_A():
    author = input("Enter an author: ")
    results = get_books_by_author_API(author)
    results = list(results)
    print(tabulate_books(results))
    user_choice = get_valid_input("Add this book to the library? Y/N ", ["Y", "N"])
    if user_choice == "Y":
        books.insert_books_from_google(results)

def add_books_C():
    category = input("Enter a category: ")
    results = get_books_by_category_API(category)
    results = list(results)
    print(tabulate_books(results))
    user_choice = get_valid_input("Add this book to the library? Y/N ", ["Y", "N"])
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
    user_choice = get_valid_input("Add this book to the library? Y/N ", ["Y", "N"])
    if user_choice == "Y":
        books.insert_books_from_google(results)

def add_books_menu():
    menu_string = """
Search for books to add to your inventory
Search by (T)itle, (A)uthor, (C)ategory, (I)sbn, (P)ublisher or
(B)ack
"""
    valid_inputs = ["T", "A", "C", "I", "P", "B"]
    while True:
        user_choice = get_valid_input(menu_string, valid_inputs)
        if user_choice == "B":
            break
        my_func = add_books_dict[user_choice]
        my_func()
    
add_books_dict = {"T": add_books_T, "A": add_books_A, "C": add_books_C, "I": add_books_I, "P": add_books_P}

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
(B)ack
"""
    valid_inputs = ["U", "S", "C", "A", "T", "P", "L",  "B"]
    while True:
        user_choice = get_valid_input(menu_string, valid_inputs)
        if user_choice == "B":
            break
        my_func = consult_menu_dict[user_choice]
        my_func()

consult_menu_dict = {"U": show_user_statistics_menu, "S": best_sellers, "C": get_books_by_category_db, "A": get_books_by_author_db, "T": get_books_by_title_db, "P":get_books_by_publisher_db,  "L": get_all_books_db}
    
def show_inventory_menu():
    menu_string="""
(A)dd new books
(S)earch inventory
(B)ack
"""
    valid_inputs= ["A", "S", "B"]
    while True:
        user_choice = get_valid_input(menu_string, valid_inputs)
        if user_choice == "B":
            break
        my_func = inv_menu_dict[user_choice]
        my_func()

def search_inv_menu():
    # TODO
    return "We have some problems, try later"

def show_menu():
    """
    Shows the primary program menu
    """
    # consulting the db will be 
    #   a.by ages
    #   b. the best-selling book
    #   c. which kind of books (comics, history, etc)
    #   d. all books and inventory
    #   
    menu_string="""
Add a new (B)ook
Add a new (U)ser
(C)onsult the db
(S)ell a book
or e(X)it the program
"""
    valid_inputs = ["B", "U", "C", "S", "X"]
    while True:
        user_choice = get_valid_input(menu_string, valid_inputs)
        if user_choice != "X":
            my_func = main_function_dict[user_choice]
            my_func()
        else:
            break
    # return user_choice

def get_filtered_table(data, headers, skip_columns=[]):
    # Filter out the headers we want to skip
    filtered_headers = [h for i, h in enumerate(headers) if i not in skip_columns]
    
    # Filter out the data for columns we want to skip
    filtered_data = [[row[i] for i in range(len(row)) if i not in skip_columns] for row in data]
    
    # Generate the table
    table = tabulate(filtered_data, headers=filtered_headers, tablefmt="grid")
    return table

main_function_dict = {"B": add_books_menu, "U": add_user, "C": show_consult_menu, "S": make_sale} # todo make these function
inv_menu_dict = {"A": add_books_menu, "S": search_inv_menu}
# inventory_menu_dict = ("A": show_all_inventory, "B": search_by_name, "C": search_by_category, "D": search_by_isbn, "I": add_book_menu)
# inventory_add_dict = {"A": search_api_by_author, "B": search_api_by_name, "C": search_api_by_category, "D": search_api_by_isbn}

show_menu()
# print(books.get_books_by_title("hollows"))