import sqlite3

conn = sqlite3.connect('test.db')

regno = input("enter regno to check: ")

cursor = conn.execute("select * from student where regno="+regno+";")


for row in cursor:
    print(row)

