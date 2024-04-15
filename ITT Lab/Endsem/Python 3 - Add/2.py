import sqlite3

conn = sqlite3.connect('test.db')

conn.execute('''create table student2(
             id int primary key,
             mark1 int,
             mark2 int
); ''')

conn.commit()

conn.execute("insert into student2 values(1,80,60);")
conn.execute("insert into student2 values(2,70,70);")
conn.execute("insert into student2 values(3,60,80);")
conn.execute("insert into student2 values(4,50,90);")
conn.commit()

cursor = conn.execute("select * from student2;")

for i in cursor:
    print(i[0]," has total ",i[1]+i[2])
