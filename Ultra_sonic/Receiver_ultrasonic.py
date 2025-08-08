import json
import mysql.connector
from paho.mqtt.client import Client
from twilio.rest import Client as TwilioClient

# Twilio Credentials
TWILIO_SID = 'YOUR_SID'
TWILIO_AUTH = 'YOUR_AUTH_TOKEN'
TWILIO_FROM = '+18507473974'
TWILIO_TO = '+91xxxxxxxxxxx'
twilio_client = TwilioClient(TWILIO_SID, TWILIO_AUTH)
# Create DB and Table if not exist
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password=""
)
cursor = db.cursor()
cursor.execute("CREATE DATABASE IF NOT EXISTS dustbin")
cursor.execute("USE dustbin")
cursor.execute("""
    CREATE TABLE IF NOT EXISTS dustbin_data (
        distance FLOAT,
        filled FLOAT,
        timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
""")
# MQTT callback
def on_message(client, userdata, message):
    try:
        data = json.loads(message.payload.decode())
        distance = data.get("distance", 0)
        filled = data.get("filled", 0)
        print(f" Distance: {distance:.2f} cm |  Filled: {filled:.2f}%"
        if filled >= 50:
            twilio_client.messages.create(
                body=f"Alert: Dustbin is {filled:.2f}% full!",
                from_=TWILIO_FROM,
                to=TWILIO_TO
            )
            print(" SMS Alert Sent!")
         query = "INSERT INTO dustbin_data (distance, filled) VALUES (%s, %s)"
        cursor.execute(query, (distance, filled))
        db.commit()
    except Exception as e:
        print(" Error:", e)
# MQTT setup
client = Client()
client.connect("broker.emqx.io", 1883, 60)
client.subscribe("quantanics/ultrasonic")
client.on_message = on_message
print(" Listening for MQTT data...")
client.loop_forever()
