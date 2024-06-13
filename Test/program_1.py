import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings (False)
pins=[14,15,18,23]
for pin in pins:
GPIO.setup(pin, GPIO.OUT)
for pin in pins:
GPIO.output(pin, GPIO.HIGH)
time.sleep(1)
GPIO.output(pin, GPIO. LOW)