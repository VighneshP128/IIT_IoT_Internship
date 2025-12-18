import mysql.connector
from datetime import datetime
connection=mysql.connector.connect(
    host="127.0.0.1",
    port=3306,
    user="root",
    password="root",
    database="iot_data1",
    use_pure=True

)
query=f"select * from sen_reading where temperature<60;"
cursor=connection.cursor()
cursor.execute(query)
sen_reading = cursor.fetchall()

for s in sen_reading:
    print(s)
cursor.close()
connection.close()