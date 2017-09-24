# -*- coding: utf-8 -*-
"""
Created on Sun Sep 24 17:45:21 2017

@author: Hyun-seok with help from Benton

A python program for the Raspi for reading the ADXL 345 Accelerometer and flushing its outputs in a unstructured string: time, x, y, z
(unstructured meaning that it is just string instead of a list or a tuple).
Meant to be used in conjunction with a bash file to write the data out to a txt file and commence websocketing.


NOTE: Time is in seconds since Unix Epoch, not the normal dd/mm/yy hh:mm:ss
WARNING: This is not the actual code from the 2017 R4S project. It is rather a leftover file from my computer that I think is an early iteration of the project. Stuff may not work

"""

import adxl345 
import time
from sys import stdout
from adxl345 import ADXL345

def readAccelerometerX(accelerometer, gees=False):
   #Takes accelerometer tag (Orestes or whatever else = ADXL345()) and a boolean input to read out the data in gees or m/s**2. Default m/s**2.
   #Returns X axis readings
   axes = accelerometer.getAxes(gees)
   accelX = axes['x']
   return accelX

def readAccelerometerY(accelerometer, gees=False):
   #Takes accelerometer tag (Orestes or whatever else = ADXL345()) and a boolean input to read out the data in gees or m/s**2. Default m/s**2.
   #Returns Y axis readings
   axes = accelerometer.getAxes(gees)
   accelY = axes['y']
   return accelY

def readAccelerometerZ(accelerometer, gees=False):
   #Takes accelerometer tag (Orestes or whatever else = ADXL345()) and a boolean input to read out the data in gees or m/s**2. Default m/s**2.
   #Returns Z axis readings
   axes = accelerometer.getAxes(gees)
   accelZ = axes['z']
   return accelZ

def readAccelerometerMagnitude(accelerometerReadout, values):
   #Takes an accelerometer readout input (float or string) and a input named values (list)
   #Returns the Range data value for the accelerometer (float)
   #Used in conjunction with function readAverages
   #Exact use of function not know. It is also not used anywhere else in this code. Will not be supported in future updates
   if not accelerometerReadout == None:
       values.append(accelerometerReadout)
   if len(values) >= 5:
       top = max(values)
       bottom = min(values)
       difference = abs(top-bottom)
       values.pop(0)
       return difference
   else:
       return 0
def readAverages(difference,differenceList, smoothness=100):
   #Takes an float difference (from function ReadAccelerometerMagnitude) and a list input called differenceList) (probrably a list of differences), and a smoothness value default 100)
   #Returns the average of the data set. Smoothness is how big the list has to be before sample size is calculated.
   #Used in conjunction with function readAccelerometerMagnitude
   #Exact use of function not know. It is also not used anywhere else in this code. Will not be supported in future updates
   differenceList.append(difference)
   if len(differenceList) > smoothness:
       average = sum(differenceList)/len(differenceList)
       differenceList.pop(0)
       return average
   else:
       return 0
  
def bars(inputt, scale=0.01):
   #Takes a float/int input named inputt and a float input named scale (default 0.01)
   #returns a visual representation of data with ascii bars. With default scale of 0.01, each # = 100.
   return "#" * int(scale * inputt)
  


if __name__ == "__main__":
  
   accel = adxl345.ADXL345() #I don't know what this is for but I'm too scared to take it out.

   while True:
        orestes = ADXL345() #Orestes is my pet name for the accelerometer. The raspi is affectionatley named the Temeraire. (Only Freespace 2: Blue Planet people would get this)
        readingX = readAccelerometerX(orestes)
        readingY = readAccelerometerY(orestes)
        readingZ = readAccelerometerZ(orestes)
        timestamp = time.time()
        print ("{},{},{},{}".format(timestamp, readingX, readingY, readingZ))
        stdout.flush()



