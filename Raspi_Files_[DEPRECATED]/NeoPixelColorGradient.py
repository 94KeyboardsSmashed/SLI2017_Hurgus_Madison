from neopixel import *
#from strandtest import rainbow 
import time

LED_COUNT     = 16
LED_PIN       = 18
LED_FREQ_HZ   = 800000
LED_DMA       = 5
LED_BRIGHTNESS = 255
LED_INVERT    = False

    
def ColorGradientRG(strip, percentage):
    a = 255
    b = 0
    n = percentage
    a-=2.55*n
    b+=2.55*n
    
    if a < 0:
        a = 0
    if b > 255:
        b = 255

    for i in range(strip.numPixels()):
        strip.setPixelColor(i, Color(int(a),int(b),0))
        strip.show()

def ColorGradientBR(strip, percentage):
    a = 255
    b = 0
    n = percentage
    a-=2.55*n
    b+=2.55*n
    
    if a < 0:
        a = 0
    if b > 255:
        b = 255

    for i in range(strip.numPixels()):
        strip.setPixelColor(i, Color(0,int(b),int(a)))
        strip.show()
        
def ColorGradientRV(strip, percentage):
    a = 255
    b = 0
    n = percentage
    a-=2.55*n
    b+=2.55*n
    
    if a < 0:
        a = 0
    if b > 255:
        b = 255

    for i in range(strip.numPixels()):
        strip.setPixelColor(i, Color(int(a),0,int(b)))
        strip.show()
        
def TotalColorGradient(strip, perX, perY, perZ, a=0, b=0, c=0):
    a+=2.55*perX
    b+=2.55*perY
    c+=2.55*perZ
    if a > 255:
        a = 255
    if b > 255:
        b = 255
    if c > 255:
        c = 255
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, Color(int(b),int(a),int(c)))
        strip.show()
            
if __name__ == '__main__':
    strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS)
    strip.begin()


