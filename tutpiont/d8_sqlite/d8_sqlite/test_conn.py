import sqlite3

conn = sqlite3.connect('database.db')
print('Connected to database')

conn.execute('CREATE TABLE students (name TEXT, addr TEXT, city TEXT, pin TEXT)')
print('students table created ...')

conn.close()