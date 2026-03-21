import psycopg2
conn = psycopg2.connect(
    host="localhost",
    database="phonebook_db",
    user="postgres",
    password="aa956467",
    port=2763
)
cursor = conn.cursor()
import csv

def icsv(f):
    with open(f, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            name  = row[0]  
            phone = row[1]  
            cursor.execute(
                "INSERT INTO phonebook (name, phone) VALUES (%s, %s)",
                (name, phone)
    )
    conn.commit() 
def ie():
    name  = input("N ")
    phone = input("P ")
    cursor.execute(
        "INSERT INTO phonebook (name, phone) VALUES (%s, %s)",
        (name, phone)
    )
    conn.commit() 
def update():
    name = input("N f ch ")
    print("ch cho ")
    print("Name ")
    print("Phone ")
    choice = input("1 or 2 ")
    if choice == "1":
        new_name = input("New Na ")
        cursor.execute(
            "UPDATE phonebook SET name = %s WHERE name = %s",
            (new_name, name)
        )
    elif choice == "2":
        new_phone = input("Nw Ph ")
        cursor.execute(
            "UPDATE phonebook SET phone = %s WHERE name = %s",
            (new_phone, name)
        )
    conn.commit()
def search():
    print("Find")
    print("Na")
    print("Ph")
    choice = input("1 or 2 ")

    if choice == "1":
        name = input("Na ")
        cursor.execute(
            "SELECT * FROM phonebook WHERE name = %s",
            (name,)
        )
    elif choice == "2":
        phone = input("Ph ")
        cursor.execute(
            "SELECT * FROM phonebook WHERE phone = %s",
            (phone,)
        )

    results = cursor.fetchall() 

    if results:
        for row in results:
            print(f"ID: {row[0]}, Na: {row[1]}, Ph: {row[2]}")
    else:
         print("Леее радной нету такого")
def Del():
    print("Del:")
    print("Na")
    print("Ph")
    choice = input("1 or 2 ")

    if choice == "1":
        name = input("Na: ")
        cursor.execute(
            "DELETE FROM phonebook WHERE name = %s",
            (name,)
        )
    elif choice == "2":
        phone = input("Ph: ")
        cursor.execute(
            "DELETE FROM phonebook WHERE phone = %s",
            (phone,)
        )
    conn.commit()
Del()