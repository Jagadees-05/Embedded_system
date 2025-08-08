#include <Wire.h>
#include <BH1750.h>
#include <WiFi.h>
#include <PubSubClient.h>
#include <ArduinoJson.h>

const char* ssid = "YOUR_SSID";
const char* password = "YOUR_PASSWORD";
const char* mqtt_server = "broker.emqx.io";

WiFiClient espClient;
PubSubClient client(espClient);
BH1750 lightMeter;

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
  Wire.begin();
  lightMeter.begin();
  setup_wifi();
  client.setServer(mqtt_server, 1883);
}

void loop() {
  if (!client.connected()) reconnect();
  client.loop();

  float lux = lightMeter.readLightLevel();
  StaticJsonDocument<100> doc;
  doc["lux"] = lux;

  char buffer[100];
  serializeJson(doc, buffer);
  client.publish("esp32/light_sensor", buffer);

  delay(3000);}
