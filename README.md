# Raspberry-Pi-PWM-fan
Based on [DriftKingTW's instructable.](https://github.com/DriftKingTW/Raspberry-Pi-PWM-Fan-Control) 

I use a 25mm 5V 0,2A fan.

[The circuit needed to drive it](https://github.com/AstaRom/RPi-PWM-Fan-Control/raw/main/fan_circuit%20%5Bpwm%5D.png)
* 5V, GND and GPIO inputs (from left to right)
* 1kOhm resistor
* 2N2222 NPN transistor
* 1N4001 diode
* 5V and GND output for the fan (from left to right)

# Setting to use:

Install the RPi.GPIO package :

`sudo apt-get install rpi.gpio`

Download the script file from the repository:

`wget https://raw.githubusercontent.com/AstaRom/RPi-PWM-Fan-Control/main/fan_control.py`

Move the script to '/usr/local/bin', which is the ideal location for scripts.

`sudo mv fan_control.py /usr/local/bin/`  
`sudo chmod +x /usr/local/bin/fan_control.py`

Download the shell script file:

`wget https://raw.githubusercontent.com/AstaRom/RPi-PWM-Fan-Control/main/fan_control.sh`

Move this file to '/etc/init.d', and make it executable:

`sudo mv fan_control.sh /etc/init.d/`  
`sudo chmod +x /etc/init.d/fan_control.sh`

Now we'll register the script to run on boot:

`sudo update-rc.d fan_control.sh defaults`

Now, you can either restart your machine, or kick this off manually since it won't already be running:

`sudo reboot` or `sudo /etc/init.d/fan_control.sh start`
