import ppadb
from ppadb.client import Client
from PIL import Image
import numpy
import time

adb = Client(host='127.0.0.1', port=5555) #Stops on one of these two lines 
devices = adb.devices()

if len(devices) == 0:
    print("No device found")
    quit()

device = devices[0]

print("Connected...")