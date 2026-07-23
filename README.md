# text-to-morse-code-using-buzzer-
ESP32 Text-to-Morse Code Buzzer 🔊
A simple and fun project that converts text from your computer into audible Morse code using an ESP32 and an active buzzer.

This project uses a Python script to handle the text-to-Morse conversion and sends basic ON/OFF signals to the ESP32, which then drives the buzzer.

## What You'll Need
### Hardware
1 x ESP32 Development Board

1 x Active Buzzer (the kind that beeps when you just give it power)

2 x Jumper Wires

1 x Micro-USB Cable

### Software
Python 3.x

VS Code  with PlatformIO (with ESP32 board support installed)

The pyserial Python library

## Setup Guide
Getting this running is a 3-step process: wire it, flash it, run it.

### Step 1: Wire the Hardware
The wiring is super simple.

Connect the buzzer's positive (+) leg to GPIO 25 on the ESP32.

Connect the buzzer's negative (-) leg to a GND (Ground) pin on the ESP32.

### Step 2: Flash the ESP32
Open the buzzer_controller file in the PlatformIO. Select your ESP32 board and the correct port, then upload the sketch. This code instructs the ESP32 on how to receive commands from your computer.

### Step 3: Set Up the Python Script
The script morse_translator.py is the "brain" of the operation and runs on your computer.

Install the required library: Open your terminal or command prompt and run this command:


pip install pyserial

Configure the Port: Open the morse_translator.py file in a text editor. Find the SERIAL_PORT variable at the top and change its value (e.g., 'COM3') to match the port your ESP32 is connected to.

