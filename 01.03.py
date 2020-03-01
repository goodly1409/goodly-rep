import sqlite3

conn = sqlite3.connect('students.db')
cur = conn.cursor()

cur.execute("DROP TABLE IF EXISTS classes")
cur.execute("DROP TABLE IF EXISTS students")
cur.execute("DROP TABLE IF EXISTS marks")
cur.execute("DROP TABLE IF EXISTS subjects")

cur.execute("PRAGMA foreign_keys=on")

cur.execute("CREATE TABLE IF NOT EXISTS classes (id INT NOT NULL PRIMARY KEY, "
            "class CHAR, num_of_stud INT, teacher CHAR)")

cur.execute("CREATE TABLE IF NOT EXISTS students (id INT NOT NULL PRIMARY KEY, "
            "familia CHAR, imya CHAR, otchestvo CHAR, id_classes INT, age INT, "
            "FOREIGN KEY (id_classes) REFERENCES classes (id))")

cur.execute("CREATE TABLE IF NOT EXISTS marks (id INT NOT NULL PRIMARY KEY, "
            "mark INT, id_subjects INT, id_students INT)")

cur.execute("CREATE TABLE IF NOT EXISTS subjects (id INT NOT NULL PRIMARY KEY, "
            "subject CHAR)")

classes = ((1, "5А", 25, "Сергеева Наталья Петровна"),
           (2, "6А", 20, "Морозов Виталий Борисович"),
           (3, "10Б", 27, "Сидорова Ирина Вячеславовна"))
for i in classes:
    cur.execute("INSERT INTO classes VALUES (?, ?, ?, ?)", i)

students = ((1, "Иванов", "Иван", "Иванович", 2, 15),
            (2, "Семёнов", "Сергей", "Петрович", 1, 14))
for i in students:
    cur.execute("INSERT INTO students VALUES(?, ?, ?, ?, ?, ?)", i)

marks = ((1, 1, 1, 1),
         (2, 2, 2, 2))
for i in marks:
    cur.execute("INSERT INTO marks VALUES(?, ?, ?, ?)", i)

subjects = ((1, "English"),
            (2, "Russian"),
            (3, "Math"))
for i in subjects:
    cur.execute("INSERT INTO subjects VALUES(?, ?)", i)

cur.execute("SELECT * FROM classes")
rows = cur.fetchall()
print(rows)

cur.execute("SELECT * FROM students")
rows = cur.fetchall()
print(rows)

cur.execute("SELECT * FROM subjects")
rows = cur.fetchall()
print(rows)

cur.execute("SELECT * FROM marks")
rows = cur.fetchall()
print(rows)

conn.commit()
conn.close()
