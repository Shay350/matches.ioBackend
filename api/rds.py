import mysql.connector

mydb = mysql.connector.connect(
    user='admin',        # The username you set up
    password='password',    # The password for your user
    database='database-1' # The database you want to connect to
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE mydatabase")