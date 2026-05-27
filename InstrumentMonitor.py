#imports and installs
import os
import sys
import time
import requests
import board
import logging
from urllib.parse import urlparse
import paho.mqtt.client as mqtt


#Sensehat Setup
from sense_hat import SenseHat
sense=SenseHat()


#Thingspeak Info
THINGSPEAK_API_KEY = 'API KEY'
EMAIL_ADDRESS = "EMAIL@EMAIL.COM"
EMAIL_Password = "PASSWORD"
TO_EMAIL = 'EMAIL@EMAIL.COM'

# ThingSpeak settings
THINGSPEAK_WRITE_API_KEY = os.getenv("TS_WRITE_KEY", "WRITE KEY")
THINGSPEAK_CHANNEL_URL = "https://api.thingspeak.com/update"

ALERT_API_KEY = "ALERTAPIKEY"

# configure Logging
logging.basicConfig(level=logging.INFO)

# Initialise SenseHAT
sense = SenseHat()
sense.clear()

# MQTT Config
USERNAME = os.getenv("THINGSPEAK_USERNAME")
CLIENT_ID = os.getenv("THINGSPEAK_CLIENT_ID")
PASSWORD = os.getenv("THINGSPEAK_PASSWORD")
CHANNEL_ID = os.getenv("THINGSPEAK_CHANNEL_ID")
TRANSMISSION_INTERVAL = int(os.getenv("TRANSMISSION_INTERVAL", "15"))


def on_connect(client, userdata, flags, rc):
    logging.info("Connection Result: %s", rc)

def on_publish(client, obj, mid):
    logging.info("Message Sent ID: %s", mid)

mqttc = mqtt.Client(client_id=CLIENT_ID)
mqttc.on_connect = on_connect
mqttc.on_publish = on_publish

url_str = sys.argv[1]
url = urlparse(url_str)

mqttc.username_pw_set(USERNAME, PASSWORD)

# Connect to MQTT Broker
mqttc.connect(url.hostname, url.port)
mqttc.loop_start()

# Set Thingspeak Channel to publish
topic = f"channels/{3386369}/publish"

# Send data to ThingSpeak
def send_to_thingspeak(case_humidity,case_temperature):
    payload = {
        'api_key': 'API KEY',
        'field1': case_humidity,
        'field2': case_temperature
    }
  
    response = requests.get(THINGSPEAK_CHANNEL_URL, params=payload)

    if response.status_code == 200:
        print("Data sent to ThingSpeak.")
    else:
        print(f"Failed to send data. Status code: {response.status_code}")
def send_alert(temperature,humidity):

    alert_url = "https://api.thingspeak.com/alerts/send"
    headers = {"ThingSpeak-Alerts-API-Key": ALERT_API_KEY,
        "Content-Type": "application/json"}
    message = {
            "subject": "Instrument Warning",
            "body": (
                f"Temperature: {temperature:.1f}C\n"
                f"Humidity: {humidity:.1f}%"  
            )
        }
    response = requests.post(
        alert_url,
        json=message,
        headers=headers
    )
    if response.status_code == 200:
        print ("Alert sent")
    else:
         print("Alert failed")

   

#Minimum and Maximum
Temp_Min = 15
Temp_Max = 22

Humidity_Min = 35
Humidity_Max = 50

#Colours for SenseHat
BLUE = (0, 0, 255)
RED = (255, 0, 0)

while True:
    try:
        case_temperature = sense.get_temperature()
        case_humidity = sense.get_humidity()

        print(
            f"Case Temp: {case_temperature:.1f} C | "
            f"Case Humidity: {case_humidity:.1f}%")

        sense.show_message("T:{:.1f}C".format(room_temperature), text_colour=RED)
        sense.show_message("H:{:.1f}%".format(room_humidity), text_colour=BLUE)
        send_to_thingspeak(case_temperature,case_humidity)
        if (case_temperature_c < Temp_Min or
            case_temperature_c > Temp_Max or
            case_humidity < Humidity_Min or
            case_humidity > Humidity_Max):
            send_alert(
                viola_temperature_c,
                viola_humidity
        )
        time.sleep(15)
    except KeyboardInterrupt:
        logging.info("Interrupted")
        break
    except Exception as e:
        logging.exception("Error: %s", e)
        time.sleep(2)