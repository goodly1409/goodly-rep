import sqlite3


conn = sqlite3.connect('students.db')
cur = conn.cursor()

cur.execute("DROP TABLE IF EXISTS num1")

query = "CREATE TABLE IF NOT EXISTS stud1 (id INT, name TEXT, surname TEXT, mid_name TEXT, grade TEXT, nickname TEXT)"
cur.execute(query)

cur.execute('INSERT INTO stud1 VALUES(1,"Petya", "Petrov", "Alexandrovich", "5A", "Petka")')
stud2 = (2, "Andrey", "Ivanov", "Andreyevich", "5B", "Cowboy")
cur.execute("INSERT INTO stud1 VALUES(?, ?, ?, ?, ?, ?)", stud2)

cur.execute('UPDATE stud1 SET id = 3 where name = "Petya"')

cur.execute("SELECT * FROM stud1")
# cur.execute("SELECT author FROM stud1")
# cur.execute("SELECT * FROM book WHERE year=1799")
rows = cur.fetchall()
# print(rows)
for row in rows:
    print(row)
conn.commit()
conn.close()