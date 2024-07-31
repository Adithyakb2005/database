import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="Adithyakb",
  password="adithyakb@2005",
  database="SYNNEFO")


cursor = mydb.cursor()
cursor.execute("create table if not exists details(id int primary key,address varchar(255),position varchar(255))")
while True:
    print("\n1.add\n2.exit\n3.join")
    ch=input("enter your choice:")
    if ch=='1':
        l= int (input("Enter limit : "))
        for i in range(l):
            id= int(input('enter employee id: '))
            address=str(input("enter address: "))
            position=str(input('enter position: '))
            cursor.execute('INSERT INTO details (id,address,position) VALUES (%s,%s,%s)',(id,address,position))
            mydb.commit()
    elif ch=='2':
        break
    elif ch=='3':
        data=cursor.execute("select employe.emp_id,employe.name,employe.age,employe.email,employe.position,employe.salary,details.address,details.position from employe cross join details")
        m=cursor.fetchall()
        for i in m:
            print(i)
    else:
        print('invalid choice.....')
    # elif ch == '2':
    #     id = int(input('enter employee id: '))
    #     address=str(input("enter address: "))
    #     position = input('enter position: ')
    #     cursor.execute('UPDATE details SET address=%s,position=%s,WHERE id=%s',(address,position,id))
    #     print("employee information updated successfully")
    #     mydb.commit()
    # elif ch == '3':
    #     id = int(input('enter id of details to delete: '))
    #     cursor.execute('DELETE FROM details WHERE id=%s', (id,))
    #     print("deleted the employee")
    #     mydb.commit()
    # elif ch == '4':
    #     id = int(input('enter id to search: '))
    #     cursor.execute('SELECT * FROM details WHERE id=%s', (id,))
    #     data = cursor.fetchall()
    #     print('{:<10}{:<10}{:<10}'.format('id','address', 'position'))
    #     print('-' * 40)
    #     if data:
    #         for i in data:
    #             print("{:<10}{:<10}{:<10}".format(i[0], i[1], i[2]))
    #     else:
    #         print('id not available')
    # elif ch == '5':
    #     cursor.execute('SELECT * FROM details')
    #     data = cursor.fetchall()
    #     print('{:<10}{:<10}{:<10}'.format('id','address', 'position'))
    #     print('-' * 40)
    #     for i in data:
    #         print("{:<10}{:<10}{:<10}".format(i[0], i[1], i[2]))
  