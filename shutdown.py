#! /usr/bin/env python3
import os
import RPi.GPIO as GPIO
GPIO.setmode(BCM)
# exchange PIN for your desired PIN
GPIO.setup("PIN", GPIO.IN, pull_up_down=GPIO.PUD_UP)



try:
    while True:
        GPIO.wait_for_edge("PIN", GPIO.FALLING)
        os.system("/sbin/shutdown -h now")
except:
    GPIO.cleanup()
#if not make sure all the pullups are in a known state

