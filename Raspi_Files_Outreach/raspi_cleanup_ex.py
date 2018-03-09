# -*- coding: utf-8 -*
# Python Main Payload Computing Module

"""
Created on Mon Oct 2 21:13:27 2017

@author: Hyun-seok

IMPORTANT: THIS MODULE REQUIRES ROOT ACCESS TO RUN
Uses indents.

This module is meant to be called in bash scripts to start cleanup 
operations. Simply shuts down neopixel ring.

"""

import raspi_neopixel_lib


#Neopixel Constants
LED_COUNT_1 = 24
LED_PIN_1 = 18
LED_FREQ_HZ_1 = 800000
LED_DMA_1 = 5
LED_BRIGHTNESS_1 = 255
LED_INVERT_1 = False

#Accelerometer Constants
ACCEL_SENSITIVITY = 5
ACCEL_RESPONSE = 30

#Neopixel Colors


if __name__ == '__main__':

    #Defines Neopixel Ring
    AQUITAINE = raspi_neopixel_lib.Adafruit_NeoPixel(LED_COUNT_1, LED_PIN_1, LED_FREQ_HZ_1,
                                                     LED_DMA_1, LED_INVERT_1, LED_BRIGHTNESS_1)
    #Initiates Shutdown Sequence
    AQUITAINE.neopixel_shutdown(False)
