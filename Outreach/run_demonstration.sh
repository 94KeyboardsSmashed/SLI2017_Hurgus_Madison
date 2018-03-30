#!/bin/bash
#Run this script when using websockets
sudo nice -20 python3 /home/pi/SLI2017_Hurgus_Madison/Raspi_Files/raspi_run2.py > /home/pi/SLI2017_Hurgus_Madison/Raspi_Files/log.txt & websocketd --port=8080 --staticdir=/home/pi/SLI2017_Hurgus_Madison/Raspi_Files/static tail -f /home/pi/SLI2017_Hurgus_Madison/Raspi_Files/log.txt
