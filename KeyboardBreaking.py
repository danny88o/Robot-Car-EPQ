import pygame, sys
from pygame.locals import *
import RPi.GPIO as GPIO
import time
import AdvancedMotorFunctions as car
from Basic_echo import distancescanner 

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

RF = 7
RB = 8
LF = 10
LB = 9
trigger = 17
echo = 18

GPIO.setup(RF, GPIO.OUT)
GPIO.setup(RB, GPIO.OUT)
GPIO.setup(LF, GPIO.OUT)
GPIO.setup(LB, GPIO.OUT)


pygame.init()
window = pygame.display.set_mode((100,100), 0, 32)
window.fill((100,100,100))

while True:
    for event in pygame.event.get():

        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if event.type != KEYDOWN:
            motoroff()
            

        if event.type == KEYDOWN:

            if event.key == pygame.K_s:
                car.backwards(80)
            if event.key == pygame.K_w:
                if int(distancescanner(trigger,echo)) <= 20:
                    car.motoroff()
                else:
                    car.forward(80)
            if event.key == pygame.K_d:
                if int(distancescanner(trigger,echo)) <= 20:
                    car.motoroff()
                else:
                    car.right(80)
            if event.key == pygame.K_a:
                if int(distancescanner(trigger,echo)) <= 20:
                    motoroff()
                else:
                    car.left(80)
            if event.key == pygame.K_q:
                car.rotateleft(80)
            if event.key == pygame.K_e:
                car.rotateright(80)
            if event.key == pygame.K_l:
                pygame.quit()
                sys.exit()
GPIO.cleanup()
                

