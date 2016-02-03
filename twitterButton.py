import RPi.GPIO as GPIO
import time
import urllib2

GPIO.setmode(GPIO.BCM)
GPIO.setup(26, GPIO.IN)

def buttonPressed(argument):
   print "The Button was pressed"
   url="https://maker.ifttt.com/trigger/ButtonPressed/with/key/g0BhW1jHunSLXKdnJDiz8CJjJX_LINLZ8ea193EJMSl"
   urllib2.urlopen(url)




GPIO.add_event_detect(26, GPIO.RISING, callback=buttonPressed )


time.sleep(3600)

