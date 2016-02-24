#!/usr/bin/env python
""" Handles interactions with water valve """
import RPi.GPIO as GPIO
import time

def open_valve(valve_num, seconds_open):
    """ Must be tested with LEDs """
    if valve_num < 0 or valve_num > 7 or not isinstance(valve_num, (int, long)):
        raise ValueError("Invalid valve number")
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(valve_num, GPIO.OUT)
    GPIO.output(valve_num, True)
    time.sleep(seconds_open)
    GPIO.output(valve_num, False)
    GPIO.cleanup()