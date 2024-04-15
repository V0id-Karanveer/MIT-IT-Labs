import sqlite3

conn = sqlite3.connect('test.db')

conn.execute('''create table exam(
             id int primary key,
             name text,
             country,
             city,
             duration int,
             cost int,
             budget int check(budget>0)
)
 ''')

data = [
    (1001,'red fort','india','delhi',50,800,650),
    (1005,'taj mahal','india','agra',50,1000,1200),
    (1080,'great wall','china','border',50,900,750)
]

conn.executemany("insert into exam values(?,?,?,?,?,?,?)",data)

n = int(input("no of inputs?"))

for i in range(n):
    while 1:
        id = int(input("id: "))
        if id>1200 or id < 1000:
            print('wrong')
        else:
            break
    name = input('name: ')
    country = input('country: ')
    city = input('city: ')
    while 1:
        dur = int(input("duration: "))
        if dur<0:
            print('wrong')
        else:
            break
    while 1:
        cost = int(input("cost: "))
        if cost<0:
            print('wrong')
        else:
            break
    while 1:
        budget = int(input("budget: "))
        if budget<0:
            print('wrong')
        else:
            break
    conn.execute("insert into exam values("+str(id)+",'"+name+"','"+country+"','"+city+"',"+str(dur)+","+str(cost)+","+str(budget)+");")

cursor = conn.execute("select * from exam order by name asc")
for i in cursor:
    print(i)

cursor= conn.execute("select avg(cost) from exam")
for i in cursor:
    print("Average cost is: ",i[0])

conn.execute("update exam set budget=cost where budget<cost")

cursor = conn.execute("select * from exam")
for i in cursor:
    print(i)


