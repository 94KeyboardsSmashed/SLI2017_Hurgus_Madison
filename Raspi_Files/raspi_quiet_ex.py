# -*- coding: utf-8 -*
# Python Main Demonstration Computing Module

"""
Created on Mon Oct 2 21:13:27 2017

@author: Hyun-seok

IMPORTANT: THIS MODULE REQUIRES ROOT ACCESS TO RUN
Uses indents

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
IDLER_TIME = 200

#Accelerometer Constants
ACCEL_SENSITIVITY = 5
ACCEL_RESPONSE = 30

#Neopixel Colors


if __name__ == '__main__':
    #init global variables
    per_mag_log = []
    proceed = True
    idle = IDLER_TIME
    shutdown_lights = True

    #"""Accelerometers will be named after swords.
    # eg. Katana, Rapier, Saber, Eepee, Gladius, Machete, Cutlass, Trombash"""
    KATANA = raspi_accel_lib.ADXL345()

    #"""Neopixel Rings will be named after regions of france.
    # eg. Aquitaine, Corsica, Brittany, Normandy"""
    AQUITAINE = raspi_neopixel_lib.Adafruit_NeoPixel(LED_COUNT_1, LED_PIN_1, LED_FREQ_HZ_1,
                                                     LED_DMA_1, LED_INVERT_1, LED_BRIGHTNESS_1)
    #initiate startup sequence for neopixel
    KATANA.accel_startup(False, False)
    AQUITAINE.neopixel_startup(False)

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
			
            #Websocketing        
            print(KATANA.string_output())
            stdout.flush()

            #Check For Idleness
            if abs(per_mag_log[0]/per_mag_log[-1]) < 5:
                idle -= 1
            else:
                idle = IDLER_TIME
                shutdown_lights = True
                for i in range(AQUITAINE.numPixels()):
                    AQUITAINE.setBrightness(255)
                    AQUITAINE.show()
            if idle <= 0:
                if shutdown_lights:
                    AQUITAINE.neopixel_shutdown(False)
                    shutdown_lights = False
                else:
                    pass

        except (KeyboardInterrupt, SystemExit):
            AQUITAINE.neopixel_shutdown(False)
            proceed = False
