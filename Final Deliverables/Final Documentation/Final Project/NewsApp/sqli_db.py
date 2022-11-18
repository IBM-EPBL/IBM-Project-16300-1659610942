import sqlite3

conn = sqlite3.connect('user.db')
print("Opened database successfully")

conn.execute('CREATE TABLE user(pid integer primary key,name text,mail BLOB,password )')
print("Table created successfully")
conn.close()