import random
from machine import Pin, SPI
import gc9a01

import utime
import italicc

import vga1_bold_16x32 as font

#------joystck pin declaration----- 



def main():
    spi = SPI(0, baudrate=40000000, sck=Pin(2), mosi=Pin(3))
    tft = gc9a01.GC9A01(spi,240,240,reset=Pin(8, Pin.OUT),cs=Pin(5, Pin.OUT),dc=Pin(22, Pin.OUT),backlight=Pin(26, Pin.OUT),rotation=1)

    tft.init()
    tft.rotation(3)
    tft.fill(gc9a01.BLACK)
    utime.sleep(0.5)
    tft.text(font, "Round lcd hat", 20, 50, gc9a01.RED)
    tft.text(font, "1.28(240x240)", 20, 100, gc9a01.YELLOW)
    tft.text(font, "Hello World!!", 20, 150, gc9a01.GREEN)
    #tft.draw(italicc, "hello" , 100, 50, gc9a01.BLUE)
    #tft.fill_rect(120,120,200,200, gc9a01.BLUE)
    #tft.pixel(100, 50, gc9a01.BLUE)
    


main() 
