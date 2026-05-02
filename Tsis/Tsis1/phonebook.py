import csv
import json
import os
from connect import get_connection
 
conn = get_connection()
cursor = conn.cursor()
def init_db():
    for filename in ["schema.sql", "procedures.sql"]:
        try:
            with open(filename, "r", encoding="utf-8") as f:
                sql = f.read()
            cursor.execute(sql)
            conn.commit()
        except FileNotFoundError:
            print(f"Файл {filename} не найден!")

init_db()
def filter_by_group():
    cursor.execute("SELECT id, name FROM groups")
    groups = cursor.fetchall()
    for g in groups:
        print(f"{g[0]}. {g[1]}")
 
    group_id = input("Введите ID группы: ")
    cursor.execute("""
        SELECT c.id, c.name, c.email, c.birthday, g.name, p.phone, p.type
        FROM contacts c
        LEFT JOIN groups g ON c.group_id = g.id
        LEFT JOIN phones p ON c.id = p.contact_id
        WHERE g.id = %s
    """, (group_id,))
 
    rows = cursor.fetchall()
    for row in rows:
        print(row)
def search_by_email():
    email = input("Введите email (или часть): ")
    cursor.execute("""
        SELECT c.id, c.name, c.email, c.birthday, g.name, p.phone, p.type
        FROM contacts c
        LEFT JOIN groups g ON c.group_id = g.id
        LEFT JOIN phones p ON c.id = p.contact_id
        WHERE c.email ILIKE %s
    """, ('%' + email + '%',))
 
    rows = cursor.fetchall()
    for row in rows:
        print(row)
def sort_contacts():
    print("1 - По имени")
    print("2 - По дню рождения")
    print("3 - По дате добавления")
    choice = input("Выбор: ")
 
    if choice == "1":
        order = "c.name"
    elif choice == "2":
        order = "c.birthday"
    else:
        order = "c.created_at"
 
    cursor.execute(f"""
        SELECT c.id, c.name, c.email, c.birthday, g.name, p.phone, p.type
        FROM contacts c
        LEFT JOIN groups g ON c.group_id = g.id
        LEFT JOIN phones p ON c.id = p.contact_id
        ORDER BY {order}
    """)
 
    rows = cursor.fetchall()
    for row in rows:
        print(row)
def paginated_view():
    page_size = 5
    offset = 0
 
    while True:
        cursor.execute("SELECT * FROM phonebook ORDER BY id LIMIT %s OFFSET %s", (page_size, offset))
        rows = cursor.fetchall()
 
        print(f"\n--- Страница {offset // page_size + 1} ---")
        for row in rows:
            print(f"ID: {row[0]}, Имя: {row[1]}, Телефон: {row[2]}")
 
        cmd = input("\n[n]след  [p]пред  [q]выход: ").strip().lower()
 
        if cmd == 'n':
            if len(rows) < page_size:
                print("Это последняя страница.")
            else:
                offset += page_size
        elif cmd == 'p':
            if offset == 0:
                print("Вы на первой странице.")
            else:
                offset -= page_size
        elif cmd == 'q':
            break
def add_contact():
    name = input("Имя: ")
    email = input("Email: ")
    birthday = input("День рождения (YYYY-MM-DD): ") or None
 
    cursor.execute("SELECT id, name FROM groups")
    groups = cursor.fetchall()
    for g in groups:
        print(f"{g[0]}. {g[1]}")
    group_id = input("ID группы: ") or None
 
    cursor.execute("""
        INSERT INTO contacts (name, email, birthday, group_id)
        VALUES (%s, %s, %s, %s) RETURNING id
    """, (name, email, birthday, group_id))
    contact_id = cursor.fetchone()[0]
    conn.commit()
 
    phone = input("Телефон: ")
    ptype = input("Тип (home/work/mobile): ")
    cursor.execute(
        "INSERT INTO phones (contact_id, phone, type) VALUES (%s, %s, %s)",
        (contact_id, phone, ptype)
    )
    conn.commit()
    print("Контакт добавлен!")

def add_phone():
    name = input("Имя контакта: ")
    phone = input("Новый телефон: ")
    ptype = input("Тип (home/work/mobile): ")
    cursor.execute("CALL add_phone(%s, %s, %s)", (name, phone, ptype))
    conn.commit()
    print("Телефон добавлен!")

def move_to_group():
    name = input("Имя контакта: ")
    group = input("Название группы: ")
    cursor.execute("CALL move_to_group(%s, %s)", (name, group))
    conn.commit()
    print("Контакт перемещён!")

def search_all():
    query = input("Поиск (имя / email / телефон): ")
    cursor.execute("SELECT * FROM search_contacts(%s)", (query,))
    rows = cursor.fetchall()
    for row in rows:
        print(row)
def export_json():
    cursor.execute("""
        SELECT c.id, c.name, c.email, c.birthday::TEXT, g.name
        FROM contacts c
        LEFT JOIN groups g ON c.group_id = g.id
    """)
    contacts = cursor.fetchall()
 
    result = []
    for c in contacts:
        cursor.execute("SELECT phone, type FROM phones WHERE contact_id = %s", (c[0],))
        phones = [{"phone": p[0], "type": p[1]} for p in cursor.fetchall()]
        result.append({
            "name": c[1],
            "email": c[2],
            "birthday": c[3],
            "group": c[4],
            "phones": phones
        })
 
    with open("contacts_export.json", "w", encoding="utf-8") as f:
        json.dump(result, f, ensure_ascii=False, indent=2)
    print("Экспорт готов: contacts_export.json")
def import_json():
    filename = input("Имя файла (contacts_export.json): ").strip() or "contacts_export.json"
 
    with open(filename, "r", encoding="utf-8") as f:
        data = json.load(f)
 
    for contact in data:
        name = contact["name"]
 
        # Проверяем дубликат
        cursor.execute("SELECT id FROM contacts WHERE name = %s", (name,))
        existing = cursor.fetchone()
 
        if existing:
            choice = input(f"'{name}' уже есть. 1-пропустить, 2-перезаписать: ")
            if choice != "2":
                continue
            cursor.execute("UPDATE contacts SET email=%s, birthday=%s WHERE id=%s",
                           (contact.get("email"), contact.get("birthday"), existing[0]))
            cursor.execute("DELETE FROM phones WHERE contact_id=%s", (existing[0],))
            for p in contact.get("phones", []):
                cursor.execute(
                    "INSERT INTO phones (contact_id, phone, type) VALUES (%s, %s, %s)",
                    (existing[0], p["phone"], p["type"])
                )
        else:
            group_id = None
            if contact.get("group"):
                cursor.execute("SELECT id FROM groups WHERE name = %s", (contact["group"],))
                g = cursor.fetchone()
                if g:
                    group_id = g[0]
 
            cursor.execute("""
                INSERT INTO contacts (name, email, birthday, group_id)
                VALUES (%s, %s, %s, %s) RETURNING id
            """, (name, contact.get("email"), contact.get("birthday"), group_id))
            contact_id = cursor.fetchone()[0]
 
            for p in contact.get("phones", []):
                cursor.execute(
                    "INSERT INTO phones (contact_id, phone, type) VALUES (%s, %s, %s)",
                    (contact_id, p["phone"], p["type"])
                )
 
        conn.commit()
    print("Импорт завершён!")
def import_csv():
    filename = input("Имя CSV файла (contacts.csv): ").strip() or "contacts.csv"
    filepath = os.path.join(os.path.dirname(os.path.abspath(__file__)), filename)
    
    with open(filepath, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            name       = row.get("name", "")
            phone      = row.get("phone", "")
            phone_type = row.get("phone_type", "mobile")
            email      = row.get("email") or None
            birthday   = row.get("birthday") or None
            group      = row.get("group") or None
 
            group_id = None
            if group:
                cursor.execute("SELECT id FROM groups WHERE name = %s", (group,))
                g = cursor.fetchone()
                if g:
                    group_id = g[0]
 
            cursor.execute("""
                INSERT INTO contacts (name, email, birthday, group_id)
                VALUES (%s, %s, %s, %s) RETURNING id
            """, (name, email, birthday, group_id))
            contact_id = cursor.fetchone()[0]
 
            if phone:
                cursor.execute(
                    "INSERT INTO phones (contact_id, phone, type) VALUES (%s, %s, %s)",
                    (contact_id, phone, phone_type)
                )
            conn.commit()
 
    print("CSV импорт завершён!")
 
def menu():
    while True:
        print("\n--- PHONEBOOK ---")
        print("1  - Добавить контакт")
        print("2  - Поиск (имя/email/телефон)")
        print("3  - Фильтр по группе")
        print("4  - Поиск по email")
        print("5  - Сортировка")
        print("6  - Просмотр по страницам")
        print("7  - Добавить телефон контакту")
        print("8  - Переместить в группу")
        print("9  - Экспорт в JSON")
        print("10 - Импорт из JSON")
        print("11 - Импорт из CSV")
        print("0  - Выход")
 
        choice = input("Выбор: ")
 
        if   choice == "1":  add_contact()
        elif choice == "2":  search_all()
        elif choice == "3":  filter_by_group()
        elif choice == "4":  search_by_email()
        elif choice == "5":  sort_contacts()
        elif choice == "6":  paginated_view()
        elif choice == "7":  add_phone()
        elif choice == "8":  move_to_group()
        elif choice == "9":  export_json()
        elif choice == "10": import_json()
        elif choice == "11": import_csv()
        elif choice == "0":  break
        else: print("Неверный выбор")
menu()
conn.close()
 

