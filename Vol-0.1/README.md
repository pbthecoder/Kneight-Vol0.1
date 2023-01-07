#Vol-0.1

This is where I put the code. 

Keep in mind other volumes will be put into different repositaries. 

What this code does: 

Lines 1-3: Comments

import pygame
pygame.init()

Sets up the window

win = pygame.display.set_mode((2475,2000)) is fitted to the size of the screen I use. You can make a copy and change it. DO NOT CHANGE WHAT I HAVE DONE HERE. IT TOOK LOTS OF SACRIFICE.

x = 0
y = 0

vel = 5

run = True

Run is a boolean, and it will be used to define the running. 
Vel is the amount of movement. It stands for velocity. 
x and y define the x and y. For some reason, it always starts at the top corner. 
If you can fix it, I would be happy. 

cImg = pygame.image.load('Kneight200x200pix.png')
win.blit(cImg, (0,0))

It is called cImg as a test. I wanted to use something very, very easy to type just in case of error. 
It draws the basic images, and BGKneight's Path does not work, unfortunately. 
It will be replaced. 

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

Game loop. 

It is very self explanatory. 

Yes, it is. 

At the bottom I put some more comments for ideas. 



All the art was done on Pixilart. To see the art, go to https://www.pixilart.com/phoenixblazes
