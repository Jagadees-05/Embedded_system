#include <WiFi.h>
#include <PubSubClient.h>
#include <ArduinoJson.h>
const char* ssid = "YOUR_SSID";
const char* password = "YOUR_PASSWORD";
const char* mqtt_server = "broker.emqx.io";
const int mqtt_port = 1883;
const char* mqtt_topic = "esp32/safety";
const int MQ2_PIN = 34; // Analog pin
const int THRESHOLD = 300; // Dangerous level
WiFiClient espClient;
PubSubClient client(espClient);
void setup_wifi() {
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);  }}
void reconnect() {
  while (!client.connected()) {
    client.connect("ESP32SafetyClient");  }}
void setup() {
  Serial.begin(115200);
  setup_wifi();
  client.setServer(mqtt_server, mqtt_port);
void loop() {
  if (!client.connected()) reconnect();
  client.loop();
  int gasLevel = analogRead(MQ2_PIN);
  String status = (gasLevel > THRESHOLD) ? "DANGEROUS" : "NORMAL";
  StaticJsonDocument<64> doc;
  doc["mq2"] = gasLevel;
  doc["status"] = status; 
  char buffer[64];
  serializeJson(doc, buffer);
  client.publish(mqtt_topic, buffer);
  Serial.print("Published: ");
  Serial.println(buffer);
  delay(3000);}
