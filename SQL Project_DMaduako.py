import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Mysterious01"
)

print(mydb)

mycursor = mydb.cursor()

#mycursor.execute("CREATE DATABASE menagerie")
mycursor.execute("DROP DATABASE menagerie")
mycursor.execute("SHOW DATABASES")

for x in mycursor:
  print(x)
