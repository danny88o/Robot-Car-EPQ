import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

RF = 7
RB = 8
LF = 10
LB = 9

GPIO.setup(RF, GPIO.OUT)
GPIO.setup(RB, GPIO.OUT)
GPIO.setup(LF, GPIO.OUT)
GPIO.setup(LB, GPIO.OUT)

GPIO.output(RF,1)
GPIO.output(RB,0)
GPIO.output(LF,1)
GPIO.output(LB,0)

time.sleep(5)

GPIO.output(RF,0)
GPIO.output(RB,1)
GPIO.output(LF,0)
GPIO.output(LB,1)

time.sleep(5)

GPIO.cleanup()


