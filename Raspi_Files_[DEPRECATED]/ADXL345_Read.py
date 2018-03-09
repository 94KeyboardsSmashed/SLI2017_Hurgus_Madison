import adxl345  
import time
from sys import stdout
from adxl345 import ADXL345

def readAccelerometerX(accelerometer, gees=False):
    axes = accelerometer.getAxes(gees)
    accelX = axes['x']
    return accelX

def readAccelerometerY(accelerometer, gees=False):
    axes = accelerometer.getAxes(gees)
    accelY = axes['y']
    return accelY

def readAccelerometerZ(accelerometer, gees=False):
    axes = accelerometer.getAxes(gees)
    accelZ = axes['z']
    return accelZ

def readAccelerometerMagnitude(accelerometerReadout, values):
    if not accelerometerReadout == None:
        values.append(accelerometerReadout)
    if len(values) >= 5:
        top = max(values)
        bottom = min(values)
        difference = abs(top-bottom)
        values.pop(0)
        return difference
    else:
        return 0
def readAverages(difference,differenceList, smoothness=100):
    differenceList.append(difference)
    if len(differenceList) > smoothness:
        average = sum(differenceList)/len(differenceList)
        differenceList.pop(0)
        return average
    else:
        return 0
    
def bars(x, scale=0.01):
    return "#" * int(scale * x)
    


if __name__ == "__main__":
    
    accel = adxl345.ADXL345()

    while True:
         orestes = ADXL345()
         readingX = readAccelerometerX(orestes)
         readingY = readAccelerometerY(orestes)
         readingZ = readAccelerometerZ(orestes)
         timestamp = time.time()
         print ("{},{},{},{}".format(timestamp, readingX, readingY, readingZ))
         stdout.flush()

