# -*- coding: utf-8 -*-
# Python Data Collection Module

"""
Created on Tue May  9 12:13:27 2017

@author: Hyun-seok

Please use indents as they are incompatible with spaces
and spaces are a pain in the arse to do 5 times for every indent.

IMPORTANT: REQUIRES ROOT ACCESS TO RUN.

Connect neopixel to ground, 5v, and physical pin 33 (gpio pin 13)
Connect ADXL345 to 3.3v, 3.3v, parallel connection to physical pin 3 and 5 (gpio 2,3)
"""

from sys import stdout
import raspi_accel_lib
import raspi_neopixel_lib


#Neopixel Constants
LED_COUNT_1 = 24
LED_PIN_1 = 13
LED_FREQ_HZ_1 = 800000
LED_DMA_1 = 5
LED_BRIGHTNESS_1 = 255
LED_INVERT_1 = False

if __name__ == '__main__':
    #init global variables
    proceed = True

    #"""Accelerometers will be named after rivers.
    # """Indus, Yangtze, Nile, Ganges, Danube, Rhine"""
    YANGTZE = raspi_accel_lib.ADXL345(0x1D)

    #"""Neopixel Rings will be named after swords.
    # eg. Katana, Sabre, Rapier, Eepee, Gladius, Machete, Cutlass, Trombash"""
    SABRE = raspi_neopixel_lib.Adafruit_NeoPixel(LED_COUNT_1, LED_PIN_1, LED_FREQ_HZ_1,
                                                LED_DMA_1, LED_INVERT_1, LED_BRIGHTNESS_1, 1)
    #initiate startup sequence for neopixel
    try:
        YANGTZE.accel_startup(False, False)
        SABRE.neopixel_startup(False)
        SABRE.color_wipe(raspi_neopixel_lib.Color(0, 255, 0), 10)
        SABRE.neopixel_shutdown(False)
    except Exception:
        SABRE.color_wipe(raspi_neopixel_lib.Color(255, 0, 0), 10)
        SABRE.neopixel_shutdown(False)

    while proceed:
        try:
            #Write to file
            print(YANGTZE.string_output())
            stdout.flush()
        except Exception:
            SABRE.color_wipe(raspi_neopixel_lib.Color(255, 0, 0))
            SABRE.neopixel_shutdown(False)
            proceed = False
