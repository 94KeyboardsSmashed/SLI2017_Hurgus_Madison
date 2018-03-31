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

GPIO 1 setup: Component - Pi

First Accelerometer
GND - GND
3V - 3V3
SDA - SDA (GPIO 2)
SCL - SCL (GPIO 3)

First Neopixel
GND - GND
PWR - 5v
INPUT - GPIO 13

GPIO 2 setup: ADXL - Pi

Second Accelerometer
GND - GND
3V - 3V3
SDA - SDA (GPIO 2)
SCL - SCL (GPIO 3)
SDO - GND

Second Neopixel
GND - GND
PWR - 5v
INPUT - GPIO 18
"""

from sys import stdout
import collections
import raspi_accel_lib
import neopixel_lib

#Neopixel Constants
LED_COUNT_1 = 24
LED_PIN_1 = 18
LED_FREQ_HZ_1 = 800000
LED_DMA_1 = 10
LED_BRIGHTNESS_1 = 32
LED_INVERT_1 = False

LED_COUNT_2 = 24
LED_PIN_2 = 13
LED_FREQ_HZ_2 = 800000
LED_DMA_2 = 10
LED_BRIGHTNESS_2 = 32
LED_INVERT_2 = False

YELLOW = neopixel_lib.color_value(32, 32, 0) 
RED = neopixel_lib.color_value(32, 0, 0)
BLUE = neopixel_lib.color_value(0, 0, 32)
GREEN = neopixel_lib.color_value(0, 32, 0)

ACCEL_RESPONSE = 15

if __name__ == '__main__':
    #init global variables
    indus_log = collections.deque(maxlen=ACCEL_RESPONSE)
    yangtze_log = collections.deque(maxlen=ACCEL_RESPONSE)

    #init accelerometers
    INDUS = raspi_accel_lib.ADXL345(0, 0, 0, 0x53)
    YANGTZE = raspi_accel_lib.ADXL345(0, 0, 0, 0x1D)

    #init neopixels
    KATANA = neopixel_lib.Adafruit_NeoPixel(LED_COUNT_1, LED_PIN_1, LED_FREQ_HZ_1,
                                                  LED_DMA_1, LED_INVERT_1, LED_BRIGHTNESS_1, 0)
    SABER = neopixel_lib.Adafruit_NeoPixel(LED_COUNT_2, LED_PIN_2, LED_FREQ_HZ_2,
                                                  LED_DMA_2, LED_INVERT_2, LED_BRIGHTNESS_2, 1)

    #startup neopixels

    #init Katana
    KATANA.neopixel_startup(YELLOW, GREEN, RED)
        
    #init Saber
    SABER.neopixel_startup(YELLOW, GREEN, RED)

    proceed = True
    while proceed:
        try:
            #set accelerometer data percentages
            indus_log.append(int((INDUS.accel_magnitude(True)/5) * 100))
            yangtze_log.append(int((YANGTZE.accel_magnitude(True)/5) * 100))

            indus_avg = sum(indus_log)/len(indus_log)
            yangtze_avg = sum(yangtze_log)/len(yangtze_log)
        
            KATANA.color_gradient_rg(indus_avg)
            SABER.color_gradient_rg(yangtze_avg)        
        
            #Websocketing
            #combo = timestamp, indusX, indusY, indusZ, indusMag, 
            #timestamp, yangtzeX, yangtzeY, yangtzeZ, yangtzeMag   
            print('{},{},{},{}'.format(INDUS.string_output(False), INDUS.accel_magnitude(False), YANGTZE.string_output(False), YANGTZE.accel_magnitude(False)))
            stdout.flush()
        except:
            KATANA.color_wipe(RED)
            KATANA.neopixel_shutdown(False)
            SABER.color_wipe(RED)
            SABER.neopixel_shutdown(False)
            proceed = False
