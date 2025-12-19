from flask import Flask, request

from utils.executeQuery import executeQuery
from utils.executeSelectQuery import executeSelectQuery

server = Flask(__name__)

@server.get('/')
def homepage():
    return "<html><body><h1>This is home page</h1></body></html>"

@server.post('/sensor')
def create_sensor():
    id = request.form.get('id')
    temp = request.form.get('temp')
    humidity = request.form.get('humidity')
    timestamp = request.form.get('timestamp')

    query = f"insert into sen_read values({id}, '{temp}', '{humidity}', '{timestamp}');"

    executeQuery(query=query)

    return "sen_read is added successfully"

@server.get('/sensor')
def retrieve_sen_read():
    query = "select * from sen_read;"

    data = executeSelectQuery(query=query)

    return f"sen_read : {data}"

@server.put('/sensor')
def update_sensor():
    id = request.form.get('id')
    temp = request.form.get('temp')

    query = f"update sen_read SET email = '{temp}' where name = '{id}';"

    executeQuery(query=query)

    return "temperature is updated successfully"

@server.delete('/sensor')
def delete_sensor():
    id = request.form.get('id')

    query = f"delete from sen_read where name = '{id}';"

    executeQuery(query=query)

    return " id is deleted successfully"

if __name__ == '_main_':
    server.run(host='0.0.0.0', port=4000, debug=True)