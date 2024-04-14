import sqlite3
import os

# Путь к файлу базы данных SQLite
db_file = 'dhcp_snooping.db'

# Проверяем, существует ли файл базы данных
if not os.path.exists(db_file):
    # Если файл не существует, создаем базу данных и загружаем схему
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()

    # Чтение схемы из файла
    with open('dhcp_snooping_schema.sql', 'r') as f:
        schema = f.read()

    # Выполнение схемы
    cursor.executescript(schema)

    # Сохранение изменений и закрытие соединения
    conn.commit()
    conn.close()

    print("Создаю базу данных...")
else:
    print("База данных существует")