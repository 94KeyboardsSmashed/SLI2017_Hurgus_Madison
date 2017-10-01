#import the adxl345 module
import adxl345
import time

#create ADXL345 object
accel = adxl345.ADXL345()

#get axes as g
# to get axes as ms^2 use
#axes = accel.getAxes(False)
while True:
    axes = accel.getAxes(True)
    #put the axes into variables
    x = axes['x']
    #print axes
    print (x)
    time.sleep(0.5)