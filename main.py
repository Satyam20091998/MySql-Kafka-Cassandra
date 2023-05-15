import mysql.connector
import time
from mysql.connector import Error

try: 
    connection = mysql.connector.connect(
        host='localhost',
        user='your_user',
        password='your_password',
        database='your_database'
    )

except Error as e:
    print("Error while connecting to MySQL", e)

cursor = connection.cursor()
qry="insert into  demo1 values(1,'satyam');"
insert_query = "INSERT INTO demo1 (id, name) VALUES (%s, %s)"
for i in range(5):
    data = (i, 'value2')

    try:
        cursor.execute(insert_query, data)
        connection.commit()
        print("Data inserted successfully-",i)
        time.sleep(3)
    except Error as e:
        print("Error while inserting data into MySQL", e)

    
cursor.close()
connection.close()

