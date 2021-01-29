import RPi.GPIO as GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

RF = 7
RB = 8
LF = 10
LB = 9
callibration = 0.86
GPIO.setup(RF, GPIO.OUT)
GPIO.setup(RB, GPIO.OUT)
GPIO.setup(LF, GPIO.OUT)
GPIO.setup(LB, GPIO.OUT)
Hz = 20
pwmRF = GPIO.PWM(RF,Hz)
pwmRB = GPIO.PWM(RB,Hz)
pwmLF = GPIO.PWM(LF,Hz)
pwmLB = GPIO.PWM(LB,Hz)
pwmRF.start(0)
pwmRB.start(0)
pwmLF.start(0)
pwmLB.start(0)

def forward(DutyCycle):
    pwmRF.ChangeDutyCycle(DutyCycle)
    pwmRB.ChangeDutyCycle(0)
    pwmLF.ChangeDutyCycle(DutyCycle*callibration)
    pwmLB.ChangeDutyCycle(0)
        
def right(DutyCycle):
    pwmRF.ChangeDutyCycle(0)
    pwmRB.ChangeDutyCycle(0)
    pwmLF.ChangeDutyCycle(DutyCycle)
    pwmLB.ChangeDutyCycle(0)

def left(DutyCycle):
    pwmRF.ChangeDutyCycle(DutyCycle)
    pwmRB.ChangeDutyCycle(0)
    pwmLF.ChangeDutyCycle(0)
    pwmLB.ChangeDutyCycle(0)

def rotateright(DutyCycle):
    pwmRF.ChangeDutyCycle(0)
    pwmRB.ChangeDutyCycle(DutyCycle)
    pwmLF.ChangeDutyCycle(DutyCycle*callibration)
    pwmLB.ChangeDutyCycle(0)
def rotateleft(DutyCycle):
    pwmRwsF.ChangeDutyCycle(DutyCycle)
    pwmRB.ChangeDutyCycle(0)
    pwmLF.ChangeDutyCycle(0)
    pwmLB.ChangeDutyCycle(DutyCycle)   
def backwards(DutyCycle):
    pwmRF.ChangeDutyCycle(0)
    pwmRB.ChangeDutyCycle(DutyCycle)
    pwmLF.ChangeDutyCycle(0)
    pwmLB.ChangeDutyCycle(DutyCycle*callibration)

def motoroff():
    pwmRF.ChangeDutyCycle(0)
    pwmRB.ChangeDutyCycle(0)
    pwmLF.ChangeDutyCycle(0)
    pwmLB.ChangeDutyCycle(0)




    
