import pygame
import sys
import time

pygame.init()

win = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Pygame on Windows")

cycleTime = 0.05 #in seconds

# info about the square
x = 50
y = 50
w = 40
h = 50
vel = 5

while(True):
    for event in pygame.event.get():
        pygame.event.pump()
        if event.type == pygame.QUIT:
            print("It's over we are quitting")
            pygame.quit()
            sys.exit()
            
        # not working on hold have to presee each time
##        elif event.type == pygame.KEYDOWN:
##            print("there is a keydown")
##            if event.key == pygame.K_LEFT:
##                #print("LEFT Key Pressed")
##                x -= vel
##            if event.key == pygame.K_RIGHT:
##                #print("RIGHT Key Pressed")
##                x += vel
##            if event.key == pygame.K_UP:
##                #print("LEFT Key Pressed")
##                y -= vel
##            if event.key == pygame.K_DOWN:
##                #print("RIGHT Key Pressed")
##                y += vel

        #will work on hold
    keys = pygame.key.get_pressed()
    if keys[pygame.K_DOWN]:
        y += vel
    if keys[pygame.K_UP]:
        y -= vel
    if keys[pygame.K_RIGHT]:
        x += vel
    if keys[pygame.K_LEFT]:
        x -= vel
            
        
                

    win.fill((0,0,0))
    pygame.draw.rect(win, (255,0,0), (x, y, w, h))
    pygame.draw.ellipse(win, (100,100,255), (x, y, w, h))
    pygame.display.update()

    pygame.time.delay(100)
        
                
            



