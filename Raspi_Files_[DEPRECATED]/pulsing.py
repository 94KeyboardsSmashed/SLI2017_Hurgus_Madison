from neopixel import *
import time

LED_COUNT      = 24      
LED_PIN        = 18      
LED_FREQ_HZ    = 800000  
LED_DMA        = 5       
LED_BRIGHTNESS = 255     
LED_INVERT     = False



def pulsateNeoPixel(strip, brightness, Color):
    for i in range(strip.numPixels()):
        strip.setPixelColor(i,Color)
#        strip.show()
        strip.setBrightness(brightness)
        strip.show()

def pulsation(color, strip):
        for t in range(63):
            pulsateNeoPixel(strip, t*4, color)
        for t in range(63):
            n = 63-t
            pulsateNeoPixel(strip, n*4, color)

def colorWipe(strip, color, wait_ms=50):
    """Wipe color across display a pixel at a time."""
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, color)
        strip.setBrightness(255)
        strip.show()
        time.sleep(0.01)

def option1():
    while True:
        pulsation(Color(30,0,205))
        pulsation(Color(205,0,205))
        pulsation(Color(205,0,30))
        pulsation(Color(205,0,205))
        colorWipe(strip,Color(30,0,205))
        time.sleep(0.25)
        colorWipe(strip,Color(205,0,205))
        time.sleep(0.25)
        colorWipe(strip,Color(205,0,30))
        time.sleep(0.25)
        colorWipe(strip,Color(205,0,30))
        time.sleep(0.25)

if __name__ == '__main__':
    strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS)
    strip.begin()

    while True:
        pulsation(Color(30,0,205))
        pulsation(Color(205,0,205))
        pulsation(Color(205,0,30))
        pulsation(Color(205,0,205))
        colorWipe(strip,Color(30,0,205))
        strip.setBrightness(0)
        time.sleep(0.25)
        colorWipe(strip,Color(205,0,205))
        strip.setBrightness(0)
        time.sleep(0.25)
        colorWipe(strip,Color(205,0,30))
        strip.setBrightness(0)
        time.sleep(0.25)
        colorWipe(strip,Color(205,0,30))
        strip.setBrightness(0)
        time.sleep(0.25)

"""
    for i in range(strip.numPixels()):
        strip.setBrightness(255)
        strip.show()
        strip.setPixelColor(i, Color(0,255,0))
        strip.show()
        
    time.sleep(5)
"""

