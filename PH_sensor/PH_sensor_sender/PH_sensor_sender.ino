#include <WiFi.h>
#include <PubSubClient.h>
#include <ArduinoJson.h>

const char* ssid = "your_SSID";
const char* password = "your_PASSWORD";
const char* mqtt_server = "broker.emqx.io";

WiFiClient espClient;
PubSubClient client(espClient);

#define PH_PIN 34

void setup_wifi() {
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) delay(500);
}

void reconnect() {
  while (!client.connected()) {
    client.connect("ESP32Client");
  }
}

void setup() {
  Serial.begin(115200);
  setup_wifi();
  client.setServer(mqtt_server, 1883);
  pinMode(PH_PIN, INPUT);
}

void loop() {
  if (!client.connected()) reconnect();
  client.loop();

  int analogValue = analogRead(PH_PIN);
  float voltage = analogValue * (3.3 / 4095.0);
  float pHValue = 3.5 * voltage;

  StaticJsonDocument<100> doc;
  doc["pH"] = pHValue;
  char buffer[100];
  serializeJson(doc, buffer);

  client.publish("esp32/ph", buffer);

  Serial.print("pH Value: ");
  Serial.println(pHValue);

  delay(5000);}
