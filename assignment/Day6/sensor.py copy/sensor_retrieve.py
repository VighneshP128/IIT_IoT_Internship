import mysql.connector


connection = mysql.connector.connect(
    host="127.0.0.1",
    port = 3306,
    user = "root",
    password = "root",
    database = "iot_data1",
    use_pure = True
)


query = "select * from sen_reading"

cursor = connection.cursor()

cursor.execute(query)

sen_reading = cursor.fetchall()

for sen_reading in sen_reading:
    print(sen_reading)
    
cursor.close()
connection.close()