#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#Python Acceleration Libraries Module

"""
Created on Tue May  9 12:13:27 2017

@author: Hyun-seok

Please use indents as they are incompatible with spaces
and spaces are a pain in the arse to do 5 times for every indent

Accel libraries adapted form ADXL345 Python library for Raspberry Pi by Jonathan Williamson.
"""

import time
import math
import smbus

# select the correct i2c bus for this revision of Raspberry Pi
REVISION = ([l[12:-1] for l in open('/proc/cpuinfo', 'r').readlines() if l[:8] == "Revision"]+['0000'])[0]
BUS = smbus.SMBus(1 if int(REVISION, 16) >= 4 else 0)

# ADXL345 constants
EARTH_GRAVITY_MS2 = 9.80665
SCALE_MULTIPLIER = 0.004

DATA_FORMAT = 0x31
BW_RATE = 0x2C
POWER_CTL = 0x2D

BW_RATE_1600HZ = 0x0F
BW_RATE_800HZ = 0x0E
BW_RATE_400HZ = 0x0D
BW_RATE_200HZ = 0x0C
BW_RATE_100HZ = 0x0B
BW_RATE_50HZ = 0x0A
BW_RATE_25HZ = 0x09

RANGE_2G = 0x00
RANGE_4G = 0x01
RANGE_8G = 0x02
RANGE_16G = 0x03

MEASURE = 0x08
AXES_DATA = 0x32

class ADXL345:
    """Main Class for everything to do with the ADXL345"""

    address = None

    def __init__(self, address=0x53):
        self.address = address
        self.set_bandwidth_rate(BW_RATE_100HZ)
        self.set_range(RANGE_8G)
        self.enable_measurement()
        self.x_measurement = 0
        self.y_measurement = 0
        self.z_measurement = 0
        self.mag_measurement = 0

    def enable_measurement(self):
        """Enables Measurement Readings"""
        BUS.write_byte_data(self.address, POWER_CTL, MEASURE)

    def set_bandwidth_rate(self, rate_flag):
        """set the measurement range for 10-bit readings"""
        BUS.write_byte_data(self.address, BW_RATE, rate_flag)

    def set_range(self, range_flag):
        """returns the current reading from the sensor for each axis parameter gforce:
        #    False (default): result is returned in m/s^2
        #    True           : result is returned in gs"""
        value = BUS.read_byte_data(self.address, DATA_FORMAT)

        value &= ~0x0F;
        value |= range_flag;
        value |= 0x08;

        BUS.write_byte_data(self.address, DATA_FORMAT, value)

    def get_axes(self, gforce=False):
        """Returns the measurement of the axes of the accelerometer in a dictionary (x,y,z)"""
        _bytes = BUS.read_i2c_block_data(self.address, AXES_DATA, 6)

        _x = _bytes[0] | (_bytes[1] << 8)
        if _x & (1 << 16 - 1):
            _x = _x - (1<<16)

        _y = _bytes[2] | (_bytes[3] << 8)
        if _y & (1 << 16 - 1):
            _y = _y - (1<<16)

        _z = _bytes[4] | (_bytes[5] << 8)
        if _z & (1 << 16 - 1):
            _z = _z - (1<<16)

        _x = _x * SCALE_MULTIPLIER
        _y = _y * SCALE_MULTIPLIER
        _z = _z * SCALE_MULTIPLIER

        if not gforce:
            _x = _x * EARTH_GRAVITY_MS2
            _y = _y * EARTH_GRAVITY_MS2
            _z = _z * EARTH_GRAVITY_MS2

        _x = round(_x, 4)
        _y = round(_y, 4)
        _z = round(_z, 4)

        return {"x": _x, "y": _y, "z": _z}

    def string_output(self, gees=False):
        """Returns a string 'time, x, y, z'"""
        axes = self.get_axes(gees)
        return "{},{},{},{}".format(time.time(), axes['x'], axes['y'], axes['z'])

    def accel_startup(self, gees=False, noise=True):
        """Reads out a couple accelerometer values (disable with noise = False)
        and checks for errors."""
        axes = self.get_axes(gees)
        x_readout = axes['x']
        y_readout = axes['y']
        z_readout = axes['z']
        mag = abs(math.sqrt(axes['x']**2 + axes['y']**2 + axes['z']**2)-9.81)
        # Read out values for debugging
        if noise:
            print("# Starting up accelerometer")
            print("# Outputting values...")
            # Formal data values
            print("# {}".format(self.string_output(gees)))
            # Comparative Test Values (should be similar)
            print("# Timestamp: {}".format(time.time()))
            print("# X: {}".format(x_readout))
            print("# Y: {}".format(y_readout))
            print("# Z: {}".format(z_readout))
            print("# Magnitude: {}".format(mag))
        if x_readout > 24 or y_readout > 24 or z_readout > 24:
            raise ValueError("Accelerometer readout is too high. Hold payload still during startup")

        if x_readout < -15 or y_readout < -15 or z_readout < -15:
            raise ValueError("Accelerometer readout is too low. Hold payload still during startup")