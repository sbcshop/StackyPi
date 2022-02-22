#Receiver code
import utime
from machine import Pin, UART,SPI
import time
import st7789

import vga1_8x16 as font1
#import vga2_8x8 as font
import vga1_16x32 as font                                                                             

import vga1_16x16 as font2

spi = SPI(0, baudrate=40000000, sck=Pin(2), mosi=Pin(3))
tft = st7789.ST7789(spi,240,240,reset=Pin(18, Pin.OUT),cs=Pin(5, Pin.OUT),dc=Pin(22, Pin.OUT),backlight=Pin(26, Pin.OUT),rotation=1)

lora = UART(0,baudrate = 9600,tx = Pin(0),rx = Pin(1))

def info():
    tft.init()
    utime.sleep(0.2)
    tft.text(font,"SB-COMPONENTS", 15,20)
    tft.fill_rect(15, 60, 210,10, st7789.RED)
    
    tft.text(font,"1.3 LCD HAT", 15,100,st7789.YELLOW)
    tft.fill_rect(15, 140, 210, 10, st7789.BLUE)
    time.sleep(2)
    tft.fill(0) #clear screen
    

    
info()

while True:
    tft.text(font,"RECIVER", 60,20)
    tft.fill_rect(15, 60, 210,10, st7789.RED)
    data_Read = lora.readline()#read data comming from other pico lora expansion
    print(data_Read)
    if data_Read is not None:
        
            tft.text(font,data_Read, 5,100,st7789.WHITE)
            print(data_Read)
            time.sleep(2)
            tft.fill(0) #clear screen
            
        #if data_Read is not None and "A" in data_Read:
    utime.sleep(0.2)#wait for 200ms
    
    
 

