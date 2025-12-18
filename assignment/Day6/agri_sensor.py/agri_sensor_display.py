import mysql.connector
from datetime import datetime
connection=mysql.connector.connect(
    host="127.0.0.1",
    port=3306,
    user="root",
    password="root",
    database="smart_agri_iot1",
    use_pure=True

)
query=f"select * from agri_info where Moisture_level<50;"
cursor=connection.cursor()
cursor.execute(query)
agri_info = cursor.fetchall()
for s in agri_info :
    print(s)
cursor.close()
connection.close()