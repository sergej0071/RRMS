#include <DHT.h>
#include <Adafruit_Sensor.h>
#include <Adafruit_BMP280.h>

#define BMP_SCK 13
#define BMP_MISO 12
#define BMP_MOSI 11 
#define BMP_CS 10
DHT dht(2, DHT11); 
Adafruit_BMP280 bme; // I2C


void setup() {
   dht.begin();
   Serial.begin(9600);

   if (!bme.begin(0x76)) {  
    Serial.println(F("Could not find a valid BMP280 sensor, check wiring!"));
    while (1);
  }
}

void loop() {  
   int endSignalTime = millis();

   float humidityDTH11 = dht.readHumidity();
   float temperatureDTH11 = dht.readTemperature();
   float temperatureBMP280 = bme.readTemperature();
   float pressureBMP280 = bme.readPressure();
   
   Serial.print(humidityDTH11); // %
   Serial.print("x");
   Serial.print(pressureBMP280); // PA
   Serial.print("x");
   if(temperatureBMP280 != 0)
    Serial.println(temperatureBMP280); // C0
   else
    Serial.println(temperatureDTH11); // C0

  int timeOfCode = millis() - endSignalTime; 
  delay(1000 - timeOfCode);
}
