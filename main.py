

# Example file showing a circle moving on screen
import pygame
import math
# pygame setup
pygame.init()

#GAME VARIABLES
screen = pygame.display.set_mode((300, 600))
clock = pygame.time.Clock()
running = True
dt = 0
background = pygame.image.load("assets/bg.png")

## NOTE VARIABLES
noteSpeed = 100
noteHoldTime = 5
noteDeadzone = 25



## A BLOCKS
aBlockImage = pygame.image.load("assets/A.png")
def aBlock(x, y):
    screen.blit(aBlockImage, (x, y))
aX = 75
aY = 0
aHeld = False
aTimout = 0

## B BLOCKS
bBlockImage = pygame.image.load("assets/B.png")
def bBlock(x, y):
    screen.blit(bBlockImage, (x, y))
bX = 225
bY = 0
bHeld = False
bTimout = 0


## LOOP
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    
    aY += noteSpeed * dt
    bY +=  noteSpeed * dt

    ## RENDERING
    screen.blit(background, (0,0))
    aBlock(aX, aY)
    bBlock(bX, bY)

    # display visual indicator for if buttons are pressed
    if(aHeld == True):
        pygame.draw.circle(screen, "green", pygame.Vector2(0, 500), 49)
    if(bHeld == True):
        pygame.draw.circle(screen, "red", pygame.Vector2(300, 500), 49)

    if(abs(aY - 500) <= noteDeadzone):
        #print("A NOTE IN ZONE")
        if(aHeld == True):
            #print("A NOTE HIT")
            aBlockImage = pygame.image.load("assets/BLANK.png")
    if(abs(bY - 500) <= 30):
        #print("B NOTE IN ZONE")
        if(bHeld == True):
            #print("B NOTE HIT")
            bBlockImage = pygame.image.load("assets/BLANK.png")


    ## KEYBINDS
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        if aTimout >= noteHoldTime:
            aHeld = False
        else:
            aHeld = True
        aTimout = aTimout+1
    else:
        aTimout = 0
    
    if keys[pygame.K_d]:
        if bTimout >= noteHoldTime:
            bHeld = False
        else:
            bHeld = True
        bTimout = bTimout+1
    else:
        bTimout = 0
    
            
        

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()

