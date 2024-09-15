from customers_manager import CustomerManager
from customers import Customer
from tabulate import tabulate

class CustomerEditor:
    @classmethod
    def view_customer_by_name(cls, name):
        cust = CustomerManager.get_by_name(name)
        print(cust)

    @classmethod
    def view_customer_by_id(cls, id):
        cust = CustomerManager.get_customer_by_id(id)
        print(cust)
        return cust
    
    @classmethod
    def view_customer_by_email(cls, email):
        cust = CustomerManager.get_by_email(email)
        print(cust)
        return cust            
    
    @classmethod
    def add_customer(cls):
        try: 
            name = input("Enter the name: ")
            age = int(input("Enter the age as a whole number: "))
            email = input("Enter the email: e.g. sample@host.com: ")
            new_cust = Customer(name, age, email)
            if new_cust.save():
                print("Customer Added Successfully")
        except:
            print("Something went wrong)")
    
    @classmethod
    def view_age_distribution(cls):
        counts = CustomerManager.customer_count_by_age()
        print(tabulate(counts, ["Age", "Customers"]))
    
    @classmethod
    def show_all_customers(cls):
        customers = CustomerManager.all_customer_tabular()
        print(tabulate(customers, ["Name", "Age", "Email"]))

    @classmethod
    def update_customer(cls, id):
        name = input("Enter customer name: ")
        age = input("Enter a customer age: ")
        email = input("Enter a customer email: ")
        customer = CustomerManager.get_customer_by_id(id)
        customer.update(name, age, email)

    @classmethod
    def delete_customer(cls, id):
        customer = CustomerManager.get_customer_by_id(id)
        customer.delete()

