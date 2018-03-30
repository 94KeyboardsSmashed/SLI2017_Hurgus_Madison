#!/bin/bash
#sudo nice -20 python3 run_demo.py > logdemo.txt & websocketd --port=8080 --staticdir=./static tail -f logdemo.txt
sudo websocketd --port=8080 --staticdir=./static sudo python3 run_demo.py

