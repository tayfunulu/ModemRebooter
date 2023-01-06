# ModemRebooter
## SONOFF S20/S26 - Internet Checker and automatic model rebooter with micropython

Some modems and some service providers do not have a stable internet connection and sometimes the internet connection is randomly disconnected. In such cases, the best solution is to restart the modem. It is an important problem especially for people who remotely connect to devices at home. 

My friend Mr. Cenap came to me with a similar problem. I prepared this product and small codes for him. I preferred to use a sonoff's smart plug to make it tidy. In this way, it was both a safe and visually better... 

![image](https://user-images.githubusercontent.com/11840582/210970263-f4bdb6d9-734b-406d-ac57-4675051ff585.png)


**Device :** [SONOFF S20 / S26](https://sonoff.tech/product/smart-plugs/s26/) <br>
**Device for serial connection :** FT232RL TTL USB Serial Port Adapter <br>
**Hacking :** [Hacking Sonoff S26 WiFi Smart Plug](https://notenoughtech.com/home-automation/hacking-sonoff-wifi-smart-plug/) <br>

**Not:** you could easily make your own circuit. All you need is that a microcontroller like ESP or Pico and a Relay element. 

**WARNING : NEVER POWER YOUR DEVICE WITH POWERLINE DURING ALL PROCESS**

1. Step: To make correct wiring between SONOFF device and USB serial Port adapter
      <code>GND-GND</code> , <code>VCC-VCC</code> , <code>RX-TX</code> , <code>TX-RX</code> 
2. Step: Be sure to use 3.3 Volt: Probably there is small jumper on your FTL USB serial port adaper
4. Step: install [esptool](docs.micropython.org/en/latest/esp8266/tutorial/intro.html) 
      - install esptool on PC
      - powered device only with USB serial adapter with holding button on device to enter boot mode 
      - erase device and upload newest micropython code on device ( 1 MB ESP8266 code)  

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

![image](https://user-images.githubusercontent.com/11840582/210970394-09c92544-9e2c-4604-aac5-32532961feaf.png)


## Algorithm

![image](https://user-images.githubusercontent.com/11840582/210866834-43f840b3-9553-460b-89e7-90c3922bffce.png)


## Button Functions

one short press = rebooting 
5 sec long press  = delete stored wifi datas and disconnect (like factory reset)


<b>Source :</b> 

  * [WiFiManager](https://github.com/tayfunulu/WiFiManager)
  * [Monitoring internet connection  - Jorge Alberto Díaz Orozco (Akiel)](https://dev.to/jadolg/monitoring-my-internet-connection-with-micropython-and-esp8266-42lp)
