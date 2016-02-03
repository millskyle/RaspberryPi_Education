import RPi.GPIO as GPIO 
import time 
import turtle  

GPIO.setmode(GPIO.BCM)
GPIO.setup(26, GPIO.IN)


while 1==1:
   turtle.forward(4)

   if GPIO.input(26) == 1:
      turtle.right(12)

   time.sleep(0.1)




