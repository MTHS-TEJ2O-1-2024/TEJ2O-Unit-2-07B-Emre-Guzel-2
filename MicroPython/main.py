"""
Created by: Emre Guzel 
Created on: Oct 1 2024
This module is a Micro:bit cookie counter 
"""
from microbit import *
display.clear()
display.show(Image.HAPPY)
cookie_count=0

while True:
    if button_b.is_pressed():
        cookie_count=0
        display.scroll(cookie_count)

    if button_a.is_pressed():
        cookie_count += 1
        display.scroll(cookie_count)