import sqlite3

conn = sqlite3.connect('test.db')

conn.execute('''create table if not exists exam(
             destination_id int primary key,
             destination_name text,
             country text,
             city text,
             duration int,
             cost int,
             budget int
);
 ''')

data = [
    (1,"gurgaon","india","hry",10,1000,800),
    (2,"chandigarh","india","punjab",8,1000,1800),
    (3,"amritsar","india","punjab",6,900,700)
]

conn.executemany("insert into exam values(?,?,?,?,?,?,?)",data)


n = int(input("How many do u want to input?"))

for i in range(n):
    while 1:
        id = int(input("Enter id"))
        if id>10 or id <=1:
            print("wring , enter again")
        else:
            break
    name = input("Enter name")
    country = input("Enter country")
    city = input("Enter city") 
    while 1:
        dur = int(input("enter duration"))
        if dur<0:
            print("wrong , enter again")
        else:
            break
    while 1:
        budget = int(input("enter budget"))
        if budget<0:
            print("wrong , enter again")
        else:
            break
    while 1:
        cost = int(input("enter cost"))
        if cost<0:
            print("wrong , enter again")
        else:
            break
    conn.execute("insert into exam values("+str(id)+","+"'"+name+"','"+country+"','"+city+"',"+str(dur)+","+str(budget)+","+str(cost)+");")

conn.commit()
header = ("id","name","country","city","duration","cost","budget")
cursor = conn.execute("select * from exam order by destination_name asc")
print(header)
for i in cursor:
    print(i)

cursor = conn.execute("select avg(cost) from exam")
for i in cursor:
    print("Average cost is "+str(i[0]))

conn.execute("update exam set budget=cost where cost> budget")
conn.commit()

header = ("id","name","country","city","duration","cost","budget")
cursor = conn.execute("select * from exam")
print(header)
for i in cursor:
    print(i)



    




