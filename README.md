# StackyPi
<img src= "https://github.com/sbcshop/StackyPi/blob/main/images/Capture.JPG" />

## StackyPi is a compact and advanced board that is designed with the RP2040 Micro-controller, which provides one set of 2x20 pin headers on which you can connect Raspberry Pi HATs. It means that one can plug HAT designed for Raspberry Pi and run it via the Pico Zero RP2040 that would make the user perform the advanced functions on it.

## StackyPi consists of standard Raspberry Pi 40 pins on its board for Raspberry Pi HAT. One can plug Raspberry Pi HAT by directly putting it on the StackyPi that has the power pins for the connection. StackyPi is a board on which, clear and descriptive pin labels make the process easier for the user.

<img src= "https://github.com/sbcshop/StackyPi/blob/main/images/img4.png" />

## Pin Out Of StackyPi
<img src= "https://github.com/sbcshop/StackyPi/blob/main/images/img6.png" />
<img src= "https://github.com/sbcshop/StackyPi/blob/main/images/img.JPG" />

## On board Status led of stackypi is connected with GP25 Pin
## Already we install the micropython on StackyPi

## Pin Out Of SD Card Module
<img src= "https://github.com/sbcshop/StackyPi/blob/main/images/img1.JPG" />

## There are various folder you see:-
  * **lcd_display_1.3_inch** - this folder have two files
    * **1._3_lcd_display.p**y - demo code of 1.3 lcd display
    * **firmware.uf2** - This is the firmware of lcd display.press boot button then plug usb to pc then release button ,you need to drag and drop the firmware to stackypi 
  * **lora_home_automation** -  this folder have one file
    * **homeautomation.py** - Run this file to control home appliances
  * **lora_receiver** - this folder have two files
    * **lora_receiver.py** - receiver code
    * **firmware.uf2** -  lcd display firmware
  * **pi_relay6** - this folder have one file
    * **6_channnel_relay.py** - Run this file to control relay
  * **relay4_zero** - this folder have one file
    * **relay_4_zero.py** - Run this file to control relay zero
  * **rfid_hat** - this folder have two files
    * **rfid_hat.py** - Run this file to read rfid cards
    * **ssd1306.py** - this is the library of oled display, save this file to stackypi 
  * **round_lcd_1.28_hat** - this folder have two files
    * **round_lcd_1_28.py** - demo code of 1.28 round lcd display
    * **firmware.uf2** - This is the firmware of round lcd display, drag and drop the firmware to stackypi 
  * **sd_card** - this folder have three files
    * **sdcard.py** - This is the library of sdcard onboard sd card module, save this file to stackypi 
    * **firmware.uf2** - This is the firmware of round lcd display, drag and drop the firmware to stackypi
    * **main.py** - you need to run this file to read/write sd card
  * **led_cube** - inside this folder there is a file name "led_cube.py",run this file before this mount picube on the StackyPi
  
## Getting Started of StackyPi
https://www.youtube.com/watch?v=EEsRHvAQ-30



