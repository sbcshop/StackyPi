#Receiver code
import utime
from machine import Pin, UART,SPI
from machine import Pin
import time

lora = UART(0,baudrate = 9600,tx = Pin(0),rx = Pin(1))

led_1 = machine.Pin(13, machine.Pin.OUT)#led_1 connected to pico pin 20
led_2 = machine.Pin(14, machine.Pin.OUT)#led_2 connected to pico pin 19
led_3 = machine.Pin(15, machine.Pin.OUT)#led_3 connected to pico pin 18

led_1.value(0)#initally led_1 at LOW
led_2.value(0)#initally led_2 at LOW
led_3.value(0)#initally led_3 at LOW

request1 = 0;
flag_1=0;

request2 = 0;
flag_2=0;

request3 = 0;
flag_3=0;

while True:
    data_Read = lora.readline(3)#read data comming from other pico lora expansion
 
    if data_Read is not None and "A" in data_Read:
      #ones, turn led on!
      if flag_1 == 0:
        print("relay 1 on")
        led_1.value(1)
        flag_1=1; #change flag variable
        
        
      #twice, turn led off!
      elif flag_1 == 1:
        print("relay 1 off")
        led_1.value(0)
        flag_1=0; #change flag variable again
        
        
    if data_Read is not None and "B" in data_Read:
      #ones, turn led on!
      if flag_2 == 0:
        print("relay 2 on")
        led_2.value(1)
        flag_2=1; #change flag variable
        
      #twice, turn led off!
      elif flag_2 == 1:
        print("relay 2 off")
        led_2.value(0)
        flag_2=0; #change flag variable again
        
        
    if data_Read is not None and "C" in data_Read:
      #ones, turn led on!
      if flag_3 == 0:
        print("relay 3 on")
        led_3.value(1)
        flag_3=1; #change flag variable
        
      #twice, turn led off!
      elif flag_3 == 1:
        print("relay 3 off")
        led_3.value(0)
        flag_3=0; #change flag variable again
        
    utime.sleep(0.2)#wait for 200ms
    
    
 
