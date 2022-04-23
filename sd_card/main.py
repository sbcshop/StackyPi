'''
Project   :- PICO LOGGER 
Developed :- SB-COMPONENTS
Date      :- 16/06/2021
Firmware  :- Demo code  for PICO LOGGER
CODE DISCREPTION :-
                   
'''
import random
from machine import Pin, SPI ,UART
import sdcard
import os
import utime


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
