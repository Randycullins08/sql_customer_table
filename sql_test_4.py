import sqlite3

connection = sqlite3.connect('dp_customers_(4)_copy.db')
cursor = connection.cursor()

new_customers = [
    ("Fake Company-1", "123 Street","Acuamville", "FL", 31140, 1234567890, "test@test14.com"),
    ("Fake Company-2", "123 Street","Acuamville", "FL", 31140, 1234567890, "test@test13.com"),
    ("Fake Company-3", "123 Street","Acuamville", "FL", 31140, 1234567890, "test@test12.com"),
    ("Fake Company-4", "123 Street","Acuamville", "FL", 31140, 1234567890, "test@test11.com"),
    ("Fake Company-5", "123 Street","Acuamville", "FL", 31140, 1234567890, "test@test10.com"),
    ("Fake Company-6", "123 Street","Dallas", "TX", 75001, 1234567890, "test@test9.com"),
    ("Fake Company-7", "123 Street","Dallas", "TX", 75001, 1234567890, "test@test8.com"),
    ("Fake Company-8", "123 Street","Dallas", "TX", 75001, 1234567890, "test@test7.com"),
    ("Fake Company-9", "123 Street","ELKO", "NV", 89801, 1234567890, "test@test6.com"),
    ("Fake Company-10","123 Street", "ELKO", "NV", 89801, 1234567890, "test@test5.com"),
    ("Fake Company-11","123 Street", "ELKO", "NV", 89801, 1234567890, "test@test4.com"),
    ("Fake Company-12","123 Street", "Ogden", "UT", 84401, 1234567890, "test@test3.com"),
    ("Fake Company-13","123 Street", "Ogden", "UT", 84401, 1234567890, "test@test2.com"),
    ("Fake Company-14","123 Street", "Ogden", "UT", 84401, 1234567890, "test@test1.com"),
    ("Fake Company-15","123 Street", "Ogden", "UT", 84401, 1234567890, "test@test.com"),
]

insert_sql = "INSERT INTO Customers(name, street_address, city, state, postal_code, phone, email) VALUES(?,?,?,?,?,?,?)"

for new_customer in new_customers:
    cursor.execute(insert_sql, new_customer)

connection.commit()