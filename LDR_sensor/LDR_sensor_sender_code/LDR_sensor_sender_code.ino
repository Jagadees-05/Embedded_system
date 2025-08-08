#include <WiFi.h>
#include <PubSubClient.h>
#include <ArduinoJson.h>
const char* ssid = "YOUR_SSID";
const char* password = "YOUR_PASSWORD";
const char* mqtt_server = "broker.emqx.io";
const int mqtt_port = 1883;
const char* mqtt_topic = "esp32/billboard";
const int LDR_PIN = 34;  // Analog pin for LDR
const int THRESHOLD = 1000;
WiFiClient espClient;
PubSubClient client(espClient);
void setup_wifi() {
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);  }}
void reconnect() {
  while (!client.connected()) {
    client.connect("ESP32BillboardClient");  }}
void setup() {
  Serial.begin(115200);
  setup_wifi();
  client.setServer(mqtt_server, mqtt_port);
}void loop() {
  if (!client.connected()) reconnect();
  client.loop();
  int ldrValue = analogRead(LDR_PIN);
  String status = (ldrValue <= THRESHOLD) ? "ON" : "OFF";
  StaticJsonDocument<64> doc;
  doc["ldr"] = ldrValue;
  doc["status"] = status;  
  char buffer[64];
  serializeJson(doc, buffer);
  client.publish(mqtt_topic, buffer);
  Serial.print("Published: ");
  Serial.println(buffer);
  delay(3000);}
