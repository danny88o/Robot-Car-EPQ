import pygame, sys
from pygame.locals import *
import RPi.GPIO as GPIO
import CarBasicFunctions as car

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

pygame.init()
window = pygame.display.set_mode((100,100), 0, 32)
window.fill((100,100,100))

while True:
    for event in pygame.event.get():

        if event.type == QUIT :
            pygame.quit()
            sys.exit()

        if event.type != KEYDOWN:
            car.motoroff()      

        if event.type == KEYDOWN:
            
            if event.key == pygame.K_w:
                car.forward()
            if event.key == pygame.K_d:
                car.right()
            if event.key == pygame.K_a:
                car.left()
            if event.key == pygame.K_s:
                car.backwards()
            if event.key == pygame.K_q:
                car.rotateleft()
            if event.key == pygame.K_e:
                car.rotateright()
            if event.key == pygame.K_l:
                pygame.quit()
                sys.exit()
GPIO.cleanup()
