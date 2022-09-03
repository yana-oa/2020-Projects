##Welcome to the       ##
##Animation Program for##
##Intro to Pygame      ##
##Ariana Faye          ##
#########################

import pygame
pygame.init()

WIDTH= 800
HEIGHT= 600
gameCanvas= pygame.display.set_mode((800,600))

#Title
pygame.display.set_caption("AnimationS")

##Colors List
MAIN =(249,129,56)
RED  =(255,0,0)
GREEN=(0,255,0)
BLUE =(0,0,255)
YELL =(255,255,0)
CYAN =(0,255,255)
GREY =(128,128,128)
WHITE=(255,255,255)
BLACK=(0,0,0)

#Different Speeds
reg_speedx = 1
reg_speedy = 1

med_speedx = 2
med_speedy = 2

fast_speedx = 4
fast_speedy = 4

#Ball 1
firstBall_rad = 65
first_x = 450
first_y = 250

#Ball 2
scndBall_rad = 40
scnd_x = 320
scnd_y = 560

#Ball 3
lastBall_rad = 10
last_x = 10
last_y = 550

##redraw/update Canvas func
def redraw_Canvas():
    gameCanvas.fill(MAIN)
    pygame.draw.circle(gameCanvas, RED,(first_x,first_y), firstBall_rad,0)
    pygame.draw.circle(gameCanvas,BLUE,(scnd_x,scnd_y), scndBall_rad,0)
    pygame.draw.circle(gameCanvas,YELL,(last_x,last_y),lastBall_rad,0)
    pygame.display.update()


#---Main---#
end = False

while not end:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            end = True

    #ball 1 anim
    first_x+=reg_speedx
    first_y+=reg_speedy
    if (first_x + firstBall_rad) > WIDTH or (first_x - firstBall_rad) < 0:
        reg_speedx = reg_speedx*-1
    if (first_y + firstBall_rad) > HEIGHT or (first_y - firstBall_rad) < 0:
        reg_speedy = reg_speedy*-1

    #ball 2 anim
    scnd_x+=med_speedx
    scnd_y+=med_speedy
    if (scnd_x + scndBall_rad) > WIDTH or (scnd_x - scndBall_rad) < 0:
        med_speedx = med_speedx*-1
    if (scnd_y + scndBall_rad) > HEIGHT or (scnd_y - scndBall_rad) < 0:
        med_speedy = med_speedy*-1

    #ball 3 anim
    last_x+=fast_speedx
    last_y+=fast_speedy
    if (last_x + lastBall_rad) > WIDTH or (last_x - lastBall_rad) < 0:
        fast_speedx = fast_speedx*-1
    if (last_y + lastBall_rad) > HEIGHT or (last_y - lastBall_rad) < 0:
        fast_speedy = fast_speedy*-1
        
    redraw_Canvas()
    pygame.time.delay(2)
    
pygame.quit()
