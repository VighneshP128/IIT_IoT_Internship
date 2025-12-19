from flask import Flask, request
from createCustomResponse import createCustomResponse
from utils.executeQuery import executeQuery
from utils.executeSelectQuery import executeSelectQuery

app = Flask(__name__)

@app.route('/', methods=['GET'])
def homepage():
    return "<html><body><h1>Smart Home Monitoring System</h1></body></html>"


@app.route('/update', methods=['POST'])
def update_home_status():
    light_status = request.get_json().get('light_status')
    fan_status = request.get_json().get('fan_status')
    temperature = request.get_json().get('temperature')

    query = f"""
    insert into home_status (light_status, fan_status, temperature, reading_time)
    values ('{light_status}', '{fan_status}', {temperature}, NOW());
    """
    executeQuery(query)

    msg = "Home status updated successfully"
    return createCustomResponse(msg, error=False)


@app.route('/status', methods=['GET'])
def get_home_status():
    query = """
    select light_status, fan_status, temperature
    from home_status;
    """
    data = executeSelectQuery(query)

    msg = f"Current Home Status: {data}"
    return createCustomResponse(msg, error=False)


if __name__ == '_main_':
    app.run(host='0.0.0.0', port=4000, debug=True)