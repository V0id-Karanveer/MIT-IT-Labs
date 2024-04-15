import sqlite3

conn = sqlite3.connect('test.db')

cursor = conn.execute("select * from student order by cgpa asc;")
for i in cursor:
    print(i)

conn.close()