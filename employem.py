import sqlite3
con=sqlite3.connect("employee.db")
try:
    con.execute("create table staff(id int,name text,age int,email text,salary real)")
except:
    pass

while True:
    print("1.add")
    print("2.display")
    print("3.update")
    print("4.delete")
    print("5.exit")
    ch=input("enter your choice: ")
    if ch=='1':
        id=int(input("enter the id:"))
        name=str(input("enter the name:"))
        age=int(input("enter the age:"))
    
        con.execute("insert into staff(id,name,age)values(?,?,?)",(id,name,age))