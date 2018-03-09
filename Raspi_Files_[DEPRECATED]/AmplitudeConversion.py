
import adxl345
import time
from pulsing import * #
from neopixel import * #
from ADXL345_Read import * 
from NeoPixelColorGradient import *
from sys import stdout

LED_COUNT     = 24
LED_PIN       = 18
LED_FREQ_HZ   = 800000
LED_DMA       = 5
LED_BRIGHTNESS = 255
LED_INVERT    = False
    
def TotalPer(values, averages, accelerometerIn, denom=4, smoothness=5):
    difference = readAccelerometerMagnitude(accelerometerIn, values)
    average = readAverages(difference, averages, smoothness)
    percentage = (average/denom)*100
    return percentage

def websocketing(accelerometer):
    orestes = accelerometer
    readingX = readAccelerometerX(orestes)
    readingY = readAccelerometerY(orestes)
    readingZ = readAccelerometerZ(orestes)
    timestamp = time.time()
    print ("{},{},{},{}".format(timestamp, readingX, readingY, readingZ))
    stdout.flush()

def case(argument):
    if argument == 0:
        pulsation(Color(30,0,205), strip)
    if argument == 1:
        pulsation(Color(205,0,205), strip)
    if argument == 2:
        pulsation(Color(205,0,30), strip)
    if argument == 3:
        pulsation(Color(205,0,205), strip)
    if argument == 4:
        colorWipe(strip,Color(30,0,205))
        time.sleep(0.25)
    if argument == 5:
        colorWipe(strip,Color(205,0,205))
        time.sleep(0.25)
    if argument == 6:
        colorWipe(strip,Color(205,0,30))
        time.sleep(0.25)
    if argument == 7:
        colorWipe(strip,Color(205,0,30))
        time.sleep(0.25)

if __name__ == "__main__":
    idle = 200
    a = 0
    accel = adxl345.ADXL345()
    
    strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS)
    strip.begin()
    
    valuesX = []
    averagesX = []

    valuesY = []
    averagesY = []

    valuesZ = []
    averagesZ = []

    #style = input('1:GradeX, 2:GradeY, 3:GradeZ, 4:Value : ')
    style = input("Enter style: ")
    websocket = input("WebSocket[y/n]: ")
    
    while True:

            perX = TotalPer(valuesX, averagesX, readAccelerometerX(accel, True))
            perY = TotalPer(valuesY, averagesY, readAccelerometerY(accel, True))
            perZ = TotalPer(valuesZ, averagesZ, readAccelerometerZ(accel, True))
            print (perX, perY, perZ)

            if websocket == 'y':
                websocketing(accel)
            elif websocket == 'n':
                print ("websocket disabled :(") 

            if style == '4':
                TotalColorGradient(strip, perX, perY, perZ)
            elif style == '1':
                ColorGradientRG(strip, perX)
            elif style == '2':
                ColorGradientBR(strip, perY)
            elif style == '3':
                ColorGradientRV(strip, perZ)
               
            if perX < 2 and perY < 2 and perZ < 2:
                idle -= 1
            else:
                idle = 200
                strip.setBrightness(LED_BRIGHTNESS)
                strip.show()
            if idle <= 0:
                case(a)
                a += 1
                if a == 7:
                  a = 0
          
        
