from customers import Customer
import sqlite3
from tabulate import tabulate

class CustomerManager:
    @classmethod
    def run_query(cls,query, params = None):
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

    @classmethod
    def get_by_name(cls, name):
        query = "SELECT * FROM customers WHERE name = ?"
        params = (name,)
        results = CustomerManager.run_query(query, params)
        if results and len(results) > 0:
            return Customer.load_customer(results[0])
        else:
            return None
    
    @classmethod
    def get_by_email(cls, email):
        query = "SELECT * FROM customers WHERE email LIKE ?"
        term = f"%{email}%"
        params = (term,)
        results = CustomerManager.run_query(query, params)
        if results and len(results) > 0:
            return Customer.load_customer(results[0])
        else:
            return None
        
    @classmethod
    def get_customer_by_id(cls, id):
        query = "SELECT * from customers WHERE customer_id = ?"
        params = (id,)
        results = CustomerManager.run_query(query, params)
        if results:
            return Customer.load_customer(results[0])
        else:
            print("ID not found")

    @classmethod
    def get_by_name_and_age(cls, name, age):
        query = "SELECT * FROM customers WHERE name = ? and age = ?"
        params = (name, age)
        results = CustomerManager.run_query(query, params)
        if results and len(results) > 0:
            return Customer.load_customer(results[0])
        else:
            return None
        
    @classmethod
    def all_customers(cls):
        query = "SELECT * from customers"
        results = CustomerManager.run_query(query)
        customers =[]
        for row in results:
            customers.append(Customer.load_customer(row))
        return customers
    
    @classmethod
    def customer_count_by_age(cls):
        query = "SELECT age, count(*) FROM customers GROUP BY age"
        results = CustomerManager.run_query(query)
        return results


    @classmethod
    def all_customer_tabular(cls):
        query = "SELECT name, age, email from customers"
        results = CustomerManager.run_query(query)
        return results

def main():

    counts = CustomerManager.customer_count_by_age()
    print(tabulate(counts, ["Age", "Customers"]))

if __name__ == "__main__":    
    main()
