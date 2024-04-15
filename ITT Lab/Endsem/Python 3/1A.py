import sqlite3

conn = sqlite3.connect('test.db')

conn.execute(''' 
create table student(
            regno int primary key not null,
            name text,
            branch text check(branch in ('IT','CCE','CSE')),
            cgpa float
);
''')
conn.commit()
conn.close()