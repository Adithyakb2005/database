# import sqlite3
# con=sqlite3.connect("sample.db")
# try:
#     con.execute("create table student(age int,name text,mark real)")
# except:
#     pass
# con.execute("insert into student(age,name,mark)values(22,'manu',70)")
# con.commit()

# import sqlite3
# con=sqlite3.connect("sample.db")
# try:
#     con.execute("create table student(age int,name text,mark real)")
# except:
#     pass
# con.execute("insert into student(age,name,mark)values(22,'manu',70),(23,'anu',75),(24,'vanu',80)")
# con.commit()


# import sqlite3
# con=sqlite3.connect("sample.db")
# try:
#     con.execute("create table student(age int,name text,mark real)")
# except:
#     pass
# age=int(input('age: '))
# name=str(input('name; '))
# mark=float(input('mark'))
# con.execute("insert into student(age,name,mark)values(?,?,?)",(age,name,mark))
# con.commit()

# import sqlite3
# con=sqlite3.connect("sample1.db")
# try:
#     con.execute("create table student(age int,name text,mark real)")
# except:
#     pass
# n=int(input("enter how many students:"))
# for i in range(n):
#     age=int(input('age: '))
#     name=str(input('name; '))
#     mark=float(input('mark'))

#     con.execute("insert into student(age,name,mark)values(?,?,?)",(age,name,mark))
#     con.commit()

# import sqlite3
# con=sqlite3.connect("sample1.db")
# try:
#     con.execute("create table student(age int,name text,mark real)")
# except:
#     pass
# data=con.execute("select * from student")
# print(data)
# for i in data:
#     print(i)

# import sqlite3
# con=sqlite3.connect("sample1.db")
# try:
#     con.execute("create table student(age int,name text,mark real)")
# except:
#     pass
# data=con.execute("select name from student")
# print(data)
# for i in data:
#     print(i)

# import sqlite3
# con=sqlite3.connect("sample1.db")
# try:
#     con.execute("create table student(age int,name text,mark real)")
# except:
#     pass
# data=con.execute("select age from student")
# print(data)
# for i in data:
#     print(i)

#TABLE 

# import sqlite3
# con=sqlite3.connect("sample1.db")
# try:
#     con.execute("create table student(age int,name text,mark real)")
# except:
#     pass
# data=con.execute("select * from student")
# print("{:<10}{:<16}{:<10}".format('name',"age","mark"))
# for i in data:
#     print("{:<10}{:<16}{:<10}".format(i[0],i[1],i[2]))

#WHERE

# import sqlite3
# con=sqlite3.connect("sample1.db")
# try:
#     con.execute("create table student(age int,name text,mark real)")
# except:
#     pass
# data=con.execute("select * from student where age=27")
# print("{:<10}{:<16}{:<10}".format('name',"age","mark"))
# for i in data:
#     print("{:<10}{:<16}{:<10}".format(i[0],i[1],i[2]))

# import sqlite3
# con=sqlite3.connect("sample1.db")
# try:
#     con.execute("create table student(age int,name text,mark real)")
# except:
#     pass
# # name=str(input("name"))
# data=con.execute("select * from student where age>=20")
# print("{:<10}{:<16}{:<10}".format('name',"age","mark"))
# print("-------------------------------")
# for i in data:
#     print("{:<10}{:<16}{:<10}".format(i[0],i[1],i[2]))

# import sqlite3
# con=sqlite3.connect("sample1.db")
# try:
#     con.execute("create table student(age int,name text,mark real)")
# except:
#     pass
# # name=str(input("name"))
# data=con.execute("select * from student where mark>=70")
# print("{:<10}{:<16}{:<10}".format('name',"age","mark"))
# print("-------------------------------")
# for i in data:
#     print("{:<10}{:<16}{:<10}".format(i[0],i[1],i[2]))

# UPDATE

# import sqlite3
# con=sqlite3.connect("sample1.db")
# try:
#     con.execute("create table student(age int,name text,mark real)")
# except:
#     pass
# con.execute("update student set name='sanu p' where name='sumi'")
# con.commit()
# data=con.execute("select * from student")
# print("{:<10}{:<16}{:<10}".format('name',"age","mark"))
# print("-------------------------------")
# for i in data:
#     print("{:<10}{:<16}{:<10}".format(i[0],i[1],i[2]))


# import sqlite3
# con=sqlite3.connect("sample1.db")
# try:
#     con.execute("create table student(age int,name text,mark real)")
# except:
#     pass
# con.execute("update student set age=22 where age='19'")
# con.commit()
# data=con.execute("select * from student")
# print("{:<10}{:<16}{:<10}".format('name',"age","mark"))
# print("-------------------------------")
# for i in data:
#     print("{:<10}{:<16}{:<10}".format(i[0],i[1],i[2]))


# import sqlite3
# con=sqlite3.connect("sample1.db")
# try:
#     con.execute("create table student(age int,name text,mark real)")
# except:
#     pass
# con.execute("update student set mark=96.5 where mark=78")
# con.commit()
# data=con.execute("select * from student")
# print("{:<10}{:<16}".format('name','age'))
# print("-------------------")
# for i in data:
#     print("{:<10}{:<16}".format(i[0],i[1]))


import sqlite3
con=sqlite3.connect("sample1.db")
try:
    con.execute("create table student(age int,name text,mark real)")
except:
    pass
name=str(input("name"))
con.execute("delete from student where name=?",(name,))
con.commit()
data=con.execute("select * from student")
print("{:<10}{:<16}{:<10}".format('name',"age","mark"))
print("-------------------------------")
for i in data:
    print("{:<10}{:<16}{:<10}".format(i[0],i[1],i[2]))
