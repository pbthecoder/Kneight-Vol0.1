#Test RPG by David Sun
#December 31, 2022
#This has no copyright information. I created it by myself

import pygame,sys
from pygame.locals import *
import keyboard

pygame.init()

#FPS frames per second

FPS = 30 # frames per second setting
fpsClock = pygame.time.Clock()

#set up window

DISPLAYSURF = pygame.display.set_mode((500,400),0,32)
pygame.display.set_caption("Test RPG")

#Set Image
WHITE = (255, 255, 255)
KneightImg = pygame.image.load('Kneight.png')
Kneightx = 10
Kneighty = 10
direction = 'right'

#run Game Loop

while True: # the main game loop
    DISPLAYSURF.fill(WHITE)
    try:
        if keyboard.is_pressed('a'):
            Kneightx += 5
        elif keyboard.is_pressed('d'):
            Kneightx -= 5
        elif keyboard.is_pressed('w'):
            Kneighty += 5
        elif keyboard.is_pressed('s'):
            Kneighty-= 5


    DISPLAYSURF.blit(KneightImg, (Kneightx, Kneighty))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
    fpsClock.tick(FPS)
    
while True:
  for event in pygame.event.get():
    if event.type == QUIT:
      pygame.quit()
      sys.edit()
  pygame.display.update()
