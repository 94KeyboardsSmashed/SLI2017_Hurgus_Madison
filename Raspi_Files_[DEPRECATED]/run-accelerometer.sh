#!/bin/bash
sudo nice -20 python3 ADXL345_Read.py > log.txt & websocketd --port=8080 --staticdir=./static tail -f log.txt & sudo python3 AmplitudeConversion.py
