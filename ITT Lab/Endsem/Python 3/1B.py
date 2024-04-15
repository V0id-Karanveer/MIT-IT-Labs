import sqlite3
conn = sqlite3.connect('test.db')

conn.execute("insert into student values(088,'Karanveer','IT',9.14);")
conn.execute("insert into student values(070,'lol','CCE',9.00);")
conn.execute("insert into student values(050,'lol2','CSE',8.50);")

conn.commit()
conn.close()