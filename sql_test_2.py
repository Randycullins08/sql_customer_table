import sqlite3

connection = sqlite3.connect('dp_customers_(4)_copy.db')
cursor = connection.cursor()

name = input("Company Name: ").title()
address = input("Company Address: ").title()
city = input("Company City: ").title()
state = input("Company State: ").upper()
postal_code = input("Company Postal Code: ")

insert_sql = "INSERT INTO Customers(name, street_address, city, state, postal_code) VALUES(?,?,?,?,?)"

values = (name, address, city, state, postal_code)

cursor.execute(insert_sql, values)

connection.commit()