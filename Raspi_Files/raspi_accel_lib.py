#Python Acceleration Libraries Module
# -*- coding: utf-8 -*-
"""
Created on Tue May  9 12:13:27 2017

@author: Hyun-seok

Sluuurp. Spagetti code debuging. Please use indents as they are incompatible with spaces
and spaces are a pain in the arse to do 5 times for every indent

Accel libraries adapted form ADXL345 Python library for Raspberry Pi by Jonathan Williamson
"""

import smbus
from time import sleep
import math

# select the correct i2c bus for this revision of Raspberry Pi
revision = ([l[12:-1] for l in open('/proc/cpuinfo','r').readlines() if l[:8]=="Revision"]+['0000'])[0]
bus = smbus.SMBus(1 if int(revision, 16) >= 4 else 0)

# ADXL345 constants
EARTH_GRAVITY_MS2   = 9.80665
SCALE_MULTIPLIER    = 0.004

DATA_FORMAT         = 0x31
BW_RATE             = 0x2C
POWER_CTL           = 0x2D

BW_RATE_1600HZ      = 0x0F
BW_RATE_800HZ       = 0x0E
BW_RATE_400HZ       = 0x0D
BW_RATE_200HZ       = 0x0C
BW_RATE_100HZ       = 0x0B
BW_RATE_50HZ        = 0x0A
BW_RATE_25HZ        = 0x09

RANGE_2G            = 0x00
RANGE_4G            = 0x01
RANGE_8G            = 0x02
RANGE_16G           = 0x03

MEASURE             = 0x08
AXES_DATA           = 0x32


def readout_bars(x, scale=0.01):
    return "#" * int(scale * x)

def total_per(data_in, denom=25):
    """Returns percentage of the input over the denom. Use in conjunction with color gradients
    Takes data input in int/float form and a denom for the highest value readable (25 default)"""
    percentage = (data_in/denom)*100
    return percentage

def magnitude_data(inx, iny, inz):
    """Returns 3d distance formula calculations (magnitude) normalized for gravity
    Takes Accelerometer data x, y, and z, in int/float form"""
    return abs(math.sqrt(inx^2 + iny^2 + inz^2)-9.81)

class ADXL345:

    address = None

    def __init__(self, address = 0x53):
        self.address = address
        self.setBandwidthRate(BW_RATE_100HZ)
        self.setRange(RANGE_8G)
        self.enableMeasurement()
        self.x_reading = 0
        self.y_reading = 0
        self.z_reading = 0 
        self.mag_reading = 0

    def enableMeasurement(self):
        """Enables Measurement Readings"""
        bus.write_byte_data(self.address, POWER_CTL, MEASURE)

    def setBandwidthRate(self, rate_flag):
        """set the measurement range for 10-bit readings"""
        bus.write_byte_data(self.address, BW_RATE, rate_flag)

    def setRange(self, range_flag):
        """returns the current reading from the sensor for each axis parameter gforce:
        #    False (default): result is returned in m/s^2
        #    True           : result is returned in gs"""
        value = bus.read_byte_data(self.address, DATA_FORMAT)

        value &= ~0x0F;
        value |= range_flag;  
        value |= 0x08;

        bus.write_byte_data(self.address, DATA_FORMAT, value)
    
    def getAxes(self, gforce = False):
        """Returns the measurement of the axes of the accelerometer in a dictionary (x,y,z)"""
        _bytes = bus.read_i2c_block_data(self.address, AXES_DATA, 6)
        
        x = _bytes[0] | (_bytes[1] << 8)
        if(x & (1 << 16 - 1)):
            x = x - (1<<16)

        y = _bytes[2] | (_bytes[3] << 8)
        if(y & (1 << 16 - 1)):
            y = y - (1<<16)

        z = _bytes[4] | (_bytes[5] << 8)
        if(z & (1 << 16 - 1)):
            z = z - (1<<16)

        x = x * SCALE_MULTIPLIER 
        y = y * SCALE_MULTIPLIER
        z = z * SCALE_MULTIPLIER

        if not gforce:
            x = x * EARTH_GRAVITY_MS2
            y = y * EARTH_GRAVITY_MS2
            z = z * EARTH_GRAVITY_MS2

        x = round(x, 4)
        y = round(y, 4)
        z = round(z, 4)

        return {"x": x, "y": y, "z": z}

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
