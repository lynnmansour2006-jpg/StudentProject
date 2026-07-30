import sqlite3
connection=sqlite3.connect("student.db")
cursor=connection.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS students(
id INTEGER PRIMARY KEY,
name TEXT NOT NULL,
age INTEGER,
email TEXT)
""")
connection.commit()
connection.close()
print("database created")
