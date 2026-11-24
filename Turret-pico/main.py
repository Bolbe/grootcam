import time
import network
import urequests
import machine
import conf

pwm = machine.PWM(machine.Pin(0))
pwm.freq(50)

print('Starting...')
# LED
led = machine.Pin("LED", machine.Pin.OUT)
led.on()
time.sleep(0.5)
led.off()

blue = machine.Pin(15, machine.Pin.OUT)
yellow = machine.Pin(14, machine.Pin.OUT)

yellow.off()
blue.on()

def set_servo_angle(angle):
    if angle<-90 or angle>90:
        return
    print(f"Setting servo to angle {angle}")
    position = int(2000+((angle+90)*6500/180))
    pwm.duty_u16(position)
    time.sleep(2)
    pwm.duty_u16(0)

def blinkled(timer):
    yellow.toggle()
    blue.toggle()

def wifi_connect():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(conf.wifi['ssid'], conf.wifi['passwd'])
    credential_index = 0
    while wlan.isconnected() == False:
        ssid = conf.wifi[credential_index]['ssid']
        passwd = conf.wifi[credential_index]['passwd']
        print(f"Trying to connect {ssid}")
        time.sleep(1)
        led.toggle()
        credential_index = (credential_index+1) % conf.wifi.length # +1, reset if overflow
    ip = wlan.ifconfig()[0]
    print(f'Connected on {ip}')
    time.sleep(2)
    led.on()
    
def groot_is_bored():
    print("Groot is bored")
    set_servo_angle(-90)
    set_servo_angle(90)
    set_servo_angle(0)

ledtimer = machine.Timer()
ledtimer.init(period=250, mode=machine.Timer.PERIODIC, callback=blinkled)
wifi_connect()
ledtimer.deinit()
current_angle = 0
set_servo_angle(0)

bored_ref = time.time()

while True:
    # Groot is bored after 30 min = 1800 s
    use_time = time.time()-bored_ref
    if (use_time>1800):
        bored_ref = time.time()
        groot_is_bored()
        current_angle = 0
        
    # Request angle
    print(f"Requesting angle with myangle={current_angle}")
    ts = time.time()
    r = urequests.get(f"{conf.url}/angle.php?myangle={current_angle}")
    elapsed = time.time()-ts
    print(f"Response time: {elapsed}")
    print(r.text)
    a = int(r.text.split('|')[0])
    print(f"Angle received: {a}")
    if a>=-90 and a<=90:
        current_angle = a
        blinkled(None)
        set_servo_angle(current_angle)
        
