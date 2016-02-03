import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM) 
GPIO.setup(26, GPIO.OUT)


while 1==1:
   GPIO.output(26, 0)
   time.sleep(0.5)
   GPIO.output(26, 0)
   time.sleep(0.5)




