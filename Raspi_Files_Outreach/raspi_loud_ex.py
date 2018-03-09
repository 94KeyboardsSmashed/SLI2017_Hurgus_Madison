# -*- coding: utf-8 -*
# Python Main Payload Computing Module

"""
Created on Mon Oct 2 21:13:27 2017

@author: Hyun-seok

IMPORTANT: THIS MODULE REQUIRES ROOT ACCESS TO RUN
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

#Accelerometer Constants
ACCEL_SENSITIVITY = 10
ACCEL_RESPONSE = 25

#Neopixel Colors


if __name__ == '__main__':
    #init global variables
    per_mag_log = []
    proceed = True
    #Set up shell output
    print("# Debugger Log:")
    print("# Initiating Startup...")
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

    while proceed:
        try:
            #Get values in percentages
            per_x = raspi_accel_lib.total_per(KATANA.read_accelerometer_x(), ACCEL_SENSITIVITY)
            per_y = raspi_accel_lib.total_per(KATANA.read_accelerometer_y(), ACCEL_SENSITIVITY)
            per_z = raspi_accel_lib.total_per(KATANA.read_accelerometer_z(), ACCEL_SENSITIVITY)
            per_mag = raspi_accel_lib.total_per(KATANA.read_accelerometer_mag(), ACCEL_SENSITIVITY)

            #Process light color by finding averages
            per_mag_log.append(per_mag)
            if len(per_mag_log) >=ACCEL_RESPONSE:
                per_mag_log.pop(0)
            per_mag_avg = sum(per_mag_log)/len(per_mag_log)

            #Do color gradient
            AQUITAINE.color_gradient_rg(per_mag_avg)

            print(KATANA.string_output())

        except (KeyboardInterrupt, SystemExit):
            for i in range(AQUITAINE.numPixels()):
                AQUITAINE.setBrightness(0)
                AQUITAINE.show()
            proceed = False
