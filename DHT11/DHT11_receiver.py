import paho.mqtt.client as mqtt
import mysql.connector
import json

# MQTT Configuration
MQTT_BROKER = "broker.emqx.io"
MQTT_PORT = 1883
MQTT_TOPIC = "dht11/data"

# MySQL Configuration
MYSQL_HOST = "localhost"
MYSQL_USER = "root"
MYSQL_PASSWORD = ""
MYSQL_DATABASE = "dht11_monitoring"
MYSQL_TABLE = "environment_data"

# Create database and table if not exists
def init_db():
    connection = mysql.connector.connect(
        host=MYSQL_HOST,
        user=MYSQL_USER,
        password=MYSQL_PASSWORD
    )
    cursor = connection.cursor()
    cursor.execute(f"CREATE DATABASE IF NOT EXISTS {MYSQL_DATABASE}")
    connection.database = MYSQL_DATABASE
    cursor.execute(f"""
        CREATE TABLE IF NOT EXISTS {MYSQL_TABLE} (
            id INT AUTO_INCREMENT PRIMARY KEY,
            temperature FLOAT,
            humidity FLOAT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    """)
    connection.commit()
    cursor.close()
    connection.close()

# MQTT Callbacks
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to MQTT Broker")
        client.subscribe(MQTT_TOPIC)
    else:
        print(f"Failed to connect, return code {rc}")

def on_message(client, userdata, msg):
    try:
        payload = json.loads(msg.payload.decode())
        temperature = float(payload["temperature"])
        humidity = float(payload["humidity"])
        print(f"Received -> Temp: {temperature} °C, Humidity: {humidity} %")
        save_to_db(temperature, humidity)
    except Exception as e:
        print(f"Error: {e}")

# Save to MySQL
def save_to_db(temp, hum):
    connection = mysql.connector.connect(
        host=MYSQL_HOST,
        user=MYSQL_USER,
        password=MYSQL_PASSWORD,
        database=MYSQL_DATABASE
    )
    cursor = connection.cursor()
    sql = f"INSERT INTO {MYSQL_TABLE} (temperature, humidity) VALUES (%s, %s)"
    cursor.execute(sql, (temp, hum))
    connection.commit()
    cursor.close()
    connection.close()

# Run
if __name__ == "__main__":
    init_db()

    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message

    client.connect(MQTT_BROKER, MQTT_PORT, 60)
    client.loop_forever()
