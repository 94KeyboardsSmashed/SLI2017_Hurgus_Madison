# -*- coding: utf-8 -*-
"""
Created on Tue May  9 12:13:27 2017

@author: Hyun-seok
"""
import numpy as np
import math
import matplotlib.pyplot as plt

def mag(x):
    #Calculates Magnitude (sqrt(x^2+y^2+z^2))
    #Takes list of tuples (x, y, z)
    return math.sqrt(sum(float(i)**2 for i in x))

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

with open('log.txt') as log:
    lines = log.readlines()
    
    rawtime = linesplit(0)
    rawX = linesplit(1)
    rawY = linesplit(2)
    rawZ = linesplit(3)
    
    time = sanitize(rawtime)     
    x = sanitize(rawX)
    y = sanitize(rawY)
    z = sanitize(rawZ)
    
    total = zip(x, y, z) #Creates a list of tuples (x,y,z)
    total2 = zip(x,y,z) #Ibid. Repeat for anytime you do list comprehensions.

    #v is the absolute value of the (magnitude of the data minus 9.81)
    v = [abs(mag(val)-9.81) for val in total]
    
    #m(magnitude) is simply the magnitude of the data
    m = [mag(val) for val in total2]

    #t (transform) is the fast fourier transform of v (google is your friend)
    t = np.fft.fft(np.array(v))

    #deltatime is the length of the experiment (literaly change in time)
    deltatime = float(time[-1]) - float(time[0])

    #Data outputs in the shell
    print ("Delta Time (s): ")
    print (deltatime)
    print ("Area Determined by Trapizoid Method (m/s**3):")
    print (np.trapz(np.array(v)))
    print ("Area Determined by Trapizoid Method/Delta Time (m/s**2): ")
    print ((np.trapz(np.array(v)))/deltatime)
    print ("Mean Value of Data Set: ")
    print (np.mean(np.array(v)))
    print ("Standard Diviation of Data Set: ")
    print (np.std(np.array(v), dtype=np.float64))
    print ("Sum of Graph Range: ")
    print (sum(v))

    #consult matplotlib libraries, esp pyplot.
    plt.figure()

    #subplot 1. The fast fourier transforms graphed on a log scale. Green
    plt.subplot(3, 1, 1)
    plt.semilogy(time, abs(t), 'g')
    plt.axhline(y=0, color='b', linestyle='-') #just a line on y=0 for reference
    plt.ylabel("Amplitude (normalized log scale)")
    plt.xlabel("Frequency (in Hertz)")

    #subplot 2. Variable v graphed on a regular graph. Red
    plt.subplot(3, 1, 2)
    plt.plot(time, v, 'r')
    plt.axhline(y=0, color='b', linestyle='-') #just a line on y=0 for reference
    plt.ylabel("acceleration m/s**2")
    plt.xlabel("time (s)")

    #subplot 3. Variable m graphed on a regular graph. Blue
    plt.subplot(3, 1, 3)
    plt.plot(time, m)
    plt.axhline(y=0, color='b', linestyle='-')
    plt.ylabel("acceleration m/s**2")
    plt.xlabel("time (s)")
    plt.show()

