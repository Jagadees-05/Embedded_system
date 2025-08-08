#include <WiFi.h>
#include <PubSubClient.h>
#include <DHT.h>
#include <ArduinoJson.h>

#define DHTPIN 4
#define DHTTYPE DHT11
DHT dht(DHTPIN, DHTTYPE);
// WiFi credentials
const char* ssid = "your_SSID";
const char* password = "your_PASSWORD";
// MQTT
const char* mqtt_server = "broker.emqx.io";
const char* mqtt_topic = "esp32/dht11";
WiFiClient espClient;
PubSubClient client(espClient);
void setup_wifi() {
  delay(10);
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) delay(500);}
void reconnect() {
  while (!client.connected()) {
    if (client.connect("ESP32DHTClient")) break;
    delay(5000);  }}

void setup() {
  Serial.begin(115200);
  dht.begin();
  setup_wifi();
  client.setServer(mqtt_server, 1883);}
void loop() {
  if (!client.connected()) reconnect();
  client.loop();
  float h = dht.readHumidity();
  float t = dht.readTemperature();
  if (!isnan(h) && !isnan(t)) {
    StaticJsonDocument<200> doc;
    doc["temperature"] = t;
    doc["humidity"] = h;
    char buffer[256];
    serializeJson(doc, buffer);
    client.publish(mqtt_topic, buffer);
    Serial.print("Temp: ");
    Serial.print(t);
    Serial.print(" °C, Humidity: ");
    Serial.println(h);}
  delay(5000);}
