#imports and installs
import time
import adafruit_dht
from sense_hat import SenseHat
sense=SenseHat()


#THINGSPEAK INFO - TO BE INCLUDED LATER
#THINGSPEAK_API_KEY = 'V2NZHXW8GI9T6ZKX'
#TO_EMAIL = 'doireannocarroll1998@gmail.com'

#Colours for SenseHat
BLUE = (0, 0, 255)
RED = (255, 0, 0)

#Temperature and Humidity Readings for Instruments - SensorData
def get_environmental_data():
    # Read sensor data
    temp = sense.get_temperature()
    humidity = sense.get_humidity()
    
    return temp, humidity


while True:
    # Get readings
    temp, humidity= get_environmental_data()
    
    # Print to command line
    print("Temp: {:.1f} C  Humidity: {:.1f}%".format(
        temp, humidity))
    
    # Display on LED matrix (one after the other)
    sense.show_message("T:{:.1f}C".format(temp), text_colour=RED)
    sense.show_message("H:{:.1f}%".format(humidity), text_colour=BLUE)
    
    # 2 second delay before next reading
    time.sleep(2)



#TO BE USED LATER
#Temp_Min = 15
#Temp_Max = 22

#Humidity_Min = 35
#Humidity_Max = 50
