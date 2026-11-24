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

logHandler = TimedRotatingFileHandler(f"logs/TrunkLed{port_number_arg}.log", when='W0', backupCount=4)
logHandler.setFormatter(logging.Formatter('%(asctime)s %(levelname)s %(message)s'))
logHandler.setLevel(logging.INFO)

log = logging.getLogger(f"TrunkLed{port_number_arg}")
log.addHandler(logHandler)

led1 = led.Led(hwconf.pin['trunk'])
led1.on()

def processor(command):
    log.info(f"TrunkLed: processing command: {command}")

    if command=="Off":
        led1.off()
    elif command=="On":
        led1.on()
    else:
        return False
    return True

log.info(f"Starting TrunkLed - Listening commands on port {port_number_arg}")
ipc.listen(port_number_arg, processor)
