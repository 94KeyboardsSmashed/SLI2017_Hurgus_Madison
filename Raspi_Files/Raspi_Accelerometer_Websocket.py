# -*- coding: utf-8 -*-
"""
Created on Sun Sep 24 18:46:19 2017

@author: Hyun-seok with help from Benton

A program for initiating the Websocket and reading it out via bluetooth to another computer
Requires ADXL345 and pybluez(bluetooth) libraries, and pulsing, neopixel, ADXL345_Read, NeopixelColorGradient.py files.

Details are still missing, do you know anything Ben? As such this will not be as heavily commented
"""

import adxl345
import time
from pulsing import *
from neopixel import *
from Raspi_Accelerometer_Readout import *
from NeoPixelColorGradient import *
from sys import stdout
import bluetooth

def TotalPer(values, averages, accelerometerIn, denom=4, smoothness=5):
   #Returns a float of the average divided by the denominator (default 4) in a percentage value. 
   #Read ADXL_345_Read.py file for more information
   difference = readAccelerometerMagnitude(accelerometerIn, values)
   average = readAverages(difference, averages, smoothness)
   percentage = (average/denom)*100
   return percentage

"""
serverMACAddress = 'B8:27:EB:BF:91:27'
port = 3
s = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
s.connect((serverMACAddress, port))
while 1:
   s.send(perX, perY, perZ)
sock.close()
"""

if __name__ == "__main__":
   accel = adxl345.ADXL345()

   valuesX = []
   averagesX = []
   valuesY = []
   averagesY = []

   valuesZ = []
   averagesZ = []

   while True:

       perX = TotalPer(valuesX, averagesX, readAccelerometerX(accel, True))
       perY = TotalPer(valuesY, averagesY, readAccelerometerY(accel, True))
       perZ = TotalPer(valuesZ, averagesZ, readAccelerometerZ(accel, True))

       serverMACAddress = 'B8:27:EB:BF:91:27' #MAC address of raspi
       port = 1234
       s = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
       s.connect((serverMACAddress, port))
       while 1:
           s.send(perX, perY, perZ)
       sock.close()

