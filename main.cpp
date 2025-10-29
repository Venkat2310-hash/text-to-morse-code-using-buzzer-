#include <Arduino.h>

const int buzzerPin = 25; // The GPIO pin your active buzzer is on.

void setup() {
  // Set the buzzer pin as a digital output.
  pinMode(buzzerPin, OUTPUT);
  
  // Start serial communication.
  Serial.begin(9600);
}

void loop() {
  if (Serial.available() > 0) {
    char command = Serial.read();

    if (command == '1') {
      digitalWrite(buzzerPin, HIGH); // Turn the buzzer ON
    }
    else if (command == '0') {
      digitalWrite(buzzerPin, LOW);  // Turn the buzzer OFF
    }
  }
}