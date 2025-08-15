#include <WiFi.h>
#include <PubSubClient.h>
#include <ArduinoJson.h>
const char* ssid = "Airel_9842878776";
const char* password = "air88581";
const char* mqtt_server = "broker.emqx.io";
const int mqtt_port = 1883;
const char* mqtt_topic = "agri/monitoring";
const int soilPin = 34;
const int rainPin = 35;
WiFiClient espClient;
PubSubClient client(espClient);
void setup_wifi() {
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");}
  Serial.println("\nWiFi connected");}
void reconnect() {
  while (!client.connected()) {
    if (client.connect("ESP32Client")) {
      Serial.println("MQTT Connected");
    } else {
      delay(2000);    }}}
void setup() {
  Serial.begin(115200);
  setup_wifi();
  client.setServer(mqtt_server, mqtt_port);
  pinMode(rainPin, INPUT);
}
void loop() {
  if (!client.connected()) reconnect();
  client.loop();
  int soilValue = analogRead(soilPin);  // 0 - 4095
  int soilPercent = map(soilValue, 4095, 0, 0, 100);
  bool rainDetected = digitalRead(rainPin) == HIGH;
  const char* rainStatus = rainDetected ? "Rain" : "Clear";
  const char* soilStatus = soilPercent < 30 ? "Dry" : "OK";
  StaticJsonDocument<128> doc;
  doc["soil"] = soilPercent;
  doc["rain"] = rainStatus;
  doc["soil_status"] = soilStatus;
  char buffer[128];
  serializeJson(doc, buffer);
  client.publish(mqtt_topic, buffer);
  Serial.println(buffer);
  delay(5000);}
