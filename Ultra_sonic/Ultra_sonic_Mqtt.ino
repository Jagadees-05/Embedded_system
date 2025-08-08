#include <ESP8266WiFi.h>
#include <PubSubClient.h>
#include <ArduinoJson.h>
             // WiFi credentials
const char* ssid = "Airel_9842878776";
const char* password = "air88581";
              // MQTT broker
const char* mqtt_server = "broker.emqx.io";
const int mqtt_port = 1883;
const char* mqtt_topic = "quantanics/ultrasonic";
            // Ultrasonic Sensor Pins
const int TRIG_PIN = D1;   // GPIO5
const int ECHO_PIN = D2;   // GPIO4
            const float BIN_HEIGHT_CM = 22.0; // Max height of the dustbin (empty)
WiFiClient espClient;
PubSubClient client(espClient);
             void setup_wifi() {
  Serial.print("Connecting to WiFi: ");
  Serial.println(ssid);
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");  }
  Serial.println("\nWiFi connected");
  Serial.print("IP Address: ");
  Serial.println(WiFi.localIP());}
  void reconnect() {
  while (!client.connected()) {
    Serial.print("Connecting to MQTT...");
    if (client.connect("ESP8266Client")) {
      Serial.println("connected");
    } else {
      Serial.print("failed, rc=");
      Serial.println(client.state());
      delay(2000);}
  }}float readDistanceCM() {
  digitalWrite(TRIG_PIN, LOW);
  delayMicroseconds(2);
  digitalWrite(TRIG_PIN, HIGH);
  delayMicroseconds(10);
  digitalWrite(TRIG_PIN, LOW);
               long duration = pulseIn(ECHO_PIN, HIGH, 30000); // Timeout in 30ms
  float distance = duration * 0.0343 / 2;
  return distance;
}void setup() {
  Serial.begin(115200);
  pinMode(TRIG_PIN, OUTPUT);
  pinMode(ECHO_PIN, INPUT);
              setup_wifi();
  client.setServer(mqtt_server, mqtt_port);
}void loop() {
  if (!client.connected()) {
    reconnect();  }
  client.loop();
 float distance = readDistanceCM();
  float filledPercent = ((BIN_HEIGHT_CM - distance) / BIN_HEIGHT_CM) * 100;
  if (filledPercent < 0) filledPercent = 0;
  if (filledPercent > 100) filledPercent = 100;
              // Determine status
  const char* status = (distance <= 2.0) ? "FULL" : "OK"; // Alert if distance is less than or equal to 2 cm
             // Prepare JSON message
  StaticJsonDocument<128> doc;
  doc["distance"] = distance;
  doc["filled"] = filledPercent;
  doc["status"] = status;
  char buffer[128];
  serializeJson(doc, buffer);
    // Publish to MQTT
  client.publish(mqtt_topic, buffer);
  // Print to Serial
  Serial.print("Published: ");
  Serial.println(buffer);
delay(3000); // 3 seconds between reads
}
