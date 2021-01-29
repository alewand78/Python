import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False) GPIO.setmode(GPIO.BOARD)
GPIO.setup(leds, GPIO.OUT) 

for i in range(0, 10): 
	GPIO.output(leds, 1)
	time.sleep(0.5)
	GPIO.output(leds, 0)
	time.sleep(0.5)