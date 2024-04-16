import mysql.connector

database = mysql.connector.connect(
    host ='localhost',
    user ='root',
    passwd = 'b2xyzpqr'
)

# prepare a cursor object

cursorObject = database.cursor();

cursorObject.execute("CREATE DATABASE django_crm")
print("All Done")