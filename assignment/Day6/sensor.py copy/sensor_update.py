import mysql.connector


connection = mysql.connector.connect(
    host = "127.0.0.1",
    port = 3306,
    user = "root",
    password = "root",
    database = "iot_data1",
    use_pure = True
)

temperature = input("Enter Temperature: ")
humidity = input("Enter humidity: ")

query = f"update sen_reading SET temperature= '{temperature}' where humidity = '{humidity}';"

cursor = connection.cursor()
cursor.execute(query)
connection.commit()
cursor.close()
connection.close()