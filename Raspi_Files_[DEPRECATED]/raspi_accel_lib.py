#Python Acceleration Libraries Module
# -*- coding: utf-8 -*-
"""
Created on Tue May  9 12:13:27 2017

@author: Hyun-seok

Sluuurp. Spagetti code debuging. Please use indents as they are incompatible with spaces
and spaces are a pain in the arse to do 5 times for every indent

Frack pep 8. 162 problems
"""

from sys import stdout
import time
import math
from neopixel import *
import adxl345
from adxl345 import ADXL345

#Misc functions

def wheel(pos):
    """Generate rainbow colors across 0-255 positions."""
    if pos < 85:
        return Color(pos * 3, 255 - pos * 3, 0)
    elif pos < 170:
        pos -= 85
        return Color(255 - pos * 3, 0, pos * 3)
    else:
        pos -= 170
        return Color(0, pos * 3, 255 - pos * 3)


#Accelerometer Based Commands
class AccelerometerRead:
    """Class for reading accelerometer outputs. Init instance accelerometer ID and name"""
    def __init__(self, name):
        """Tales an acclereometer ID and a name"""
        self.name = name
        self.x_measurement = 0
        self.y_measurement = 0
        self.z_measurement = 0
        self.mag_measurement = 0
        self.socket_readout = "# Starting Up"

    def read_accelerometer_x(self, gees=False):
        """Reads Accelerometer data on the X axis
        Inputs acceleometer ID and a boolean for outputing gees or m/s. Default m/s"""
        axes = self.getAxes(gees)
        accel_x = axes['x']
        self.x_measurement = accel_x

    def read_accelerometer_y(self, gees=False):
        """Reads Accelerometer data on the Y axis
        Inputs acceleometer ID and a boolean for outputing gees or m/s. Default m/s"""
        axes = self.getAxes(gees)
        accel_y = axes['y']
        self.y_measurement = accel_y

    def read_accelerometer_z(self, gees=False):
        """Reads Accelerometer data on the Z axis
        Inputs acceleometer ID and a boolean for outputing gees or m/s. Default m/s"""
        axes = self.getAxes(gees)
        accel_z = axes['z']
        self.z_measurement = accel_z

    def read_accelerometer_mag(self, gees=False):
        """Returns 3d distance formula calculations (magnitude) normalized for gravity
        Inputs acceleometer ID and a boolean for outputing gees or m/s. Default m/s"""
        axes = self.getAxes(gees)
        accel_x = axes['x']
        accel_y = axes['y']
        accel_z = axes['z']
        self.mag_measurement = abs(math.sqrt(accel_x^2 + accel_y^2 + accel_z^2)-9.81)
    
    def websocketing(self, gees=False):
        """Returns string in form of timestamp (unix epoch), x, y, z"""
        axes = self.getAxes(gees)
        accel_x = axes['x']
        accel_y = axes['y']
        accel_z = axes['z']
        timestamp = time.time()
        self.socket_readout = "{},{},{},{}".format(timestamp, accel_x, accel_y, accel_z)

#---------------------------------------------------------------------------------------#

#Neopixel based commands

class NeopixelOutput:
    """Class for outputing commands to the neopixel. Init with name of neopixel"""
    def __init__(self, name):
        self.name = name

    ##Subset 1. Neopixel based gradient commands:

    def pulsation(self, color):
        """Pulses the Neopixel in a light gradient"""
        for _time in range(63):
            pulsateNeoPixel(self, _times*4, color)
        for _time in range(63):
            negative_time = 63-_time
            pulsateNeoPixel(self, negative_time*4, color)

    def color_gradient_rg(self, percentage):
        """Puts the Neopixel in a color gradient from red to green based on input percentage
        Input strip id and float or int between 0 and 100 (inclusive)"""
        redness = 255
        greeness = 0
        numberper = percentage
        redness -= 2.55*numberper
        greeness += 2.55*numberper
        if redness < 0:
            redness = 0
        if greeness > 255:
            greeness = 255
        for i in range(self.numPixels()):
            self.setPixelColor(i, Color(int(redness), int(greeness), 0))
            self.show()

    def color_gradient_br(self, percentage):
        """Puts the Neopixel in a color gradient from blue to red based on input percentage
        Input strip id and float or int between 0 and 100 (inclusive)"""
        blueness = 255
        greeness = 0
        numberper = percentage
        blueness -= 2.55*numberper
        greeness += 2.55*numberper
        if blueness < 0:
            blueness = 0
        if greeness > 255:
            greeness = 255

        for i in range(self.numPixels()):
            self.setPixelColor(i, Color(0, int(greeness), int(blueness)))
            self.show()

    def color_gradient_rv(self, percentage):
        """Puts the Neopixel in a color gradient from Red to violet based on input percentage
        Input strip id and float or int between 0 and 100 (inclusive)"""
        redness = 255
        blueness = 0
        numberper = percentage
        redness -= 2.55*numberper
        blueness += 2.55*numberper
        if redness < 0:
            redness = 0
        if blueness > 255:
            blueness = 255
        for i in range(self.numPixels()):
            self.setPixelColor(i, Color(int(redness), 0, int(blueness)))
            self.show()

    def total_color_gradient(self, perx, pery, perz, redness=0, greeness=0, blueness=0):
        """Puts the Neopixel in a color gradient from any color
        based on input percentage of three values
        Input strip id and 3 float or int between 0 and 100 (inclusive).
        Var a, b, and c takes int/floats based on 0-255 color scale. Default 0"""
        greeness += 2.55*perx
        redness += 2.55*pery
        blueness += 2.55*perz
        if greeness > 255:
            greeness = 255
        if redness > 255:
            redness = 255
        if blueness > 255:
            blueness = 255
        for i in range(self.numPixels()):
            self.setPixelColor(i, Color(int(redness), int(greeness), int(blueness)))
            self.show()

    ## instances adapted from functions from Tony DiCola's strandtest (in deprecated files)

    def theater_chase(self, color, wait_ms=50, iterations=10):
        """Movie theater light style chaser animation."""
        for j in range(iterations):
            for spin in range(3):
                for i in range(0, self.numPixels(), 3):
                    self.setPixelColor(i+spin, color)
                self.show()
                time.sleep(wait_ms/1000.0)
                for i in range(0, self.numPixels(), 3):
                    self.setPixelColor(i+spin, 0)

    def rainbow(self, wait_ms=20, iterations=1):
        """Draw rainbow that fades across all pixels at once."""
        for j in range(256*iterations):
            for i in range(self.numPixels()):
                self.setPixelColor(i, wheel((i+j) & 255))
            self.show()
            time.sleep(wait_ms/1000.0)

    def rainbow_cycle(self, wait_ms=20, iterations=5):
        """Draw rainbow that uniformly distributes itself across all pixels."""
        for j in range(256*iterations):
            for i in range(self.numPixels()):
                self.setPixelColor(i, wheel((int(i * 256 / self.numPixels()) + j) & 255))
            self.show()
            time.sleep(wait_ms/1000.0)

    def theater_chase_rainbow(self, wait_ms=50):
        """Rainbow movie theater light style chaser animation."""
        for j in range(256):
            for spin in range(3):
                for i in range(0, self.numPixels(), 3):
                    self.setPixelColor(i+spin, wheel((i+j) % 255))
                self.show()
                time.sleep(wait_ms/1000.0)
                for i in range(0, self.numPixels(), 3):
                    self.setPixelColor(i+spin, 0)
					
	def color_wipe(self, color, wait_ms=50):
        """Wipe color across display a pixel at a time."""
        """Inputs strip id, color 0-255 int/float, and wait_ms in int/float value for sleep time
        in miliseconds (currently not implimented)"""
        for i in range(self.numPixels()):
            self.setPixelColor(i, color)
            self.setBrightness(255)
            self.show()
            time.sleep(wait_ms/1000.0)
#Data Synthesis
def total_per(data_in, denom=25):
    """Returns percentage of the input over the denom. Use in conjunction with color gradients
    Takes data input in int/float form and a denom for the highest value readable (25 default)"""
    percentage = (data_in/denom)*100
    return percentage

def magnitude_data(inx, iny, inz):
    """Returns 3d distance formula calculations (magnitude) normalized for gravity
    Takes Accelerometer data x, y, and z, in int/float form"""
    return abs(math.sqrt(inx^2 + iny^2 + inz^2)-9.81)

