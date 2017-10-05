#!/bin/bash
#Run this script when using websockets
sudo nice -20 python3 raspi_quiet_ex.py > log.txt & websocketd --port8080 --staticdir=./static tail -f log.txt