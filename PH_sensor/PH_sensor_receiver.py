import paho.mqtt.client as mqtt
import json
import mysql.connector
from datetime import datetime

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="ph_monitor"
)
cursor = db.cursor()
cursor.execute("""
    CREATE TABLE IF NOT EXISTS ph_data (
        id INT AUTO_INCREMENT PRIMARY KEY,
        ph FLOAT,
        timestamp DATETIME
    )
""")

def on_connect(client, userdata, flags, rc):
    client.subscribe("esp32/ph")

def on_message(client, userdata, msg):
    data = json.loads(msg.payload.decode())
    ph = data["pH"]
    timestamp = datetime.now()
    print(f"pH: {ph} at {timestamp}")
    cursor.execute("INSERT INTO ph_data (ph, timestamp) VALUES (%s, %s)", (ph, timestamp))
    db.commit()

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("broker.emqx.io", 1883, 60)
client.loop_forever()
