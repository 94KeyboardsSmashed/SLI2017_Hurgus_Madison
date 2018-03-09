#!/bin/bash

# A program to run the demo on bootup.
# For more info visit see section "works on bootup to the console"
# in following link:
# https://raspberrypi.stackexchange.com/questions/8734/execute-script-on-start-up
# Basically puut it in the ect/init.d/ directory
# and make it executable with "sudo chmod 755 /etc/init.d/boot_demo.sh"
# then do "sudo update-rc.d boot_demo.sh defaults"
# That should make it run at start-up by default and not have to fiddle around with networks

cd ~
cd SLI2017_Hurgus_Madison/Raspi_files
sudo nice -20 python3 raspi_quiet_ex.py > log.txt & websocketd --port=8080 --staticdir=./static tail -f log.txt