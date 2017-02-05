import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

#4 17 27 22
GPIO.setup(4, GPIO.OUT, initial=GPIO.LOW)
print "low"
GPIO.output(4, GPIO.LOW)
time.sleep(5)
print "high"
GPIO.output(4, GPIO.HIGH)

