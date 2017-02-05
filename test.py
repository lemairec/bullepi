import RPi.GPIO as GPIO

#4 17 27 22
GPIO.setup(4, GPIO.OUT, initial=GPIO.HIGH)
GPIO.output(4, GPIO.LOW)
