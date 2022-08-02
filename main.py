import time
import restlist
import random
from machine import I2C, Pin
from pico_i2c_lcd import I2cLcd
i2c = I2C(0, sda=Pin(0), scl=Pin(1), freq=400000)


sleep = time.sleep

pullist = []
#This is the list that the final restaraunt will be picked from


#Three random choices from the big list are put into a smaller list (pullist)
#and then one is randomly selected from the pullist because I felt like the same
#results kept coming up over and over and I wanted more randomization
add = (random.choice(restlist.rests))
pullist.append(add)
add = (random.choice(restlist.rests))
pullist.append(add)
add = (random.choice(restlist.rests))
pullist.append(add)

I2C_ADDR = i2c.scan()[0]
lcd = I2cLcd(i2c, I2C_ADDR, 2, 16)        

print(pullist)

#this prints a random choice from the pullist to the LCD
lcd.putstr(random.choice(pullist))

