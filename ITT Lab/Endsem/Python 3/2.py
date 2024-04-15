import sqlite3

conn = sqlite3.connect('test.db')
while 1:
    regno = input("Enter regno: ")
    flg = 1
    for i in regno:
        if i not in "0123456789":
            print("Wrong input , enter again")
            regno = input("Enter regno: ")
            flg=0
    if flg == 1:
        break
        
name = input("Enter name: ")

while 1:
    branch = input("Enter branch: ")
    if branch not in ("IT","CCE","CSE"):
        print("wrong input enter again")
    else:
        break

while 1:
    cgpa = float(input("Enter CGPA: "))
    if not( cgpa<10 and cgpa >0):
        print("Wrong input , enter again")
    else:
        break

conn.execute("insert into student values("+regno+",'"+name+"'"+",'"+branch+"',"+str(cgpa)+");")
conn.commit()

