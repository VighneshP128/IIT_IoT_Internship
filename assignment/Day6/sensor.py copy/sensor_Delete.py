import mysql.connector

connection = mysql.connector.connect(
    host = "127.0.0.1",
    port = 3306,
    user = "root",
    password = "root",
    database = "iot_data1",
    use_pure = True
)
sen_id = int(input("Enter id to be deleted : "))

query = f"delete from sen_reading where sen_id = {sen_id};"

cursor = connection.cursor()
cursor.execute(query)
connection.commit()
cursor.close()
connection.close()