import json


class Person:
    first_name = ""
    last_name = ""
    email = ""
    name = ""

    def __init__(self, first_name, last_name, email):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email

    # returns the full name
    def full_name(self):
        return self.first_name + self.last_name


class Customer(Person):
    def __init__(self, first_name, last_name, email, Number):
        super().__init__(first_name, last_name, email)
        self.Number = Number


class Employee(Person):

    # inheritance from class person with added attribute SSN
    def __init__(self, first_name, last_name, email, SSN):
        super().__init__(first_name, last_name, email)
        self.SSN = SSN

# Return instance of Customer


def Create_Customer():
    first_name = input("First name:")
    last_name = input("Last name:")
    email = input("Email:")
    Number = input("Number:")
    cust = Customer(first_name, last_name, email, Number)
    return cust

# Return instance of employee


def Create_Employee():
    first_name = input("First name:")
    last_name = input("Last name:")
    email = input("Email:")
    SSN = input("SSN:")
    emp = Employee(first_name, last_name, email, SSN)
    return emp


def main():
    while True:
        print("Customer/Employee Data Entry")
        choice = input("customer or employee? (c/e):")
        print("DATA ENTRY")
        if choice == 'c':
            print("Create customer object")
            cust_obj = Create_Customer()
            print("*****CUSTOMER*****")
            for key, value in cust_obj.__dict__.items():
                print(key, ':', value)
        elif choice == 'e':
            print("Create Employee object")
            emp_obj = Create_Employee()
            print("*****EMPLOYEE*****")
            for key, value in emp_obj.__dict__.items():
                print(key, ':', value)
        else:
            print("Please Choose the given option")
        cont = input("Continue?(y/n):")
        if cont == 'n':
            print("BYE !")
            break


if __name__ == "__main__":
    main()
