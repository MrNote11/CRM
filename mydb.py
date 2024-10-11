import mysql.connector

database = mysql.connector.connect(host = 'localhost',
                                   user = 'root',
                                   password= 'MrNote11',
                                   )

CursorObject = database.cursor()

CursorObject.execute("CREATE DATABASE newbie")

print("All Done")
