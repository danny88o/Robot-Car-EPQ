import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
Trigger = 17
Echo = 18
GPIO.setup(Trigger, GPIO.OUT)
GPIO.setup(Echo, GPIO.IN)
time.sleep(1)

def distancescanner(Trigger, Echo):

        GPIO.output(Trigger, False)

        GPIO.output(Trigger, True)
        time.sleep(0.00001)
        GPIO.output(Trigger,False)

        
        while GPIO.input(Echo) == 0:
                InitialTime = time.time()
        while GPIO.input(Echo) == 1:
                EndTime = time.time()
            
        distance = ((EndTime - InitialTime)*34326)/2
        print("Distance = ", str(distance))
        return distance

