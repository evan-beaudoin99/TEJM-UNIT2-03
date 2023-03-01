# Created by: Evan Beaudoin
# Created on: March 2023
#
#  Turns an LED on for one second, then off for one second, repeatedly.

import time
import board
from digitalio import DigitalInOut, Direction


# LED setup for onboard LED
led = DigitalInOut(board.GP8)
led.direction = Direction.OUTPUT

while True:

    led.value = True
    print("led on")
    time.sleep(1)

    led.value = False
    print("led off")
    time.sleep(1)
    
 
