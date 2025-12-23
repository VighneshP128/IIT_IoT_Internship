from flask import Flask, request, jsonify
import mysql.connector
from datetime import datetime
import paho.mqtt.client as mqtt

app = Flask(__name__)


db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="smart_agri_iot1"
)
cursor = db.cursor()


MQTT_BROKER = "broker.hivemq.com"
MQTT_PORT = 1883
MQTT_TOPIC = "alert/moisture"
THRESHOLD = 30

mqtt_client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
mqtt_client.connect(MQTT_BROKER, MQTT_PORT, 1883)
mqtt_client.loop_start()

print(" MQTT Connected")


@app.route('/moisture', methods=['POST'])
def store_moisture():
    print(" Request received")

    data = request.get_json()
    print("📦 JSON Data:", data)

    if not data:
        return jsonify({"error": "No JSON received"}), 400

    sensor_id = data.get("sensor_id")
    Moisture_level = data.get("Moisture_level")

    if sensor_id is None or Moisture_level is None:
        return jsonify({"error": "Invalid data"}), 400

    now = datetime.now()

    cursor.execute(
        "INSERT INTO agri_info (sensor_id, Moisture_level, date_time) VALUES (%s,%s,%s)",
        (sensor_id, Moisture_level, now)
    )
    db.commit()

    print(f"Data stored → Sensor:{sensor_id}, Moisture:{Moisture_level}")

    if float(Moisture_level) < THRESHOLD:
        alert = f"ALERT! Sensor {sensor_id}: Moisture Low ({Moisture_level})"
        mqtt_client.publish(MQTT_TOPIC, alert)
        print(" Alert sent via MQTT")

    return jsonify({"status": "success"})

if __name__ == '_main_':
    print(" Flask Server Started")
    app.run(debug=True)