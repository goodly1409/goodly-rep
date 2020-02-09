# Базовые команды SQL
#
# 1. Создание таблицы
# CREATE TABLE IF NOT EXISTS user(id INT, name TEXT, year INT(20), age REAL (20) NOT NULL)
#
# 2. Вставка данных
# INSERT INTO user VALUES(1, 'Bob', 2019, 22.5)
#
# 3. Обновление данных
# UPDATE user SET name = 'Rolf' WHERE name = 'Bob'
#
# 4. Выбор данных
# SELECT * FROM user
# SELECT name, age FROM user
#
# 5.Удаление данных
# DELETE FROM user WHERE name = 'Rolf'
#
# 6. Удаление таблицы
# DROP IF EXISTS TABLE table_name
#
# 7. Удаление базы данных
# DROP DATABASE database


import sqlite3
# Сначала устанавливается соединение, а затем создаётся объект курсора с использованием объекта соединения след образом

conn = sqlite3.connect('db1.db')  # если такой БД не существует то она создастся
cur = conn.cursor()

cur.execute("DROP TABLE IF EXISTS book")

query = "CREATE TABLE IF NOT EXISTS book (author TEXT, year INT)"
cur.execute(query)

cur.execute("INSERT INTO book VALUES('Pushkin', 1799)")
book1 = ("Esenin", 1890)
cur.execute("INSERT INTO book VALUES(?, ?)", book1)

cur.execute('UPDATE book SET year = 1895 where author = "Esenin"')

cur.execute("SELECT * FROM book")
# cur.execute("SELECT author FROM book")
# cur.execute("SELECT * FROM book WHERE year=1799")
rows = cur.fetchall()
# print(rows)
for row in rows:
    print(row)
conn.commit()
conn.close()

