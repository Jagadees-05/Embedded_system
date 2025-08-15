import paho.mqtt.client as mqtt
import mysql.connector
import json

# MQTT Configuration
MQTT_BROKER = "broker.emqx.io"
MQTT_PORT = 1883
MQTT_TOPIC = "agri/monitoring"

# MySQL Configuration
MYSQL_HOST = "localhost"
MYSQL_USER = "root"
MYSQL_PASSWORD = ""
MYSQL_DATABASE = "agriculture"
MYSQL_TABLE = "sensor_data"

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
            soil INT,
            rain INT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    """)
    connection.commit()
    cursor.close()
    connection.close()

# Callback when connected to MQTT broker
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to MQTT Broker")
        client.subscribe(MQTT_TOPIC)
    else:
        print(f"Failed to connect, return code {rc}")

# Callback when a message is received
def on_message(client, userdata, msg):
    try:
        payload = json.loads(msg.payload.decode())
        soil = int(payload["soil"])
        rain = int(payload["rain"])
        print(f"Received -> Soil: {soil}, Rain: {rain}")
        save_to_db(soil, rain)
    except Exception as e:
        print(f"Error: {e}")

# Save data to MySQL
def save_to_db(soil, rain):
    connection = mysql.connector.connect(
        host=MYSQL_HOST,
        user=MYSQL_USER,
        password=MYSQL_PASSWORD,
        database=MYSQL_DATABASE
    )
    cursor = connection.cursor()
    sql = f"INSERT INTO {MYSQL_TABLE} (soil, rain) VALUES (%s, %s)"
    cursor.execute(sql, (soil, rain))
    connection.commit()
    cursor.close()
    connection.close()

# Initialize DB and start MQTT client
if __name__ == "__main__":
    init_db()

    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message

    client.connect(MQTT_BROKER, MQTT_PORT, 60)
    client.loop_forever()
