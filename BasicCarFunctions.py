import RPi.GPIO as GPIO

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

def forward():
    GPIO.output(RF,1)
    GPIO.output(RB,0)
    GPIO.output(LF,1)
    GPIO.output(LB,0)

def right():
    GPIO.output(RF,0)
    GPIO.output(RB,0)
    GPIO.output(LF,1)
    GPIO.output(LB,0)

def left():
    GPIO.output(RF,1)
    GPIO.output(RB,0)
    GPIO.output(LF,0)
    GPIO.output(LB,0)

def backwards():
    GPIO.output(RF,0)
    GPIO.output(RB,1)
    GPIO.output(LF,0)
    GPIO.output(LB,1)

def motoroff():
    GPIO.output(RF,0)
    GPIO.output(RB,0)
    GPIO.output(LF,0)
    GPIO.output(LB,0)
    
def rotateright():
    GPIO.output(RF,0)
    GPIO.output(RB,1)
    GPIO.output(LF,1)
    GPIO.output(LB,0)
    
def rotateleft():
    GPIO.output(RF,1)
    GPIO.output(RB,0)
    GPIO.output(LF,0)
    GPIO.output(LB,1)
