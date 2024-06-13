import RPi.GPIO as GPIO
import time GPIO.setmode(GPIO.BCM)
pir=14
GPIO.setup(pir, GPIO.IN)
try:
while True:
motion GPIO.input(pir)
if motion==True:
print("motion detected")
else:
Print("motion not detected")
except:
GPIO.cleanup()