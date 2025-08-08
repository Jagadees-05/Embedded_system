import json
import mysql.connector
from mysql.connector import errorcode
from paho.mqtt import client as mqtt_client

# MQTT Configuration
broker = 'broker.emqx.io'
port = 1883
topic = "ldr/sensor"
client_id = "mqtt_python_ldr_receiver"

# MySQL Configuration
mysql_config = {
    'host': 'localhost',
    'user': 'root',
    'password': ''  # Set password if you have one
}

# Initialize DB connection (without database for creation)
db = mysql.connector.connect(
    host=mysql_config['host'],
    user=mysql_config['user'],
    password=mysql_config['password']
)
cursor = db.cursor()

# Step 1: Create Database if not exists
def create_database():
    try:
        cursor.execute("CREATE DATABASE IF NOT EXISTS ldr")
        print("Database 'ldr' checked/created.")
    except mysql.connector.Error as err:
        print(f"Database creation error: {err}")

# Step 2: Create Table if not exists
def create_table():
    cursor.execute("USE ldr")
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS ldr_sensor_data (
            ldr_value INT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    """)
    print(" Table 'ldr_sensor_data' checked/created.")

# Step 3: Insert Data into Table
def insert_ldr_data(ldr_value):
    try:
        query = "INSERT INTO ldr_sensor_data (ldr_value) VALUES (%s)"
        cursor.execute(query, (ldr_value,))
        db.commit()
        print(f" Inserted: ldr_value = {ldr_value}")
    except mysql.connector.Error as err:
        print(f"Insert error: {err}")

# MQTT Callback
def on_message(client, userdata, msg):
    try:
        payload = msg.payload.decode()
        print(f"Received `{payload}` from `{msg.topic}`")

        data = json.loads(payload)
        ldr_value = data.get("ldr_value")

        if ldr_value is not None:
            insert_ldr_data(ldr_value)
        else:
            print("️ 'ldr_value' missing in payload.")

    except Exception as e:
        print(f"️ Error: {e}")

# MQTT Connection
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
