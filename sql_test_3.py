import sqlite3

connection = sqlite3.connect('dp_customers_(4)_copy.db')
cursor = connection.cursor()

sql_update = "UPDATE Customers SET phone=? WHERE phone IS NULL"
update_values = ("123456789",)

cursor.execute(sql_update, update_values)

connection.commit()