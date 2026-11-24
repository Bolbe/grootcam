import gpiozero
import threading

class Led():

    def __init__(self, pin):
        self.__led = gpiozero.LED(pin)
        self.__durationOn = 0 # if 0, then led always off
        self.__durationOff = 0 # if 0, then led always on
        self.__led.off()
        self.__timer = None

    def __cancel_timer(self):
        if self.__timer:
            self.__timer.cancel()
            self.__timer = None

    def __on(self):
        self.__cancel_timer()
        self.__led.on()
        if self.__durationOn > 0:
            self.__timer = threading.Timer(self.__durationOn, self.__off)
            self.__timer.start()

    def __off(self):
        self.__cancel_timer()
        self.__led.off()
        if self.__durationOff > 0:
            self.__timer = threading.Timer(self.__durationOff, self.__on)
            self.__timer.start()

    def blink(self, durationOn=0.5, durationOff=0.5, startOn = True):
        self.__durationOn = durationOn
        self.__durationOff = durationOff
        if (startOn):
            self.__on()
        else:
            self.__off()

    def on(self):
        self.__durationOn = 0
        self.__on()

    def off(self):
        self.__durationOff = 0
        self.__off()

