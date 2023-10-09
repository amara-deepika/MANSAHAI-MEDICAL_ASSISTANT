import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",passwd="Omganapati@1",database="mansahaidatabase")
mycursor=mydb.cursor()
mycursor.execute("select * from mansahai")
d=mycursor.fetchall()
for i in d:
    print(i)

