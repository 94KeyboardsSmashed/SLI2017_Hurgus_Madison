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
import raspi_accel_lib
import raspi_neopixel_lib


#Neopixel Constants
LED_COUNT_1 = 24
LED_PIN_1 = 18
LED_FREQ_HZ_1 = 800000
LED_DMA_1 = 5
LED_BRIGHTNESS_1 = 128
LED_INVERT_1 = False

LED_COUNT_2 = 24
LED_PIN_2 = 13
LED_FREQ_HZ_2 = 800000
LED_DMA_2 = 5
LED_BRIGHTNESS_2 = 128
LED_INVERT_2 = False

#Time until neopixel idle
IDLER_TIME = 1000

#Accelerometer Constants
ACCEL_SENSITIVITY = 5
ACCEL_RESPONSE = 30

if __name__ == '__main__':
    #init global variables
    indus_log = []
    yangtze_log = []
    proceed = True
    idle = IDLER_TIME
    shutdown_lights = True

    #"""Accelerometers will be named after rivers.
    # """
    INDUS = raspi_accel_lib.ADXL345(0x53)
    YANGTZE = raspi_accel_lib.ADXL345(0x1D)

    #"""Neopixel Rings will be named after swords.
    # eg. Katana, Rapier, Saber, Eepee, Gladius, Machete, Cutlass, Trombash"""
    KATANA = raspi_neopixel_lib.Adafruit_NeoPixel(LED_COUNT_1, LED_PIN_1, LED_FREQ_HZ_1,
                                                  LED_DMA_1, LED_INVERT_1, LED_BRIGHTNESS_1, 0)
    SABER = raspi_neopixel_lib.Adafruit_NeoPixel(LED_COUNT_2, LED_PIN_2, LED_FREQ_HZ_2,
                                                  LED_DMA_2, LED_INVERT_2, LED_BRIGHTNESS_2, 1)
    #initiate startup sequence for neopixel
    try:
        #Accel init
        INDUS.accel_startup(False, False)
        YANGTZE.accel_startup(False, False)

        #KATANA init
        KATANA.neopixel_startup(False)
        KATANA.color_wipe(raspi_neopixel_lib.Color(0, 255, 0), 10)
        KATANA.neopixel_shutdown(False)

        #SABER init
        SABER.neopixel_startup(False)
        SABER.color_wipe(raspi_neopixel_lib.Color(0, 255, 0), 10)
        SABER.neopixel_shutdown(False)

    except Exception:
        #KATANA error
        KATANA.color_wipe(raspi_neopixel_lib.Color(255, 0, 0), 10)
        KATANA.neopixel_shutdown(False)

        #SABER error
        SABER.color_wipe(raspi_neopixel_lib.Color(255, 0, 0), 10)
        SABER.neopixel_shutdown(False)

    while proceed:
        try:
            #set accelerometer data percentages
            indusPer = INDUS.read_accel_percentages(ACCEL_SENSITIVITY)
            yangtzePer = YANGTZE.read_accel_percentages(ACCEL_SENSITIVITY) 

            #Process light color by finding averages
            indus_log.append(indusPer['magper'])
            yangtze_log.append(yangtzePer['magper'])

            if len(indus_log) >= ACCEL_RESPONSE:
                indus_log.pop(0)
            indus_avg = sum(indus_log)/len(indus_log)
            
            if len(yangtze_log) >= ACCEL_RESPONSE:
                yangtze_log.pop(0)
            yangtze_avg = sum(yangtze_log)/len(yangtze_log)

            #Do color gradient
            KATANA.color_gradient_rg(indus_avg)
            SABER.color_gradient_rg(yangtze_avg)
			
            #Websocketing
            #combo = timestamp, indusX, indusY, indusZ, indusMag, 
            #timestamp, yangtzeX, yangtzeY, yangtzeZ, yangtzeMag   
            topush = "{},{}".format(INDUS.string_output(), YANGTZE.string_output())
            print(topush)
            stdout.flush()

            #Check For Idleness
            if abs(indus_log[0]/indus_avg) or abs(yangtze_log[0]/yangtze_avg) < 5:
                idle -= 1
            else:
                idle = IDLER_TIME
                shutdown_lights = True
                for i in range(KATANA.numPixels()):
                    KATANA.setBrightness(128)
                    KATANA.show()
                for i in range(SABER.numPixels()):
                    SABER.setBrightness(128)
                    SABER.show()
            if idle <= 0:
                if shutdown_lights:
                    KATANA.neopixel_shutdown(False)
                    SABER.neopixel_shutdown(False)
                    shutdown_lights = False
                else:
                    idle = -5
        except Exception:
            KATANA.color_wipe(raspi_neopixel_lib.Color(255, 0, 0))
            KATANA.neopixel_shutdown(False)
            SABER.color_wipe(raspi_neopixel_lib.Color(255, 0, 0))
            SABER.neopixel_shutdown(False)
            proceed = False
