# This is going to be the main python file for the project
from helper_functions import get_valid_input

# main_function_dict = {"B": add_book, "U": add_user, "C": show_consult_menu, "S": make_sale} # todo make these function
def show_menu():

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
    user_choice = get_valid_input(menu_string, valid_inputs)
    return user_choice

