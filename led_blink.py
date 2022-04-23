from machine import Pin, Timer
led = Pin(25, Pin.OUT)
import time
while True:
    led.value(1)
    time.sleep(1)
    led.value(0)
    time.sleep(1)