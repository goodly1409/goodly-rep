import sqlite3

conn = sqlite3.connect('students.db')
cur = conn.cursor()

cur.execute("PRAGMA foreign_keys=on")

cur.execute("CREATE TABLE IF NOT EXISTS classes (id INT NOT NULL PRIMARY KEY,"
            "class CHAR(3), num_of_stud INT(2), teacher CHAR)")

cur.execute("CREATE TABLE IF NOT EXISTS students (id INT NOT NULL PRIMARY KEY, "
            "familia CHAR, imya CHAR, otchestvo CHAR, id_classes INT NOT NULL, age INT(2), "
            "FOREIGN KEY (id_classes), REFERENCES classes (id)")

cur.execute("CREATE TABLE IF NOT EXISTS marks (id INT NOT NULL PRIMARY KEY,"
            "mark INT(5), id_subjects INT(3), id_students INT()")

cur.execute("CREATE TABLE IF NOT EXISTS subjects (id INT NOT NULL PRIMARY KEY,"
            "subject CHAR")

classes = ((1, "5А", 25, "Сергеева Наталья Петровна"),
           (2, "6А", 20, "Морозов Виталий Борисович"),
           (3, "10Б", 27, "Сидорова Ирина Вячеславовна"))
for i in classes:
    cur.execute("INSERT INTO classes VALUES (?, ?, ?, ?)", i)

students = ((1, "Иванов", "Иван", "Иванович", 2, 15),
            (2, "Семёнов", "Сергей", "Петрович", 1, 14))
for i in students:
    cur.execute("INSERT INTO students VALUES(?, ?, ?, ?, ?, ?)", i)

