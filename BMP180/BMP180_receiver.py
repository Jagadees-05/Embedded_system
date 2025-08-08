import paho.mqtt.client as mqtt
import mysql.connector
from datetime import datetime
from twilio.rest import Client

# MySQL Connection
conn = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="",
    database="practice"
)
cursor = conn.cursor()

# Twilio Setup
account_sid = 'AC7bc9090sjdhbcidiubw mw'
auth_token = '55bcd6f9eaefC KCCJWNC'
t_client = Client(account_sid, auth_token)

# MQTT Setup
broker = "broker.emqx.io"
port = 1883
topics = [("sensor/bmp180/temp", 0), ("sensor/bmp180/pres", 0), ("sensor/bmp180/alt", 0)]

# Temporary buffer
data_buffer = {"temp": None, "pres": None, "alt": None}

# MQTT Connect
def on_connect(client, userdata, flags, rc):
    print("Connected with code", rc)
    client.subscribe(topics)

# MQTT Message Handling
def on_message(client, userdata, msg):
    try:
        topic = msg.topic
        payload = msg.payload.decode()
        time_now = datetime.now()

        if "temp" in topic:
            data_buffer["temp"] = float(payload)
        elif "pres" in topic:
            data_buffer["pres"] = float(payload)
        elif "alt" in topic:
            data_buffer["alt"] = float(payload)

        # Once all data is received
        if all(value is not None for value in data_buffer.values()):
            temp = data_buffer["temp"]
            pres = data_buffer["pres"]
            alt = data_buffer["alt"]

            print(f"[{time_now}] Temp: {temp}°C, Pressure: {pres} hPa, Altitude: {alt} m")

            # Insert into database
            cursor.execute(
                "INSERT INTO bmp180_data (temperature, pressure, altitude, timestamp) VALUES (%s, %s, %s, %s)",
                (temp, pres, alt, time_now)
            )
            conn.commit()

            # Optional SMS Alert
            if temp > 30.0:
                message = t_client.messages.create(
                    body=f"Alert! High Temp: {temp}°C at {time_now.strftime('%H:%M:%S')}",
                    from_='+18065459166',
                    to='+91xxxxxxxxxx'
                )
                print(" SMS Sent! SID:", message.sid)

            # Clear buffer
            data_buffer["temp"] = None
            data_buffer["pres"] = None
            data_buffer["alt"] = None

    except Exception as e:
        print("Error:", e)

# MQTT Client Setup
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect(broker, port)
client.loop_forever()
