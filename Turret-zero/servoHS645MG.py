import ipc
import sys
import argparse
import logging
import gpiozero
import threading
from logging.handlers import TimedRotatingFileHandler

# servos needs to be controlled by a specific process because they are started with GPIOZERO_PIN_FACTORY=pigpio env variable

parser = argparse.ArgumentParser()
parser.add_argument("pin", help="Pin number to which the servo is connected")
parser.add_argument("port_number", type=int, help="Port number")
args = parser.parse_args()

port_number_arg = int(args.port_number)
pin_arg = int(args.pin)

logging.basicConfig(stream=sys.stdout,format='%(asctime)s %(levelname)s %(message)s',level=logging.DEBUG)

logHandler = TimedRotatingFileHandler(f"logs/servo{port_number_arg}.log", when='W0', backupCount=4)
logHandler.setFormatter(logging.Formatter('%(asctime)s %(levelname)s %(message)s'))
logHandler.setLevel(logging.INFO)

log = logging.getLogger(f"Servo{port_number_arg}")
log.addHandler(logHandler)
class Servo:

    def __init__(self, pin):
        self.__pin = pin
        self.__servo = gpiozero.AngularServo(self.__pin, initial_angle=None, min_angle=-97, max_angle=96, min_pulse_width=0.0005, max_pulse_width=0.0026)
        self.__timer = None
        

    def detach_servo(self):
        log.info(f"Detach")
        if (self.__timer!=None):
            self.__timer.cancel()
            self.__timer = None
        self.__servo.detach()

    def go_angle(self, angle, duration=3):
        log.info(f"Go angle {angle}")
        if (duration > 0):
            log.info(f"Detach servo in {duration} seconds.")
            if (self.__timer!=None):
                self.__timer.cancel()
            self.__timer = threading.Timer(duration, self.detach_servo)
            self.__timer.start()
        self.__servo.angle = angle

servo = Servo(pin_arg)

def processor(command):
    log.info(f"servoHS645MG: processing command: {command}")
    tab = command.split()

    if (command=="detach"):
        servo.detach_servo()
    elif (tab[0]=="go_angle"):
        servo.go_angle(int(tab[1]))
    else:
        return False
    return True

log.info(f"Starting servo HS645MG on pin {pin_arg} - Listening commands on port {port_number_arg}")

ipc.listen(port_number_arg, processor)
