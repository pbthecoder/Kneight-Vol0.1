#Test RPG by David Sun
#December 31, 2022
#This has no copyright information. I created it by myself. 

import pygame
pygame.init()

win = pygame.display.set_mode((2475,2000))
pygame.display.set_caption("Dope RPG")

x = 0
y = 0

vel = 5

run = True
cImg = pygame.image.load('Kneight200x200pix.png')
bg = pygame.image.load("BGKneight'sPath.png")
win.blit(cImg, (0,0))
while run:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_LEFT]:
        x -= vel

    if keys[pygame.K_RIGHT]:
        x += vel

    if keys[pygame.K_UP]:
        y -= vel

    if keys[pygame.K_DOWN]:
        y += vel
    win.fill((26, 150, 59))  # Fills the screen with dark greenish grass
    win.blit(cImg,(x,y))   
    pygame.display.update() 
    
pygame.quit()

#some more ideas
#Can put people to interact with
#to be done
