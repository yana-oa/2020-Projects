###Welcome to
##Mouse Trails Program!
##Ariana Faye Penalosa
##########################

from random import randint
import pygame
pygame.init()

#declaring vars
gameCanvas = pygame.display.set_mode((800,600))
RED  =(255,0,0)
GREEN=(0,255,0)
BLUE =(0,0,255)

#Shapee
square_sides=10
square_x = 400
square_y = 300
speed_x = 1
speed_y =1
CLR = RED

#update func
def redraw_Canvas():
    pygame.draw.rect(gameCanvas, CLR, (square_x,square_y,square_sides,square_sides),0)
    pygame.display.update()

#---Main---#
end = False

while not end:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            end = True
    (square_x,square_y)= pygame.mouse.get_pos()
    CLR=(randint(0,255),randint(0,255),randint(0,255))
    redraw_Canvas()
    pygame.time.delay(2)
    
pygame.quit()
    
            
