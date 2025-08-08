import paho.mqtt.client as mqtt
import mysql.connector
import json

# MQTT Configuration
MQTT_BROKER = "broker.emqx.io"
MQTT_PORT = 1883
MQTT_TOPIC = "esp32/light_sensor"

# MySQL Configuration
MYSQL_HOST = "localhost"
MYSQL_USER = "root"
MYSQL_PASSWORD = ""
MYSQL_DATABASE = "light_monitoring"
MYSQL_TABLE = "lux_data"

# Create database and table if they don't exist
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
            lux FLOAT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    """)
    connection.commit()
    cursor.close()
    connection.close()

# Callback when connected to MQTT
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to MQTT Broker")
        client.subscribe(MQTT_TOPIC)
    else:
        print(f"Failed to connect, return code {rc}")

# Callback when message is received
def on_message(client, userdata, msg):
    try:
        payload = json.loads(msg.payload.decode())
        lux = float(payload["lux"])
        print(f"Received -> Lux: {lux}")
        save_to_db(lux)
    except Exception as e:
        print(f"Error: {e}")

# Insert lux value into database
def save_to_db(lux):
    connection = mysql.connector.connect(
        host=MYSQL_HOST,
        user=MYSQL_USER,
        password=MYSQL_PASSWORD,
        database=MYSQL_DATABASE
    )
    cursor = connection.cursor()
    sql = f"INSERT INTO {MYSQL_TABLE} (lux) VALUES (%s)"
    cursor.execute(sql, (lux,))
    connection.commit()
    cursor.close()
    connection.close()

# Main execution
if __name__ == "__main__":
    init_db()

    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message

    client.connect(MQTT_BROKER, MQTT_PORT, 60)
    client.loop_forever()
