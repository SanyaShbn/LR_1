import sqlite3

connection = sqlite3.connect('students.db')
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Students (
name TEXT NOT NULL,
surname TEXT PRIMARY KEY,
group_numb INTEGER,
form TEXT NOT NULL
)
''')

connection.commit()
connection.close()
