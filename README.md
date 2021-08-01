# Raspberry Pi 4 Case Fan Temperature Control Script

This script toggles the [Raspberry Pi 4 Case Fan](https://www.raspberrypi.org/products/raspberry-pi-4-case-fan/) on/off depending on the CPU temperature.

It has a 5C "buffer" which means once the CPU reaches the high temperature threshold and the fan toggles ON, the fan won't toggle OFF until after the CPU temperature is at least 5C lower than the high-temp threshold.

## Installation

Install python3 and [gpiozero](https://gpiozero.readthedocs.io/en/stable/installing.html).  
For Ubuntu: `sudo apt install python3 python3-gpiozero`

Optional: Change "HIGH_TEMP" and/or "DELAY_SEC" in "case_fan.py". "HIGH_TEMP" is the temperature threshold that will toggle the fan on. "DELAY_SEC" is how often the script will check the CPU temperature.

Correct entries in "case-fan.service":  
* "ExecStart" needs to point to "case_fan.sh".  
* "WorkingDirectory" needs to point to the directory the files are placed in.  
* "User" should be equal to your username.

Change owner of "case-fan.service" to root user: `sudo chown root case-fan.service`  
Copy "case-fan.service" to "/etc/systemd/system": `sudo cp case-fan.service /etc/systemd/system`

Reload systemd daemons: `sudo systemctl daemon-reload`  
Start the service: `sudo systemctl start case-fan`  
Check status of the service: `sudo systemctl status case-fan`  
Enable the service (so it will start on boot): `sudo systemctl enable case-fan`
