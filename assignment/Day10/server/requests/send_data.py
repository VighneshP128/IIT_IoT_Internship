import requests

url = "http://127.0.0.1:5000/Moisture"

data = {
    "sensor_id": 1,
    "Moisture_level": 25
}

response = requests.post(url, json=data)
print(response.text)