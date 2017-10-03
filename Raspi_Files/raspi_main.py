# -*- coding: utf-8 -*
# Python Main Payload Computing Module

"""
Created on Mon Oct 2 21:13:27 2017

@author: Hyun-seok

Uses indents

"""

import raspi_accel_lib
import raspi_neopixel_lib


#Neopixel Constants
LED_COUNT_1 = 24
LED_PIN_1 = 18
LED_FREQ_HZ_1 = 800000
LED_DMA_1 = 5
LED_BRIGHTNESS_1 = 255
LED_INVERT_1 = False

#Neopixel Colors


if __name__ == '__main__':
    print("Debugger Log:")
    print("Initiating Startup")
    #"""Accelerometers will be named after swords.
    # eg. Katana, Rapier, Saber, Eepee, Gladius, Machete, Cutlass, Trombash"""
    KATANA = raspi_accel_lib.ADXL345()

    #"""Neopixel Rings will be named after regions of france.
    # eg. Aquitaine, Corsica, Brittany, Normandy"""
    AQUITAINE = raspi_neopixel_lib.Adafruit_NeoPixel(LED_COUNT_1, LED_PIN_1, LED_FREQ_HZ_1,
                                                     LED_DMA_1, LED_INVERT_1, LED_BRIGHTNESS_1)
    #initiate startup sequence for neopixel
    KATANA.accel_startup()
    AQUITAINE.neopixel_startup()

    while True:
        per_x = raspi_accel_lib.total_per(KATANA.read_accelerometer_x())
        per_y = raspi_accel_lib.total_per(KATANA.read_accelerometer_y())
        per_z = raspi_accel_lib.total_per(KATANA.read_accelerometer_z())
        per_mag = raspi_accel_lib.total_per(KATANA.read_accelerometer_mag())

        AQUITAINE.color_gradient_rg(per_mag)


