<<<<<<< HEAD
# -*- coding: utf-8 -*-
"""
Created on Fri September 22 12:13:27 2017

@author: Hyun-seok

A small Python script for plotting the X, Y, and Z values that are read by the acceleometer
Accepts a .txt file with readouts from accelerometer

"""
import numpy as np
import math
import matplotlib.pyplot as plt

def mag(value):
    #Calculates Magnitude (sqrt(x^2+y^2+z^2))
    #Takes list of tuples (x, y, z)
    return math.sqrt(sum(float(i)**2 for i in value))

def linesplit(number):
    #Parses log data into values into a iterable list
    #Takes an integer between 0 and 3. 0 is time, 1 is x, 2 is y, 3 is z.
    #Be sure to sanitize the created list to make it readable for the program
    return [line.split(",")[number] for line in lines]

def sanitize(lst):
    #Gets rid of unnessesary spaces from the log file.
    #Use to after linesplit to make lists readable by python
    return [s.rstrip() for s in lst]


#Have log.txt in the same folder as this code.
#Name of log has to be same as name in the open function

with open('Example_Log.txt') as log: #Change file in open() command to match file name
    lines = log.readlines()        
  
    rawtime = linesplit(0)
    rawX = linesplit(1)
    rawY = linesplit(2)
    rawZ = linesplit(3)
    
    time = sanitize(rawtime)     
    x = sanitize(rawX)
    y = sanitize(rawY)
    z = sanitize(rawZ)

    #consult matplotlib libraries, especially pyplot.
    plt.figure()

    #subplot 1. X axis read-outs on a regular graph. Green
    plt.subplot(3, 1, 1)
    plt.plot(time, x, 'g')
    plt.axhline(y=0, color='b', linestyle='-') #just a line on y=0 for reference
    plt.ylabel("Amplitude (normalized log scale)")
    plt.xlabel("Frequency (in Hertz)")

    #subplot 2. Y axis read-outs on a regular graph. Red
    plt.subplot(3, 1, 2)
    plt.plot(time, y, 'r')
    plt.axhline(y=0, color='b', linestyle='-') #just a line on y=0 for reference
    plt.ylabel("acceleration m/s**2")
    plt.xlabel("time (s)")

    #subplot 3. Z axis read-outs on a regular graph. Blue
    plt.subplot(3, 1, 3)
    plt.plot(time, z)
    plt.axhline(y=0, color='b', linestyle='-')
    plt.ylabel("acceleration m/s**2")
    plt.xlabel("time (s)")
    plt.show()

=======
# -*- coding: utf-8 -*-
"""
Created on Fri September 22 12:13:27 2017

@author: Hyun-seok

A small Python script for plotting the X, Y, and Z values that are read by the acceleometer
Accepts a .txt file with readouts from accelerometer

"""
import numpy as np
import math
import matplotlib.pyplot as plt

def mag(value):
    #Calculates Magnitude (sqrt(x^2+y^2+z^2))
    #Takes list of tuples (x, y, z)
    return math.sqrt(sum(float(i)**2 for i in value))

def linesplit(number):
    #Parses log data into values into a iterable list
    #Takes an integer between 0 and 3. 0 is time, 1 is x, 2 is y, 3 is z.
    #Be sure to sanitize the created list to make it readable for the program
    return [line.split(",")[number] for line in lines]

def sanitize(lst):
    #Gets rid of unnessesary spaces from the log file.
    #Use to after linesplit to make lists readable by python
    return [s.rstrip() for s in lst]


#Have log.txt in the same folder as this code.
#Name of log has to be same as name in the open function

with open('Example_Log.txt') as log: #Change file in open() command to match file name
    lines = log.readlines()        
  
    rawtime = linesplit(0)
    rawX = linesplit(1)
    rawY = linesplit(2)
    rawZ = linesplit(3)
    
    time = sanitize(rawtime)     
    x = sanitize(rawX)
    y = sanitize(rawY)
    z = sanitize(rawZ)

    #consult matplotlib libraries, especially pyplot.
    plt.figure()

    #subplot 1. X axis read-outs on a regular graph. Green
    plt.subplot(3, 1, 1)
    plt.plot(time, x, 'g')
    plt.axhline(y=0, color='b', linestyle='-') #just a line on y=0 for reference
    plt.ylabel("Amplitude (normalized log scale)")
    plt.xlabel("Frequency (in Hertz)")

    #subplot 2. Y axis read-outs on a regular graph. Red
    plt.subplot(3, 1, 2)
    plt.plot(time, y, 'r')
    plt.axhline(y=0, color='b', linestyle='-') #just a line on y=0 for reference
    plt.ylabel("acceleration m/s**2")
    plt.xlabel("time (s)")

    #subplot 3. Z axis read-outs on a regular graph. Blue
    plt.subplot(3, 1, 3)
    plt.plot(time, z)
    plt.axhline(y=0, color='b', linestyle='-')
    plt.ylabel("acceleration m/s**2")
    plt.xlabel("time (s)")
    plt.show()

>>>>>>> 30f08022b85e2a73a674a63069ca1383533668f0
