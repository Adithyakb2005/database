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
    elif ch == '3':
        name_to_update = input("Enter name of staff member to update: ")
        new_salary = float(input("Enter new salary: "))
        
        update_query = "UPDATE staff SET salary = ? WHERE name = ?"
        con.execute(update_query, (new_salary, name_to_update))
        con.commit()
        print("Staff updated successfully.")
    elif ch=='4':
        n=input("enter id:")
        con.execute("delete from staff where id=?",(n))
        con.commit()
        print("delete successfully")
    elif ch=='5':
        print("exit")
        break