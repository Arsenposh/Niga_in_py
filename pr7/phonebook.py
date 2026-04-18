import csv
from connect import get_connection
conn = get_connection()
cursor = conn.cursor()
def create_table():
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS phonebook (
            id SERIAL PRIMARY KEY,
            name VARCHAR(100),
            phone VARCHAR(20)
        )
    """)
    conn.commit()
def insert_from_csv(filename):
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        next(reader)

        for row in reader:
            cursor.execute(
                "INSERT INTO phonebook (name, phone) VALUES (%s, %s)",
                (row[0], row[1])
            )
    conn.commit()
    print("CSV загружен")
def insert_from_console():
    name = input("Имя: ")
    phone = input("Телефон: ")

    cursor.execute(
        "INSERT INTO phonebook (name, phone) VALUES (%s, %s)",
        (name, phone)
    )
    conn.commit()
    print("Добавлено!")
def update_contact():
    name = input("Кого изменить: ")

    print("1 - Имя")
    print("2 - Телефон")
    choice = input("Выбор: ")

    if choice == "1":
        new_name = input("Новое имя: ")
        cursor.execute(
            "UPDATE phonebook SET name=%s WHERE name=%s",
            (new_name, name)
        )

    elif choice == "2":
        new_phone = input("Новый телефон: ")
        cursor.execute(
            "UPDATE phonebook SET phone=%s WHERE name=%s",
            (new_phone, name)
        )

    conn.commit()
    print("Обновлено!")

def search_contacts():
    print("1 - По имени")
    print("2 - По префиксу")
    choice = input("Выбор: ")

    if choice == "1":
        name = input("Имя: ")
        cursor.execute(
            "SELECT * FROM phonebook WHERE name ILIKE %s",
            (  name)
        )

    elif choice == "2":
        prefix = input("Префикс: ")
        cursor.execute(
            "SELECT * FROM phonebook WHERE phone LIKE %s",
            (prefix + '%',)
        )

    results = cursor.fetchall()

    if results:
        for row in results:
            print(f"ID: {row[0]}, Name: {row[1]}, Phone: {row[2]}")
    else:
        print("Ничего не найдено")
def delete_contact():
    print("1 - По имени")
    print("2 - По телефону")
    choice = input("Выбор: ")
    if choice == "1":
        name = input("Имя: ")
        cursor.execute(
            "DELETE FROM phonebook WHERE name=%s",
            (name,)
        )
    elif choice == "2":
        phone = input("Телефон: ")
        cursor.execute(
            "DELETE FROM phonebook WHERE phone=%s",
            (phone,)
        )
    conn.commit()
<<<<<<< HEAD
    print("Удалено!")
def menu():
    while True:
        print("\n--- PHONEBOOK ---")
        print("1 - Create table")
        print("2 - Import CSV")
        print("3 - Add contact")
        print("4 - Update")
        print("5 - Search")
        print("6 - Delete")
        print("0 - Exit")

        choice = input("Choice: ")

        if choice == "1":
            create_table()
        elif choice == "2":
            insert_from_csv("contacts.csv")
        elif choice == "3":
            insert_from_console()
        elif choice == "4":
            update_contact()
        elif choice == "5":
            search_contacts()
        elif choice == "6":
            delete_contact()
        elif choice == "0":
            break
        else:
            print("Ошибка")
menu()
conn.close()
=======
icsv("pr7/contacts.csv")
ie()
Del()
search()
update()
>>>>>>> e56d20a645b8b1222b55aca622e85ab6d2d9f693
