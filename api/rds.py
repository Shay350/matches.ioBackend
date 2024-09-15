import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user='root',        # The username you set up
    password='password',    # The password for your user
)

mycursor = mydb.cursor()

#mycursor.execute("CREATE DATABASE database1")
#mycursor.execute()
mycursor.execute("SELECT * FROM database1.JOB_POSTINGS;")

# Fetch all rows from the executed query
rows = mycursor.fetchall()

# Print the result
for row in rows:
    print(row)