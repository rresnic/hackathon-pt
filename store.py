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
create_inventory_table()

def create_inventory_item(book_id):
    query = """INSERT INTO inventory(quantity, book_id) VALUES(?, ?);
    """
    DEFAULT_QUANTITY = 1
    params=(DEFAULT_QUANTITY, book_id)
    result= run_query(query, params)
    return result
# print(run_query("SELECT * FROM inventory;"))
# create_inventory_item(1)
