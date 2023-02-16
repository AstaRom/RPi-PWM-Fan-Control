#! /usr/bin/env python3

import RPi.GPIO as GPIO
import sys


FAN_PIN = 18   # BCM pin used to drive PWM fan
WAIT_TIME = 1  # [s] Time to wait between each refresh
PWM_FREQ = 25  # [Hz] PWM frequency
FAN_OFF = 0

GPIO.setmode(GPIO.BCM)
GPIO.setup(FAN_PIN, GPIO.OUT, initial=GPIO.LOW)
fan = GPIO.PWM(FAN_PIN, PWM_FREQ)
fan.start(FAN_OFF)


try:
    while 1:
        speed = float(input("Fan Speed: "))
        fan.ChangeDutyCycle(speed)

except KeyboardInterrupt:
    print("Fan ctrl interrupted by keyboard")
    pass

finally:
    GPIO.cleanup()