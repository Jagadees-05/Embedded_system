import json
import mysql.connector
from paho.mqtt.client import Client
from twilio.rest import Client as TwilioClient


# Twilio credentials
TWILIO_SID = 'Your_SID'
TWILIO_AUTH = 'Your_AUTH'
TWILIO_FROM = '+1234567890'
TWILIO_TO = '+91xxxxxxxxxx'
           twilio_client = TwilioClient(TWILIO_SID, TWILIO_AUTH)
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="iot_data")
cursor = db.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS garage_status (
    id INT AUTO_INCREMENT PRIMARY KEY,
    status INT,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP)
""")
+
def on_message(client, userdata, message):
    try:
        data = json.loads(message.payload.decode())
        status = data.get("garage", 0)
        print(f"Garage status: {status}")
              if status == 1:
            send_email_alert()
            twilio_client.messages.create(
                body="Garage status: OPEN",
                from_=TWILIO_FROM,
                to=TWILIO_TO          )
            print("SMS Sent!")
        cursor.execute("INSERT INTO garage_status (status) VALUES (%s)", (status,))
        db.commit()
    except Exception as e:
        print("Error:", e)
                 client = Client()
client.connect("broker.emqx.io", 1883, 60)
client.subscribe("esp32/garage")
client.on_message = on_message
      print("Listening for MQTT data...")
