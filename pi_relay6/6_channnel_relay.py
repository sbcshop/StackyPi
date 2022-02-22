import utime
from machine import Pin, UART,SPI
from machine import Pin
import time


led_1 = machine.Pin(13, machine.Pin.OUT)#led_1 connected to pico pin 20
led_2 = machine.Pin(14, machine.Pin.OUT)#led_2 connected to pico pin 19
led_3 = machine.Pin(15, machine.Pin.OUT)#led_3 connected to pico pin 18
 


led_1.value(1)#initally led_1 at LOW
led_2.value(1)#initally led_2 at LOW
led_3.value(1)#initally led_3 at LOW


request1 = 0;
flag_1=0;

request2 = 0;
flag_2=0;

request3 = 0;
flag_3=0;

while 1:
    led_1.value(1)#initally led_1 at LOW
    led_2.value(1)#initally led_2 at LOW
    led_3.value(1)#initally led_3 at LOW
    time.sleep(1)
    led_1.value(0)#initally led_1 at LOW
    led_2.value(0)#initally led_2 at LOW
    led_3.value(0)#initally led_3 at LOW
    time.sleep(1)


