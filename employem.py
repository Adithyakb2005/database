import sqlite3
con=sqlite3.connect("employee.db")
try:
    con.execute("create table staff(id int,name text,age int,position text,salary real)")
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
        position=input("enter the position:")
        salary=float(input("enter the salary:"))
        con.execute("insert into staff values(?,?,?,?,?)",(id,name,age,position,salary))
        con.commit()
        print("employee added successfully")
    elif ch=='2':
        data=con.execute("select * from staff")
        print(data)
        for i in data:
            print(i)
    elif ch=='3':
        name = input("Enter the name: ")
        new_salary = float(input("Enter the new salary: "))
        con.execute("update staff set salary=? where name=?",(new_salary, name))
        con.commit()
        print("Salary updated successfully.")
        con.commit()
    elif ch=='4':
        n=input("enter id:")
        con.execute("delete from staff where id=?",(n))
        con.commit()
        print("delete successfully")
    elif ch=='5':
        print("exit")
        break