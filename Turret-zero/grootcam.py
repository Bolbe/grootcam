import requests
import ipc
import sys
import logging
import gpiozero
import time
import hwconf
import signal
import credentials
from logging.handlers import TimedRotatingFileHandler

logging.basicConfig(stream=sys.stdout,format='%(asctime)s %(levelname)s %(message)s',level=logging.DEBUG)

logHandler = TimedRotatingFileHandler(f"logs/grootcam.log", when='W0', backupCount=4)
logHandler.setFormatter(logging.Formatter('%(asctime)s %(levelname)s %(message)s'))
logHandler.setLevel(logging.INFO)

log = logging.getLogger(f"Grootcam")
log.addHandler(logHandler)
log.info(f"Starting Grootcam...")

class Grootcam:

    def __init__(self):
        self.angle = 180
        self.activitySwitch = gpiozero.Button(hwconf.pin['switch'])
        self.running = False
        self.activitySwitch.when_pressed = self.activityOff
        self.activitySwitch.when_released = self.activityOn
        self.sync()

    def activityOff(self):
        ipc.send(35022, "Off")
        ipc.send(35023, "Off")

    def activityOn(self):
        ipc.send(35023, "On")
        ipc.send(35022, "WaitForNetwork")
        self.angle = 180
        self.sync()

    def sync(self):
        self.running = True
        while self.activitySwitch.value == 0:
            # swap eye leds.
            print(f"Requesting angle with myangle={self.angle}")
            ts = time.time()
            try:
                response = requests.get(f"http://www.micromegas.ovh/grootcam/angle.php?myangle={self.angle}", auth=(credentials.user, credentials.passwd))
                elapsed = time.time()-ts
                print(f"Response time: {elapsed}")
                if (response.status_code==200):
                    angle = int(response.text.split('|')[0])
                    print(f"Angle received: {angle}")
                    ipc.send(35022, "LedSwap")
                    if (self.angle!=angle):
                        self.angle = angle
                        ipc.send(35021, f"go_angle {angle}")
                else:
                    ipc.send(35022, "ServerError")
            except:
                log.error("Network exception.")
                ipc.send(35022, "WaitForNetwork")

            if (elapsed<2):
                time.sleep(2)

        self.running = False
        # turn off leds
        if (self.activitySwitch.value==1):
            ipc.send(35022, "Off")
            ipc.send(35023, "Off")

grootcam = Grootcam()
signal.pause()

