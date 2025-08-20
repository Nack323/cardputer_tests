import time
import network
from lib.hydra.config import Config
from lib.display import Display

nic = network.WLAN(network.STA_IF)
config = Config()


def connect_wifi():
    """Connect to the configured WiFi network."""
    print("Enabling wifi...")

    if not nic.active():
        nic.active(True)

    if not nic.isconnected():
        # tell wifi to connect (with FORCE)
        while True:
            try:  # keep trying until connect command works
                nic.connect(config['wifi_ssid'], config['wifi_pass'])
                break
            except OSError as e:
                print(f"Error: {e}")
                time.sleep_ms(500)

        # now wait until connected
        attempts = 0
        while not nic.isconnected():
            print(f"connecting... {attempts}")
            time.sleep_ms(500)
            attempts += 1

    print("Connected!")

connect_wifi()

import requests

# Make a request to meowfacts
response = requests.get("https://raw.githubusercontent.com/Nack323/cardputer_tests/refs/heads/main/test1.py")
# Verify that the request worked
if response.status_code != 200:
    raise ValueError(f"Server returned {response.status_code}.\n{response.reason}")

# Decode the returned JSON data, and extract the random fact
script = response.content.decode('utf-8')

with open('./apps/mynewscript.py', 'w') as file:
    file.write(script)

# Draw text to the framebuffer, then write the frambuffer to the display:
quit()
