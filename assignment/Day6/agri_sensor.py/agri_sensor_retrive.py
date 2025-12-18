import mysql.connector
from datetime import datetime
Connection=mysql.connector.connect (
    host="127.0.0.1",
    port = 3306,
    user = "root",
    password = "root",
    database = "smart_agri_iot1",
    use_pure = True
)

query = "select * from agri_info";


cursor = Connection.cursor()

cursor.execute(query)

agri_info= cursor.fetchall()


for agri_info in agri_info:
    print(agri_info)
    
cursor.close()
Connection.close()