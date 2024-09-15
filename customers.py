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

def create_customer_table():
    query = """CREATE TABLE IF NOT EXISTS customers (
            customer_id INTEGER PRIMARY KEY, 
            name TEXT,
            age INT, 
            email TEXT UNIQUE NOT NULL
    );
    """
    
    result = run_query(query)
    return result


class Customer:
    def __init__(self, name, age, email) -> None:
        self.name = name
        self.age = age
        self.email = email
        self.id = None
        self.saved = False
    #save, delete, update
    def save(self):
        if self.saved:
            self.update()
            return
        else:
            query = "INSERT into customers (name, age, email) VALUES (?, ?, ?)"
            params = (self.name, self.age, self.email)
            try:
                connection = sqlite3.connect("bookstore.db")
                cursor = connection.cursor()
                cursor.execute(query, params)
                connection.commit()
                # Fetch the last inserted id
                self.id = cursor.lastrowid
                self.saved = True
                cursor.close()
                connection.close()
            except sqlite3.Error as e:
                print(e)
    
    def update(self, name=None, age=None, email=None):
        if self.id:
            if name:
                self.set_name(name)
            if age:
                self.set_age(age)
            if email:
                self.set_email(email)
            query = "UPDATE customers SET name = ?, age = ?,  email = ? WHERE customer_id = ?"
            params = (self.name, self.age, self.email, self.id)
            try:
                connection = sqlite3.connect("bookstore.db")
                cursor = connection.cursor()
                cursor.execute(query, params)
                connection.commit()
                cursor.close()
                connection.close()
            except sqlite3.Error as e:
                print(e)
        else: 
            print("Must be saved first")
            return None
    
    def delete(self):
        if self.id:
            query = "DELETE FROM customers WHERE customer_id = ?"
            params = (self.id,)
            temp_id = self.id
            try:
                connection = sqlite3.connect("bookstore.db")
                cursor = connection.cursor()
                cursor.execute(query, params)
                connection.commit()
                
                if cursor.rowcount > 0:
                    # Deletion successful
                    self.saved = False
                    self.id = None
                    print(f"Customer with id {temp_id} deleted successfully.")
                    result = True
                else:
                    # No rows were affected (either the row didn't exist or wasn't deleted)
                    print(f"Customer with id {self.id} not found or already deleted.")
                    result = False

                cursor.close()
                connection.close()
                return result
            except sqlite3.Error as e:
                print(e)
                return None
        else:
            print("This customer does not exist or has not been saved yet.")

    def set_name(self, name):
        self.name = name
    
    def set_age(self, age):
        self.age = age

    def set_email(self, email):
        self.email = email

    def set_id(self, id):
        self.id = id

    def set_saved(self, boo):
        self.saved = boo

    @classmethod
    def load_customer(cls, row):
        id = row[0]
        name = row[1]
        age = row[2]
        email = row[3]
        new_item = Customer(name, age, email)
        new_item.set_id(id)
        new_item.set_saved(True)
        return new_item
    
    def run_query(self, query, params = None):
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

    def get_customer(self):
        query = "SELECT * from customers WHERE customer_id = ?"
        params = (self.id,)
        results = self.run_query(query, params)
        print(results)
        return results
         
    def __repr__(self) -> str:
        return f"Customer: {self.name}\nAge: {self.age}\nEmail: {self.email}\nID: {self.id}"
    
create_customer_table()
# test1 = Customer("John", 17, "sample@example.com")
# print(test1)
# test1.save()
# print(test1)
# test2 = Customer.load_customer(test1.get_customer()[0])
# print(test2)
# test2.update(name="",age="", email="sample2@other.com")
# print(test2)
# test3 = Customer.load_customer(test2.get_customer()[0])
# print(test3)