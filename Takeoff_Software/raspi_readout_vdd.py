#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Python Data Collection Module

"""
Created on Tue May  9 12:13:27 2017

@author: Hyun-seok

Please use indents as they are incompatible with spaces
and spaces are a pain in the arse to do 5 times for every indent.

IMPORTANT: REQUIRES ROOT ACCESS TO RUN.

Connect first neopixel to ground, 5v, and physical pin 33 (gpio pin 13)
Connect first ADXL345 to 3.3v, floating, parallel connection to physical pin 3 and 5 (gpio 2,3)
with second ADXL345

GPIO 1 setup: ADXL - Pi

GND - GND
3V - 3V3
SDA - SDA (GPIO 2)
SCL - SCL (GPIO 3)

GPIO 2 setup: ADXL - Pi

GND - GND
3V - 3V3
SDA - SDA
SCL - SCL
SDO - GND

"""

import sys
import raspi_accel_lib
import raspi_neopixel_lib


#Neopixel Constants
LED_COUNT_1 = 24
LED_PIN_1 = 13
LED_FREQ_HZ_1 = 800000
LED_DMA_1 = 5
LED_BRIGHTNESS_1 = 255
LED_INVERT_1 = False


# Accelerometer Settings:

# Read out debug code and startup messages
NOISE = True

# Output readings in Gs, set to false if measurments in m/s**2 is desired
GFORCE = False

if __name__ == '__main__':
    # init global variables

    #"""Accelerometers will be named after rivers.
    # """Indus, Yangtze, Nile, Ganges, Danube, Rhine"""
    YANGTZE = raspi_accel_lib.ADXL345(0x1D)

    #"""Neopixel Rings will be named after swords.
    # eg. Katana, Sabre, Rapier, Eepee, Gladius, Machete, Cutlass, Trombash"""
    SABRE = raspi_neopixel_lib.Adafruit_NeoPixel(LED_COUNT_1, LED_PIN_1, LED_FREQ_HZ_1,
                                                 LED_DMA_1, LED_INVERT_1, LED_BRIGHTNESS_1, 1)
    #initiate startup sequence for neopixel
    try:
        YANGTZE.accel_startup(GFORCE, NOISE)
        SABRE.neopixel_startup(NOISE)
        SABRE.color_wipe(raspi_neopixel_lib.Color(0, 255, 0), 10)
        SABRE.neopixel_shutdown(NOISE)
    except Exception as error:
        SABRE.color_wipe(raspi_neopixel_lib.Color(255, 0, 0), 10)
        SABRE.neopixel_shutdown(NOISE)
        print("# SABRE exited on startup with error: {}".format(error))
        sys.stdout.flush()
        sys.exit(1)

    while True:
        try:
            #Write to file
            print(YANGTZE.string_output(GFORCE))
            sys.stdout.flush()
        except Exception as error:
            SABRE.color_wipe(raspi_neopixel_lib.Color(255, 0, 0))
            SABRE.neopixel_shutdown(NOISE)
            print("# SABRE exited in runtime with error: {}".format(error))
            sys.stdout.flush()
            sys.exit(1)
