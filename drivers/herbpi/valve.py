#!/usr/bin/env python
""" Handles interactions with water valve """
import RPi.GPIO as GPIO
import time

VALVENUM = {0:7, 1:11, 2:12, 3:13, 4:15, 5:16, 6:18, 7:22}

def open_valve(valve_num, seconds_open):
    """ Must be tested with LEDs """
    if valve_num not in VALVENUM.keys():
        raise ValueError("Invalid valve number")
    pin_num = VALVENUM[valve_num]
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(pin_num, GPIO.OUT)
    GPIO.output(pin_num, True)
    time.sleep(seconds_open)
    GPIO.output(pin_num, False)
    GPIO.cleanup()
