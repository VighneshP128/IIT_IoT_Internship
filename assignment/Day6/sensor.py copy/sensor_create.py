import mysql.connector

conn = mysql.connector.connect(
    host="127.0.0.1",
    port=3306,
    user="root",
    password="root",
    database="iot_data1",
    use_pure=True
)
sen_id=int(input("Enter sensor id="))
temperature=int(input("Enter Temperature="))
humidity=int(input("Enter Humidity="))
timestamp=(input("Enter timestamp="))

query = f"insert into sen_reading values({sen_id}, {temperature}, {humidity},'{timestamp}');"

cursor = conn.cursor()
cursor.execute(query)
conn.commit()
cursor.close()
conn.close()
