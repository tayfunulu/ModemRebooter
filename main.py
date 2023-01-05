from machine import Pin, Signal
import time
import gc
import network
import os
import machine
import wifimgr
import urequests

led = Signal(Pin(13, Pin.OUT, value=1), invert=True)
relay = Pin(12, Pin.OUT, value=0)
button = Pin(0, Pin.IN, Pin.PULL_UP)


def blinking(led, second):

    for i in range(second):
        led.on()
        time.sleep(0.5)
        led.off()
        time.sleep(0.5)


def callback(button):
    print("trigered")
    global wlan
    global led
    global relay
    import os
    import machine

    start = time.ticks_ms()
    while button.value() == 0:
        pass
    pushed = time.ticks_diff(time.ticks_ms(), start)
    if pushed > 5000:
        blinking(led, 4)
        pushed = 0
        print("long pressed")
        try:
            os.rmdir("wifi.dat")
        except:
            print("no file")
        try:
            wlan.disconnect()
        except:
            print("no wifi")
        machine.reset()
    else:
        if relay.value():        
            print("restart modem")
            relay.off()
            led.off()
            time.sleep(10)
        else:
            relay.on()
            led.on()

button.irq(trigger=button.IRQ_FALLING, handler=callback)

relay.on()
print("Relay ON begining ")

blinking(led, 10)

print("10 Second delayed")

connected = True
panic_number = 0

while connected:
    try:
        wlan = wifimgr.get_connection()
        print("Connected")
        connected = False
    except KeyboardInterrupt:
        print("User interrupt")
        machine.reset()
    except:
        print("Not Connected")
        connected = True
        panic_number += 1
        if panic_number > 5:
            print("Rebooting ... ")
            machine.reset()

if wlan is None:
    print("Could not initialize the network connection.")
    while True:
        pass  # you shall not pass :D

print("ESP OK")
cycle_check = 0
reboot_counting = 0
while True:
    try:
        response = urequests.get("http://clients3.google.com/generate_204")
        print(response.status_code)
        if response.status_code == 204:
            print("online")
            led.off()
            cycle_check = 0
            reboot_counting = 0
        elif response.status_code == 200:
            led.on()
            cycle_check += 1
            print("portal :", cycle_check)
        else:
            led.on()
            cycle_check += 1
            print("Offline :", cycle_check)
    except:
        cycle_check += 1
        print("error :", cycle_check)
        led.on()
    try:
        if cycle_check > 4:
            relay.off()
            print("rebooting")
            led.off()
            time.sleep(10)
            relay.on()
            led.on()
            time.sleep(60 * 10)
            cycle_check = 0
            reboot_counting += 1
            print("lets try again :", reboot_counting)
        if reboot_counting > 2:
            print("a few minutes later...")
            for i in range(144):
                time.sleep(60*10)
                print ("still waiting ",round(i/6,1)," hours.")
            cycle_check = 0   
            reboot_counting = 0
                     
        gc.collect()
        time.sleep(60)  # 
    except:
        print("strange ?")
        machine.reset()
