import sqlite3

connection = sqlite3.connect('dp_customers_(4)_copy.db')

cursor = connection.cursor()

rows = cursor.execute("SELECT name, city, state, postal_code FROM Customers").fetchall()

print()
print(f"{'Name':<25} {'City':>15} {'State':^8} {'Postal Code':>5}")
print('--------------------------------------------------------------')
for row in rows:
    print(f"{row[0]:<25} {row[1]:>15} {row[2]:^8} {row[3]:>11}")
print()