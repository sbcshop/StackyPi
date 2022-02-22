'''
Project   :- PICO LOGGER 
Developed :- SB-COMPONENTS
Date      :- 16/06/2021
Firmware  :- Demo code  for PICO LOGGER
CODE DISCREPTION :-
                   
'''
import random
import gc9a01
import italicc

import vga1_bold_16x32 as font
import vga1_bold_16x16 as font1

from machine import Pin, SPI ,UART
import sdcard
import os
import utime

spi = SPI(0, baudrate=40000000, sck=Pin(2), mosi=Pin(3))
tft = gc9a01.GC9A01(spi,240,240,reset=Pin(8, Pin.OUT),cs=Pin(5, Pin.OUT),dc=Pin(22, Pin.OUT),backlight=Pin(26, Pin.OUT),rotation=1)
tft.init()
tft.fill(gc9a01.BLACK)
utime.sleep(0.5)
tft.text(font, "RP2040 Round", 20, 50, gc9a01.RED)
tft.text(font, "Display Board 1.28", 20, 80, gc9a01.YELLOW)
tft.text(font, "1.28(240x240)", 20, 120, gc9a01.BLUE)
tft.text(font, "SD card test", 20, 150, gc9a01.GREEN)
utime.sleep(2) 
tft.fill(gc9a01.BLACK)


def sdtest(data):
    spi=SPI(1,sck=Pin(10),mosi=Pin(11),miso=Pin(12))
    sd=sdcard.SDCard(spi,Pin(9))
    vfs = os.VfsFat(sd)
    os.mount(vfs, "/fc")
    print("Filesystem check")
    tft.text(font, "SD", 100, 40, gc9a01.BLUE)
    tft.text(font, "Card detect", 30, 80, gc9a01.YELLOW)
    tft.text(font, "Successfully", 20, 120, gc9a01.RED)
    print(os.listdir("/fc"))

    fn = "/fc/File.txt"
    print()
    print("Single block read/write")
    with open(fn, "a") as f:
        n = f.write(data)
        print(n, "bytes written") 

    with open(fn, "r") as f:
        result2 = f.read()
        print(len(result2), "bytes read")

    os.umount("/fc")

while True:
    sdtest('Hello World!!!!\n')
    utime.sleep(0.5)
