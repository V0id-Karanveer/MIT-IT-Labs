import sqlite3

conn =sqlite3.connect('test.db')

conn.execute('''create table customer(
             acctno int primary key,
             name text,
             bal int
); ''')

conn.execute("insert into customer values(1,'lol',65000);")
conn.execute("insert into customer values(2,'lol2',76000);")
conn.execute("insert into customer values(3,'lol3',30000);")

conn.commit()

search = input("Enter acc no.")
cursor = conn.execute("select * from customer where acctno="+search)

for i in cursor:
    print(i)

print("\nPeople with >50000:")
cursor = conn.execute("select * from customer where bal>50000")

for i in cursor:
    print(i)
