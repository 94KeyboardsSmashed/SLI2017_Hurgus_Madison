The files to are to be put on the raspberry pi. 

For simple demonstrations without websocket compatibility do sudo python3 raspi_loud_ex.py on the shell.

For demonstrations with websocket compatibility do sh run_deomonstration.sh and that should run the commands necessary for that stuff.
raspi_accel_lib.py and raspi_neopixel.py are just libraries that suppliment the nessesary files.
Additional information needed:

ssh tunneling information
ssh -L 8080:localhost:8080 pi@temeraire
