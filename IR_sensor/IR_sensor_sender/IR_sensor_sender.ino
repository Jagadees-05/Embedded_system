#include <WiFi.h>
#include <PubSubClient.h>
#include <ArduinoJson.h>
const char* ssid = "YOUR_SSID";
const char* password = "YOUR_PASSWORD";
const char* mqtt_server = "broker.emqx.io";
const int mqtt_port = 1883;
const char* mqtt_topic = "esp32/garage";
const int IR_SENSOR_PIN = 4;
WiFiClient espClient;
PubSubClient client(espClient);
void setup_wifi() {
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(500); }}
void reconnect() {
  while (!client.connected()) {
    client.connect("ESP32Client");  }}
void setup() {
  Serial.begin(115200);
  pinMode(IR_SENSOR_PIN, INPUT);
  setup_wifi();
  client.setServer(mqtt_server, mqtt_port);}
void loop() {
  if (!client.connected()) reconnect();
  client.loop();
  int irValue = digitalRead(IR_SENSOR_PIN);
  int garageStatus = (irValue == HIGH) ? 1 : 0;
  StaticJsonDocument<64> doc;
  doc["ir_status"] = garageStatus;
  doc["garage"] = garageStatus;
  char buffer[64];
  serializeJson(doc, buffer);
  client.publish(mqtt_topic, buffer);
  Serial.print("Published: ");
  Serial.println(buffer);
  delay(2000);}
