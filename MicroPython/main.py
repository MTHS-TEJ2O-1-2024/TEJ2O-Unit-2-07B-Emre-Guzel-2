"""
Created by: Emre Guzel 
Created on: Oct 1 2024
This module is a Micro:bit cookie clicker 
"""

from microbit import *

display.clear()

display.show(Image.HAPPY)
#Setting the button B#
while True:
    if button_b.get_presses():
        cookie_rest=0
        display.scroll(cookie_rest + )
        if button_a.get_presses():
            cookie_number = + 1
            display.scroll(cookie_number -1)