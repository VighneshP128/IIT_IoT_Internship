from flask import Flask, request

from utils.executeQuery import executeQuery
from utils.executeSelectQuery import executeSelectQuery

server = Flask(__name__)

@server.get('/')
def homepage():
    return "<html><body><h1>This is home page</h1></body></html>"

@server.post('/home1')
def create_home1():
    light_status = request.form.get('light_status')
    fan_status = request.form.get('fan_status')
    temperature = request.form.get('temp')
    

    query = f"insert into agri_info values({light_status}, '{fan_status}', '{temperature}');"

    executeQuery(query=query)

    return "Home_Info is added successfully"

@server.get('/home1')
def retrieve_Home():
    query = "select * from Home;"

    data = executeSelectQuery(query=query)

    return f"Home : {data}"

@server.put('/home1')
def update_home1():
    light_status = request.form.get('light_status')
    temperature= request.form.get('fan_status')

    query = f"update Home SET temperature = '{temperature}' where light_status= '{light_status}';"

    executeQuery(query=query)

    return "temperature is updated successfully"


if __name__ == '_main_':
    server.run(host='0.0.0.0', port=4000, debug=True)