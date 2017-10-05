#!/bin/bash

sudo nice -20 python3 raspi_quiet_ex.py > log.txt & websocketd --port=8080 --staticdir=./static tail -f log.txt

function finish {
  # Cleanup code. Runs raspi_cleanup_ex.py
  sudo python3 raspi_cleanup_ex.py
}

trap finish EXIT