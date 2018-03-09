# -*- coding: utf-8 -*-
# Python Data Collection Module

"""
Created on Tue May  9 12:13:27 2017

@author: Hyun-seok

Please use indents as they are incompatible with spaces
and spaces are a pain in the arse to do 5 times for every indent.

IMPORTANT: REQUIRES ROOT ACCESS TO RUN.

Connect neopixel to ground, 5v, and physical pin 12 (gpio pin 18)
Connect ADXL345 to 3.3v, ground, parallel connection to physical pin 3 and 5 (gpio 2,3)

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

from sys import stdout
import raspi_accel_lib
import raspi_neopixel_lib


#Neopixel Constants
LED_COUNT_1 = 24
LED_PIN_1 = 18
LED_FREQ_HZ_1 = 800000
LED_DMA_1 = 5
LED_BRIGHTNESS_1 = 255
LED_INVERT_1 = False

if __name__ == '__main__':
    #init global variables
    proceed = True

    #"""Accelerometers will be named after rivers.
    # """
    INDUS = raspi_accel_lib.ADXL345(0x53)

    #"""Neopixel Rings will be named after swords.
    # eg. Katana, Rapier, Saber, Eepee, Gladius, Machete, Cutlass, Trombash"""
    KATANA = raspi_neopixel_lib.Adafruit_NeoPixel(LED_COUNT_1, LED_PIN_1, LED_FREQ_HZ_1,
                                                  LED_DMA_1, LED_INVERT_1, LED_BRIGHTNESS_1, 0)
    #initiate startup sequence for neopixel
    try:
        INDUS.accel_startup(False, False)
        KATANA.neopixel_startup(False)
        KATANA.color_wipe(raspi_neopixel_lib.Color(0, 255, 0), 10)
        KATANA.neopixel_shutdown(False)
    except Exception:
        KATANA.color_wipe(raspi_neopixel_lib.Color(255, 0, 0), 10)
        KATANA.neopixel_shutdown(False)

    while proceed:
        try:
            #Write to file
            print(INDUS.string_output())
            stdout.flush()
        except Exception:
            KATANA.color_wipe(raspi_neopixel_lib.Color(255, 0, 0))
            KATANA.neopixel_shutdown(False)
            proceed = False