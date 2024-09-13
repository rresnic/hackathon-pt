# This is going to be the main python file for the project
from helper_functions import get_valid_input
from API_books import get_all_books_API,get_book_by_isbn,get_book_by_title_API,get_books_by_author_API,get_books_by_category_API,get_books_by_publisher
from customers_editor import CustomerEditor
from tabulate import tabulate
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


def get_all_books():
    results = get_all_books_API()
    print(tabulate_books(results))


def show_consult_menu():
    """
    Shows the menu for retrieving data from the database
    """
    menu_string="""
(U)ser statistics
Best (S)ellers
Books by (C)ategory
(A)ll books
(B)ack
"""
    valid_inputs = ["U", "S", "C", "A", "B"]
    while True:
        user_choice = get_valid_input(menu_string, valid_inputs)
        if user_choice == "B":
            break
        my_func = consult_menu_dict[user_choice]
        my_func()
    
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

main_function_dict = {"B": add_book, "U": add_user, "C": show_consult_menu, "S": make_sale} # todo make these function
consult_menu_dict = {"U": show_user_statistics_menu, "S": best_sellers, "C": books_by_category_API, "A": get_all_books}

show_menu()