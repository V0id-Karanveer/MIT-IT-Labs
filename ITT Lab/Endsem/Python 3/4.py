import sqlite3

conn = sqlite3.connect('test.db')

regno = input("enter regno to update cgpa: ")
cgpa = input("enter new cgpa: ")
conn.execute("update student set cgpa="+cgpa+" where regno="+regno+";")
conn.commit()
cursor = conn.execute("select * from student;")
for i in cursor:
    print(i)

conn.close()