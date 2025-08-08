import json
import mysql.connector
from mysql.connector import errorcode
from paho.mqtt import client as mqtt_client

# MQTT Configuration
broker = 'broker.emqx.io'
port = 1883
topic = "mq2/sensor"
client_id = "mqtt_python_mq2_receiver"

# MySQL Configuration
mysql_config = {
    'host': 'localhost',
    'user': 'root',
    'password': ''  # Use password if you set one in XAMPP
}

# Connect to MySQL server (no DB yet)
db = mysql.connector.connect(
    host=mysql_config['host'],
    user=mysql_config['user'],
    password=mysql_config['password']
)
cursor = db.cursor()

# Step 1: Create Database
def create_database():
    try:
        cursor.execute("CREATE DATABASE IF NOT EXISTS mq2")
        print("Database 'mq2' checked/created.")
    except mysql.connector.Error as err:
        print(f" Database creation error: {err}")

# Step 2: Create Table
def create_table():
    cursor.execute("USE mq2")
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS mq2_sensor_data (
            id INT AUTO_INCREMENT PRIMARY KEY,
            mq2_value INT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    """)
    print(" Table 'mq2_sensor_data' checked/created.")

# Step 3: Insert Data
def insert_mq2_data(mq2_value):
    try:
        query = "INSERT INTO mq2_sensor_data (mq2_value) VALUES (%s)"
        cursor.execute(query, (mq2_value,))
        db.commit()
        print(f" Inserted: mq2_value = {mq2_value}")
    except mysql.connector.Error as err:
        print(f" Insert error: {err}")

# MQTT Callback
def on_message(client, userdata, msg):
    try:
        payload = msg.payload.decode()
        print(f" Received `{payload}` from `{msg.topic}`")

        data = json.loads(payload)
        mq2_value = data.get("mq2_value")

        if mq2_value is not None:
            insert_mq2_data(mq2_value)
        else:
            print("️ 'mq2_value' missing in payload.")

    except Exception as e:
        print(f" Error: {e}")

# Connect to MQTT Broker
def connect_mqtt():
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print(" Connected to MQTT Broker!")
            client.subscribe(topic)
        else:
            print(f" MQTT connection failed with code {rc}")

    client = mqtt_client.Client(client_id)
    client.on_connect = on_connect
    client.on_message = on_message

    client.connect(broker, port)
    return client

# Run everything
def run():
    create_database()
    create_table()

    mqtt_client_instance = connect_mqtt()
    mqtt_client_instance.loop_forever()

if __name__ == '__main__':
    run()
