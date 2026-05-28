PROJECT IDEA

To create a temperature and humidity monitor for an instrument case, get alerts when conditions are not optimal for wood health of the instrument and also have a live monitor of the data.

WHAT THE PROJECT IS

Using a raspberry pi 4b and a sensehat, the sensehat will not only display the temperature and humidity in real time but the raspberry pi will also send the data to Thingspeak. The data received will be displayed and alerts are sent when the instrument gets too hot or too cold and/or if the humidity is too high or too low.

INSTALL INSTRUCTIONS

YOU WILL NEED:

Raspberry Pi (I used a Raspberry Pi 4)
SD Card
Sensehat
MathWorks account (for Thingspeak)
Internet Connection
Python (I used vscode and had python installed)


The following will need to be installed:

-raspberrypi os

-sys

-time

-requests

-logging

-from urllib.parse import urlparse

-paho.mqtt.client as mqtt

-sensehat


Create a python environment (I called mine instrumentenv)


Enter your personal details (Thingspeak Keys, email, password etc.) and copy the code over to your pi.


To run the programme enter: python3 InstrumentMonitor.py mqtt://mqtt.3thingspeak.com:1883


REFERENCES

https://projects.raspberrypi.org/en/projects/getting-started-with-the-sense-hat/7


https://stringsmagazine.com/6-ways-to-protect-your-instrument-from-damaging-winter-chill/#:~:text=Winterizing%20your%20fiddle%20will%20stabilize,protect%20it%20from%20winter's%20chill.&text=Stringed%20instruments%20are%20happiest%20given,of%2035%20to%2050%20percent.


https://www.thestrad.com/lutherie/ask-the-experts-protecting-your-instrument-in-hot-and-humid-temperatures/535.article


https://www.mathworks.com/help/thingspeak/analyze-channel-data-to-send-email.html


https://www.mathworks.com/help/thingspeak/sendalert.html


https://pypi.org/project/paho-mqtt/

