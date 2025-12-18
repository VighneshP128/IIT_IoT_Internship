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

sensor_id = int(input("Enter sensor_id  of a agri_info to be deleted : "))

query = f"delete from agri_info where sensor_id  = {sensor_id};"

cursor = Connection.cursor()
cursor.execute(query)
Connection.commit()