import mysql.connector

dataBase = mysql.connector.connect(
    
    host = 'localhost',
    user = 'root',
    passwd = '123456'
)

# prepare cursor object - used to make connection for executing sql queries.

cursorObject = dataBase.cursor()


# create a database

cursorObject.execute("CREATE DATABASE nadav")

print("All Done!")


## 11:04

#  python manage.py migrate - להבין


