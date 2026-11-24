sudo raspi-config (setup timezone, WLAN country (to enable rfkill))
Activate SSH interface
Activate I2C interface

Setup wifi:
sudo nano /etc/wpa_supplicant/wpa_supplicant.conf
cat /etc/wpa_supplicant/wpa_supplicant.conf

    ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
    update_config=1
    country=FR

    network={
	    ssid="littleking2"
	    psk="xxxxx"
    }

    network={
	    ssid="littleking"
	    psk="xxxxx"
    }

-------
Install Apple File Protocol (AFP) to mount folder:
sudo apt update
sudo apt install netatalk
sudo nano /etc/netatalk/afp.conf

To mount /home, add:
[Homes]
basedir regex = /home

then:
sudo systemctl restart netatalk

From Mac, connect to server:
afp://pi:raspberry@grootcam.local/

GPIOZERO_PIN_FACTORY=pigpio python servoHS645MG.py 6 35021

python ipcsend.py 35021 "go_angle 90"

python eyeled.py 35022

-------------------
External Activity LED:
LED+330 ohm resistor connected to GPIO24 and ground
sudo nano /boot/config.txt
# Redirect activity LED to an external LED connected to GPI24
dtoverlay=pi3-act-led,gpio=24 #pi3
# xor
dtparam=act_led_gpio=24 #pi zero

------------------
cat /boot/config.txt
At the end:
[all]
dtparam=act_led_trigger=actpwr
dtparam=act_led_gpio=24
