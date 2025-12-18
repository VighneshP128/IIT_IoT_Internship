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

sensor_id = int(input("Enter sensor_id  whose moisture to be updated : "))
Moisture_level= float(input("Enter new moisture : "))

query = f"update agri_info SET Moisture_level = {Moisture_level} where sensor_id = {sensor_id};"

cursor = Connection.cursor()
cursor.execute(query)
Connection.commit()
cursor.close()
Connection.close()