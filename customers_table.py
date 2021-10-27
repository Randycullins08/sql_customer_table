import sqlite3

connection = sqlite3.connect('dp_customers_(4)_copy.db')
cursor = connection.cursor()

def view_function():
    rows = cursor.execute("SELECT customer_id, name, city, state, postal_code FROM Customers").fetchall()

    print()
    print(f"{'ID':<5}{'Name':<25} {'City':<15} {'State':^7} {'Postal Code':>5}")
    print('-' * 66)
    for row in rows:
        print(f"{row[0]:<4} {row[1]:<25} {row[2]:<15} {row[3]:^8} {row[4]:>10}")
    print()

def print_customer(cust_id):
    search_sql = "SELECT * FROM Customers WHERE customer_id = ?"
    row = cursor.execute(search_sql, (cust_id,)).fetchone()
    print()
    print(f"{'ID':<4} {'Name':<22} {'Address':<30} {'City':<17} {'State':<7} {'Postal Code':<13} {'Phone #':<13} {'Email':>22}")
    print("-" * 136)
    print(f"{row[0]:<4} {row[1]:<22} {row[2]:<30} {row[3]:<17} {row[4]:<7} {row[5]:<13} {row[6]:<13} {row[7]:>22}")
    print()

def search_function():
    while True:
        search_start = input("Would you like to search a customer? (Y)es or (N)o: ").lower()
        if search_start == 'y':
            cust_id_input = input("Who would you like to search for? Search by 'Customer ID': ").title()
            search_sql = "SELECT * FROM Customers WHERE customer_id = ?"
            row = cursor.execute(search_sql, (cust_id_input,)).fetchone()
            print()
            print(f"{'ID':<4} {'Name':<22} {'Address':<30} {'City':<17} {'State':<7} {'Postal Code':<1}")
            print("-" * 96)
            print(f"{row[0]:<4} {row[1]:<22} {row[2]:<30} {row[3]:<17} {row[4]:<7} {row[5]:>11}")
            print()
        if search_start == 'n':
            print("Going back to the main menu")
            break

def update_function():
    print("What would you like to update? ")
    while True:
        user_input = input("""
(N)ame
(A)ddress
(C)ity
(S)tate
(P)ostal Code
(Ph)one
(E)mail
(Q)uit back to main menu
        """).lower()
        if user_input == "n":
            cust_id = input("Enter Customer ID: ")
            new_name = input("Enter New Name: ").title()
            name_update = "UPDATE Customers SET name=? WHERE customer_id=?"
            cursor.execute(name_update, (new_name, cust_id))
            print("Customer has been updated!")
            print_customer(cust_id)
            connection.commit()

        if user_input == "a":
            cust_id = input("Enter Customer ID: ")
            new_address = input("Enter New Address: ").title()
            name_update = "UPDATE Customers SET street_address=? WHERE customer_id=?"
            cursor.execute(name_update, (new_address, cust_id))
            print("Customer has been updated!")
            print_customer(cust_id)
            connection.commit()
        if user_input == "c":
            cust_id = input("Enter Customer ID: ")
            city = input("Enter New City : ").title()
            name_update = "UPDATE Customers SET city=? WHERE customer_id=?"
            cursor.execute(name_update, (city, cust_id))
            print("Customer has been updated!")
            print_customer(cust_id)
            connection.commit()
        if user_input == "s":
            cust_id = input("Enter Customer ID: ")
            state = input("Enter New State : ").upper()
            name_update = "UPDATE Customers SET state=? WHERE customer_id=?"
            cursor.execute(name_update, (state, cust_id))
            print("Customer has been updated!")
            print_customer(cust_id)
            connection.commit()
        if user_input == "p":
            cust_id = input("Enter Customer ID: ")
            zip_code = input("Enter New Postal Code : ")
            name_update = "UPDATE Customers SET postal_code=? WHERE customer_id=?"
            cursor.execute(name_update, (zip_code, cust_id))
            print("Customer has been updated!")
            print_customer(cust_id)
            connection.commit()
        if user_input == "ph":
            cust_id = input("Enter Customer ID: ")
            phone_number = input("Enter New Phone Number : ")
            name_update = "UPDATE Customers SET phone=? WHERE customer_id=?"
            cursor.execute(name_update, (phone_number, cust_id))
            print("Customer has been updated!")
            print_customer(cust_id)
            connection.commit()
        if user_input == "e":
            cust_id = input("Enter Customer ID: ")
            email = input("Enter New Email : ")
            name_update = "UPDATE Customers SET email=? WHERE customer_id=?"
            cursor.execute(name_update, (email, cust_id))
            print("Customer has been updated!")
            print_customer(cust_id)
            connection.commit()
        if user_input == "q":
            print("Heading back to main menu")
            break

def insert_function():
    while True:
        insert_input = input("Would you like to insert a new customer? (Y)es or (N)o ").lower()
        if insert_input == 'y':
            print("Enter New Customers Information")
            name = input("Enter Customer Name: ").title()
            street_address = input("Enter Customers Street Address: ").title()
            city = input("Enter Customers City: ").title()
            state = input("Enter Customers State: ").upper()
            postal_code = input("Enter Customers Postal Code: ")
            phone = input("Enter Customers Phone Number: ")
            email = input("Enter Customers Email Address: ")

            customers_info = [
                (name, street_address, city, state, postal_code, phone, email)
            ]
            insert_sql = "INSERT INTO Customers(name, street_address, city, state, postal_code, phone, email) VALUES(?,?,?,?,?,?,?)"

            for customer in customers_info:
                cursor.execute(insert_sql, customer)
            print("New customer has been added!")
            print()
            print(f"{'Name':<22} {'Address':<30} {'City':<17} {'State':<7} {'Postal Code':<13} {'Phone #':<13} {'Email':>22}")
            print("-" * 136)
            print(f"{customer[0]:<22} {customer[1]:<30} {customer[2]:<17} {customer[3]:<7} {customer[4]:<13} {customer[5]:<13} {customer[6]:>22}")
            print()
            connection.commit()
        if insert_input == 'n':
            print("Going back to main menu")
            break

def delete_function():
    print("BE CAREFUL DELETING THINGS CAN BE BAD!")
    while True:
        are_you_sure = input("Are you sure you want to delete something? (Y)es or (N)o: ").lower()
        if are_you_sure == 'y':
            you_positive = input("Are you positive? (Y)es or (N)o: ").lower()
            if you_positive == 'y':
                cust_id = input("Enter Customer ID: ")
                delete_sql = "DELETE FROM Customers WHERE customer_id=?"
                cursor.execute(delete_sql, (cust_id,))
                connection.commit()
                print("You deleted it! It's gone FOREVER!")
                break
            if you_positive == 'n':
                print("I'm glad you came to your senses lets go back to the main menu")
                break
        if are_you_sure == 'n':
            print("Good move lets go back to the main menu")
            break

while True:
    print("""
What would you like to do?
(V)iew All Customers
(S)earch For One Customer
(U)pdate Customers Table
(I)nsert Into Customers Table
(D)elete From Customers Table
(Q)uit
""")
    start_app = input().lower()
    if start_app == 'v':
        view_function()
    if start_app == 's':
        search_function()
    if start_app == 'u':
        update_function()
    if start_app == 'i':
        insert_function()
    if start_app == 'd':
        delete_function()
    if start_app == 'q':
        print("Good Bye")
        break