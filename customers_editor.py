from sql.customers_manager import CustomerManager
from sql.customers import Customer
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
    
    @classmethod
    def add_customer(cls):
        try: 
            name = input("Enter the name: ")
            age = int(input("Enter the age as a whole number"))
            email = input("Enter the email: e.g. sample@host.com")
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
