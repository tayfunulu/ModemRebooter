# ModemRebooter
## SONOFF S20/S26 - Internet Checker and automatic model rebooter with micropython

**Device :** [SONOFF S20 / S26](https://sonoff.tech/product/smart-plugs/s26/) <br>
**Device for connection :** FT232RL TTL USB Serial Port Adapter <br>
**Hacking :** [Hacking Sonoff S26 WiFi Smart Plug](https://notenoughtech.com/home-automation/hacking-sonoff-wifi-smart-plug/) <br>


**WARNING : NEVER POWER YOUR DEVICE WITH POWERLINE**

1. Step: Correct wiring between SONOFF device and USB serial Port adapter
2. Step: Be sure 3.3 Volt selected on FTL USB serial port adaper
4. Step: install [esptool](docs.micropython.org/en/latest/esp8266/tutorial/intro.html) 
      - install esptool 
      - powered device only with USB serial adapter with holding button on device to enter boot mode 
      - erase device and load newest micropython code on device ( 1 MB ESP8266 code)  

      ```sh
      pip install esptool
      esptool.py --port /dev/ttyUSB0 erase_flash
      sudo esptool.py --port /dev/ttyUSB0 --baud 460800 write_flash --flash_size=detect -fm dio 0  esp8266-1m-20220618-v1.19.1
      ```
      
Upload codes (All .py files) on device with your favorite method. Mine is RSHELL. 

```
sudo pip3 install rshell
sudo rshell --buffer-size=30 -p /dev/ttyUSB0
rsync . /pyboard
```


## Algorithm





<b>Source :</b> 

  * [WiFiManager](https://github.com/tayfunulu/WiFiManager)
  * [Monitoring internet connection  - Jorge Alberto Díaz Orozco (Akiel)](https://dev.to/jadolg/monitoring-my-internet-connection-with-micropython-and-esp8266-42lp)
