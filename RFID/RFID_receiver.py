import json
import mysql.connector
from paho.mqtt import client as mqtt_client

# MQTT Configuration
broker = 'broker.emqx.io'
port = 1883
topic = "rfid/inout"
client_id = "rfid_mqtt_receiver"

# MySQL Configuration
mysql_config = {
    'host': 'localhost',
    'user': 'root',
    'password': '',  # leave blank if no password
    'database': 'rfid'
}

# Connect to MySQL and create table if not exists
def init_db():
    conn = mysql.connector.connect(**mysql_config)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS attendance (
            name VARCHAR(50),
            uid VARCHAR(20),
            in_time DATETIME,
            out_time DATETIME
        )
    """)
    conn.commit()
    return conn

conn = init_db()
cursor = conn.cursor()

# Callback when message is received
def on_message(client, userdata, msg):
    try:
        data = json.loads(msg.payload.decode())
        name = data['name']
        uid = data['uid']
        in_time = data['in_time']
        out_time = data['out_time']

        print(f"Received: {name} | UID: {uid} | In: {in_time} | Out: {out_time}")

        query = "INSERT INTO attendance (name, uid, in_time, out_time) VALUES (%s, %s, %s, %s)"
        values = (name, uid, in_time, out_time)
        cursor.execute(query, values)
        conn.commit()

    except Exception as e:
        print("Error:", e)

# MQTT connection and subscription
def connect_mqtt():
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker.")
            client.subscribe(topic)
        else:
            print("Failed to connect, return code:", rc)

    client = mqtt_client.Client(client_id)
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect(broker, port)
    return client

# Main loop
if __name__ == '__main__':
    mqtt_client = connect_mqtt()
    mqtt_client.loop_forever()
