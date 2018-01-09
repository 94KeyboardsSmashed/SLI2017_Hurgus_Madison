# -*- coding: utf-8 -*-
"""
Created on Tue May  9 12:13:27 2017

@author: Hyun-seok
"""
import math
import numpy as np
import matplotlib.pyplot as plt

#Have log.txt in the same folder as this code.
#Name of log has to be same as name in the open function
def _mag(readings):
    """Calculates Magnitude (sqrt(x^2+y^2+z^2)). Takes list of tuples (x, y, z)"""
    return math.sqrt(sum(float(values)**2 for values in readings))

with open('log.txt') as log:
    raw_time = []
    raw_x = []
    raw_y = []
    raw_z = []
    for line in log:
        li = line.strip()
        if not line.strip().startswith("#"):
            raw_time.append(line.split(",")[0])
            raw_x.append(line.split(",")[1])
            raw_y.append(line.split(",")[2])
            raw_z.append(line.split(",")[3])

time = [values.rstrip() for values in raw_time]
x = [values.rstrip() for values in raw_x]
y = [values.rstrip() for values in raw_y]
z = [values.rstrip() for values in raw_z]

total = zip(x, y, z) #Creates a list of tuples (x,y,z)
total2 = zip(x, y, z) #Ibid. Repeat for anytime you do list comprehensions.

#v is the absolute value of the (magnitude of the data minus 9.81)
v = [abs(_mag(val)-9.81) for val in total]

#m (magnitude) is simply the magnitude of the data
m = [_mag(val) for val in total2]

#t (transform) is the fast fourier transform of v (google is your friend)
t = np.fft.fft(np.array(v))

#deltatime is the length of the experiment (literaly change in time)
deltatime = float(time[-1]) - float(time[0])

#Data outputs in the shell
print("Delta Time (s): ")
print(deltatime)
print("Area Determined by Trapizoid Method (m/s**3):")
print(np.trapz(np.array(v)))
print("Area Determined by Trapizoid Method/Delta Time (m/s**2): ")
print((np.trapz(np.array(v)))/deltatime)
print("Mean Value of Data Set: ")
print(np.mean(np.array(v)))
print("Standard Diviation of Data Set: ")
print(np.std(np.array(v), dtype=np.float64))
print("Sum of Graph Range: ")
print(sum(v))

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
plt.axhline(y=0, color='b', linestyle='-') #just a line on y=0 for reference
plt.ylabel("acceleration m/s**2")
plt.xlabel("time (s)")
plt.show()
