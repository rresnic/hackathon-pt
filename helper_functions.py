from tabulate import tabulate

def get_valid_input(prompt, valid):
    while True:
        user_input = input(prompt)
        if user_input in valid:
            return user_input
        else:
            print("Invalid input.")

def show_menu(menu_string, menu_dict, exit="X", repeating=True):
    valid_input = list(menu_dict.keys())
    valid_input.append(exit)
    while True:
        user_choice = get_valid_input(menu_string, valid_input)
        if user_choice == exit:
            break
        my_func, *args = menu_dict[user_choice]
        my_func(*args)
        if not repeating:
            break

def tabulate_books(books):
    headers = ["Title", "Authors"]
    print(type(books))
    if isinstance(books, list):
        data = [[book.title[:50], ','.join(book.authors)[:50] if isinstance(book.authors, list) else (book.authors or '')[:50]] for book in books]
    else:
        data = []
        row = [books.title[:50], ','.join(books.authors)[:50] if isinstance(books.authors, list) else (books.authors or '')[:50]]
        data.append(row)
        
    return tabulate(data, headers, tablefmt="grid")

def get_filtered_table(data, headers, skip_columns=[]):
    # Filter out the headers we want to skip
    filtered_headers = [h for i, h in enumerate(headers) if i not in skip_columns]
    
    # Filter out the data for columns we want to skip
    filtered_data = [[str(row[i])[:50] for i in range(len(row)) if i not in skip_columns] for row in data]
    
    # Generate the table
    table = tabulate(filtered_data, headers=filtered_headers, tablefmt="grid")
    return table