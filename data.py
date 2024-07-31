import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="Adithyakb",
  password="adithyakb@2005"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE mydatabase")


