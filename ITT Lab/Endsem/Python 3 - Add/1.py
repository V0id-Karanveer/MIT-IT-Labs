import sqlite3

conn = sqlite3.connect('test.db')

conn.execute('''
create table customer(
             id int primary key,
             phone int,
             email text
);
             ''')

noforows = int(input("enter no. of customers?"))
id = 0
for i in range(noforows):
    id+=1
    while 1:
        phone = input("enter phone number: ")
        if len(phone) !=10:
            print("wrong phone number , input again")
        else:
            break
    while 1:
        email = input("Enter email: ")
        if "@" not in email or email[-4:] != ".com":
            print("wrong email , enter again")
        else: 
            break
    conn.execute("insert into customer values("+str(id)+","+phone+",'"+email+"');")

conn.commit()
cursor = conn.execute("select * from customer;")

for i in cursor:
    print(i)

conn.close()
