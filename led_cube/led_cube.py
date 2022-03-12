from machine import Pin
import time
import random

LAYER = [15,16,17,18]#layers

#columns
GRID_3D = [[6, 7, 13, 14], 
           [28, 8, 11, 12],
           [9, 27, 2, 10],
           [26, 3, 4, 22]]


def enable_layer(layer):
    a = Pin(LAYER[layer])
    a.on()

def disable_layer(layer):
    a = Pin(LAYER[layer])
    a.off()

def light_on(y,x, z,):
    enable_layer(y)
    a = Pin(GRID_3D[x][z])
    a.on()
    
def light_off(y, x, z):
    enable_layer(y)
    a = Pin(GRID_3D[x][z])
    a.off()
    

def reset(t):
    for x in range(4):
        for z in range(4):
            a = Pin(GRID_3D[x][z])
            a.off()
            time.sleep(t)
            
def resetlayer():
    for i in range(0,4):
        a = Pin(LAYER[i])
        a.off()
        time.sleep(0.01)

for pin in LAYER:
    Pin(pin, Pin.OUT)

for x in range(4):
    for z in range(4):
        Pin(GRID_3D[x][z], Pin.OUT)




def pattern_1(): #slowly all bulb turn on ahen slowly all bulb turn off
    for i in range(4):
        for j in range(4):
            light_on(i,i,j)
            time.sleep(0.1)
    reset(0)
    
    for i in reversed(range(4)):
        for j in reversed(range(4)):
            light_on(i,i,j)
            time.sleep(0.1)
    reset(0)


def pattern_2():
    for j in range(4):
            for k in range(4):
                light_on(j,j,k)
            time.sleep(0.1)

    for j in range(4):
            for k in range(4):
                light_off(j,j,k)
            time.sleep(0.1)
            
x = 0         
def pattern_3():
    x = 0 
    for i in range(3):
        light_on(x,0,i)
        time.sleep(0.1)
        reset(0)
           
    for j in range(4):
        light_on(x,j,3)
        time.sleep(0.1)
        reset(0)
       
    for k in reversed(range(3)):
        light_on(x,3,k)
        time.sleep(0.1)
        reset(0)

    for l in reversed(range(3)):
        light_on(x,l,0)
        time.sleep(0.1)
        reset(0)
        
    disable_layer(x)    
    x +=1 
    if x > 3:
        x =0

def pattern_4():
    x = 0
    for i in range(4):
        for j in range(4):
            light_on(x,i,j)
    time.sleep(0.15)
    resetlayer()
    reset(0)
    
    x +=1 
    if x > 3:
        x =0

def pattern_5():
    u = 0.2
    for i in range(4):
            light_on(i,0,i)
    time.sleep(u)
    reset(0)
               
    for j in range(4):
            light_on(j,j,3)
    time.sleep(u)
    reset(0)
           
    for k in reversed(range(4)):
            light_on(k,3,k)
    time.sleep(u)
    reset(0)

    for l in reversed(range(4)):
            light_on(l,l,0)
    time.sleep(u)
    reset(0)
            

def pattern_6():
    for i in reversed(range(4)):
        for j in reversed(range(4)):
            light_on(i,j,i)
            time.sleep(0.02)
            disable_layer(i)
    reset(0)        
    for i in range(4):
        for j in range(4):
            light_on(i,j,i)
            time.sleep(0.02)
            disable_layer(i)

def pattern_7():
    for i in reversed(range(4)):
            for j in reversed(range(4)):
                light_on(0,j,i)
                time.sleep(0.02)
                disable_layer(i)
                
    reset(0)            
    for i in range(4):
            for j in reversed(range(4)):
                light_on(1,j,i)
                time.sleep(0.02)
                disable_layer(i)
    reset(0)            
    for i in reversed(range(4)):
            for j in reversed(range(4)):
                light_on(2,j,i)
                time.sleep(0.02)
                disable_layer(i)
                
    reset(0)            
    for i in range(4):
            for j in reversed(range(4)):
                light_on(3,j,i)
                time.sleep(0.02)
                disable_layer(i)
      
def pattern_8():
    for i in range(4):
            for j in range(4):
                light_on(0,i,j)
             
    for i in range(4):
            for j in range(4):
                light_on(3,i,j)
         
    time.sleep(0.3)
    disable_layer(0)
    disable_layer(3)
    reset(0) 

    for i in range(4):
            for j in range(4):
                light_on(1,i,j)
                #time.sleep(0.02)
                #disable_layer(i)
    for i in range(4):
            for j in range(4):
                light_on(2,i,j)
                
    time.sleep(0.3)
    disable_layer(1)
    disable_layer(2)

def pattern_9():
    for i in range(4):
                for j in range(4):
                    light_on(0,i,j)
                 
    for i in range(4):
                for j in range(4):
                    light_on(1,i,j)
             
    time.sleep(0.3)
    disable_layer(0)
    disable_layer(1)
    reset(0) 

    for i in range(4):
                for j in range(4):
                    light_on(2,i,j)
                    #time.sleep(0.02)
                    #disable_layer(i)
    for i in range(4):
                for j in range(4):
                    light_on(3,i,j)
                    
    time.sleep(0.3)
    disable_layer(2)
    disable_layer(3)
        
        
def pattern_10():       
    for i in range(4):
            for j in range(4):
                 for k in range(4):
                    light_on(i,j,k)
    time.sleep(1)
    for i in range(4):
            for j in range(4):
                 for k in range(4):
                    light_off(i,j,k)
                 time.sleep(0.1)
while 1:
    for i in range(5):
          pattern_1()
          
    for i in range(5):      
          pattern_2()
          
    for i in range(5):
          pattern_3()
          
    for i in range(5):      
          pattern_4()
          
    for i in range(5):
          pattern_5()
          
    for i in range(5):
          pattern_6()
          
    for i in range(5):
          pattern_7()
          
    for i in range(5):
          pattern_8()
          
    for i in range(5):
          pattern_9()
          
    for i in range(5):
          pattern_10()


