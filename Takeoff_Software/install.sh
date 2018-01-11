#!/bin/bash
sudo apt-get update

# Install accel dependancies
sudo apt-get install python-smbus
sudo apt-get install python3-smbus
sudo pip install RPi.GPIO
sudo pip install cap1xxx

# Install neopixel depenancies
sudo apt-get install build-essential python-dev git scons swig
git clone https://github.com/jgarff/rpi_ws281x.git
cd rpi_ws281x
scons