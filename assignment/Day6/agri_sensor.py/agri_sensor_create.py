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
sensor_id =  int(input("enter sensor_id :"))
Moisture_level = float(input("enter Moisture_level: "))
Date_Time=datetime.fromisoformat(input("enetr date and time :"))

query = f"insert into agri_info values({sensor_id}, {Moisture_level}, '{Date_Time}');"

cursor = Connection.cursor()
cursor.execute(query)
Connection.commit()
cursor.close()
Connection.close()
