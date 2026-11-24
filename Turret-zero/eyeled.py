import ipc
import sys
import argparse
import logging
import gpiozero
import hwconf
import led
from logging.handlers import TimedRotatingFileHandler

parser = argparse.ArgumentParser()
parser.add_argument("port_number", type=int, help="IPC Port number")
args = parser.parse_args()

port_number_arg = int(args.port_number)

logging.basicConfig(stream=sys.stdout,format='%(asctime)s %(levelname)s %(message)s',level=logging.DEBUG)

logHandler = TimedRotatingFileHandler(f"logs/eyeled{port_number_arg}.log", when='W0', backupCount=4)
logHandler.setFormatter(logging.Formatter('%(asctime)s %(levelname)s %(message)s'))
logHandler.setLevel(logging.INFO)

log = logging.getLogger(f"Eyeled{port_number_arg}")
log.addHandler(logHandler)
class Eyeled:

    def __init__(self):
        self.__blue = led.Led(hwconf.pin['blue'])
        self.__yellow = led.Led(hwconf.pin['yellow'])
        self.__swap = False
        self.state = "Off"

    def off(self):
        self.state = "Off"
        self.__blue.off()
        self.__yellow.off()

    def wait_for_network(self):
        self.state = "WaitForNetwork"
        self.__blue.blink(0.2, 0.2, True)
        self.__yellow.blink(0.2, 0.2, False)

    def server_error(self):
        self.state = "ServerError"
        self.__blue.blink(1.0, 0.5)
        self.__yellow.blink(1.0, 0.5)

    def led_swap(self):
        self.state = "LedSwap"
        self.__swap = not self.__swap
        if (self.__swap):
            self.__blue.blink(10.0, 0.5)
            self.__yellow.off()
        else:
            self.__blue.off()
            self.__yellow.blink(10.0, 0.5)

eyeled = Eyeled()

# States: Off, WaitForNetwork (exception in request), WaitForServer (http code not 200), LedSwap
def processor(command):
    log.info(f"Eyeled: processing command: {command}")
    tab = command.split()

    if (command=="Off" and eyeled.state != "Off"):
        eyeled.off()
    elif (command=="WaitForNetwork" and eyeled.state!="WaitForNetwork"):
        eyeled.wait_for_network()
    elif (command=="ServerError" and eyeled.state!="ServerError"):
        eyeled.server_error()
    elif (command=="LedSwap"):
        eyeled.led_swap()

    else:
        return False
    return True

log.info(f"Starting Eyeled - Listening commands on port {port_number_arg}")
ipc.listen(port_number_arg, processor)
