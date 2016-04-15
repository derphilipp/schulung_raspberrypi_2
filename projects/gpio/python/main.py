#!/usr/bin/env python2
import time
import RPi.GPIO as GPIO

# RPi.GPIO use BCM Layout (instead of BOARD)
GPIO.setmode(GPIO.BCM)

PIN_RED = 27
PIN_YELLOW = 17
PIN_GREEN = 4

GPIO.setup(PIN_RED, GPIO.OUT)
GPIO.setup(PIN_YELLOW, GPIO.OUT)
GPIO.setup(PIN_GREEN, GPIO.OUT)

# Turn off everything
GPIO.output(PIN_RED, GPIO.LOW)
GPIO.output(PIN_YELLOW, GPIO.LOW)
GPIO.output(PIN_GREEN, GPIO.LOW)

print("Everything initialized")

time.sleep(2)
GPIO.output(PIN_GREEN, GPIO.HIGH)
