#include <WiFi.h>
#include <PubSubClient.h>
#include <SPI.h>
#include <MFRC522.h>
#include <ArduinoJson.h>

#define SS_PIN 21
#define RST_PIN 22
MFRC522 rfid(SS_PIN, RST_PIN);

const char* ssid = "your_SSID";
const char* password = "your_PASSWORD";

const char* mqtt_server = "broker.emqx.io";
const char* topic = "rfid/attendance";

WiFiClient espClient;
PubSubClient client(espClient);

void setup() {
  Serial.begin(115200);
  SPI.begin(); 
  rfid.PCD_Init();
  WiFi.begin(ssid, password);

  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }

  client.setServer(mqtt_server, 1883);
}

void loop() {
  if (!client.connected()) {
    while (!client.connected()) {
      client.connect("ESP32Client");
    }
  }

  client.loop();

  if (rfid.PICC_IsNewCardPresent() && rfid.PICC_ReadCardSerial()) {in
    String uid = "";
    for (byte i = 0; i < rfid.uid.size; i++) {
      uid += String(rfid.uid.uidByte[i], HEX);
    }

    DynamicJsonDocument doc(256);
    doc["rfid_uid"] = uid;
    doc["timestamp"] = millis();

    char buffer[256];
    serializeJson(doc, buffer);
    client.publish(topic, buffer);

    Serial.println(buffer);
    delay(2000);
  }
}
