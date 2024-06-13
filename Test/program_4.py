import RP1.GPIO as GPIO
import time GPIO.setmode(GPIO.BCM)
led=14 
GPIO.setup(led,GPIO.OUT) GPIO.setup(led,GPIO.LOW)
PWM-GPIO.PWM(led, 1000)
PWM.start(0)
 try:
while True:
for dc in range(0,101,5):
PWM.ChangeDutyCycle(dc)
time.sleep(0.05)
time.sleep(0.5)
for dc in range(100,-1,-5);
PWM.ChangeDutyCycle(dc)
time.sleep(0.05)
time.sleep(0.5)
except:
PWM.stop()
GPIO.output(led,GPIO.LOW)
GPIO.cleanup()