import serial
import time

# --- Configuration ---
# IMPORTANT: Replace with your ESP32's correct port!
SERIAL_PORT = 'COM3' 
BAUD_RATE = 9600

# Morse Code Timing Rules (seconds)
DOT_DURATION = 0.2
DASH_DURATION = DOT_DURATION * 3
INTRA_LETTER_GAP = DOT_DURATION  # Gap between dots and dashes in a letter
INTER_LETTER_GAP = DOT_DURATION * 3
WORD_GAP = DOT_DURATION * 7

# --- Morse Code Dictionary ---
MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ' ':'/' }

# --- Main Program ---

# Establish connection to the ESP32
try:
    esp32 = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1)
    time.sleep(2) # Wait for connection to establish
    print("ESP32 connected! Ready for Morse code.")
except serial.SerialException as e:
    print(f"Error: Could not open port {SERIAL_PORT}. {e}")
    exit()

def buzz(duration):
    """Sends ON signal, waits, then sends OFF signal."""
    esp32.write('1'.encode())
    time.sleep(duration)
    esp32.write('0'.encode())

def play_morse_code(message):
    """Iterates through a message and plays the Morse code for it."""
    for char in message.upper():
        if char in MORSE_CODE_DICT:
            pattern = MORSE_CODE_DICT[char]
            print(f"Playing: {char} -> {pattern}")
            
            if pattern == '/': # Handle space between words
                time.sleep(WORD_GAP)
                continue

            for symbol in pattern:
                if symbol == '.':
                    buzz(DOT_DURATION)
                elif symbol == '-':
                    buzz(DASH_DURATION)
                
                # Gap between dots/dashes within the same letter
                time.sleep(INTRA_LETTER_GAP)
            
            # Gap between letters
            time.sleep(INTER_LETTER_GAP)
        else:
            print(f"Ignoring unsupported character: '{char}'")

# --- Program Loop ---
try:
    while True:
        user_input = input("\nEnter a message to convert to Morse code (or type 'exit'): ")
        if user_input.lower() == 'exit':
            break
        play_morse_code(user_input)
        print("--- Transmission Complete ---")

finally:
    print("\nClosing port and exiting.")
    esp32.close()