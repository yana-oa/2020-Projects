####Button Control owo####
###Ariana Faye
###This program allows the user to move a ball around w arrow keys

###################
import pygame
pygame.init()

gameCanvas= pygame.display.set_mode((800,600))

#BG image imported for blittin
bgPic = pygame.image.load("sky.jpg")
bgPic = pygame.transform.scale(bgPic, (800,600))
bgPic = bgPic.convert_alpha()
bg_x  = 0
bg_y  = 0

##colors
MAIN =(249,129,56)
RED  =(255,0,0)
GREEN=(0,255,0)
BLUE =(0,0,255)
YELL =(255,255,0)
CYAN =(0,255,255)
GREY =(128,128,128)
WHITE=(255,255,255)
BLACK=(0,0,0)
CLR = BLACK

##the ball
ball_rad = 20
#ball coordinate (centered) (now a star oops)
star_x = 0
star_y = 0

#added a code to change the speed of the object by pressing "1" and "2" (see code below)
speed_x,speed_y = 2,2

##function that redraws all objects

def redraw_canvas():
    gameCanvas.fill(MAIN)
    gameCanvas.blit(bgPic,(bg_x,bg_y))
    pygame.draw.polygon(gameCanvas,CLR,[(star_x+25, star_y), (star_x, star_y+25), (star_x+25, star_y+50), (star_x+50, star_y+25)],0)
    #pygame.draw.polygon(gameCanvas,RED,[(star_x-770, star_y-595), (star_x-795, star_y-570), (star_x-770, star_y-545), (star_x-745, star_y-570)],0)
    pygame.display.update()
    
##main program now
end = False
while not end:

    for event in pygame.event.get():
        if event.type == pygame.QUIT: #is this a built in function?
            end = True

    if star_x < 0 or (star_x+50) > 800:
       speed_x= speed_x*-1
    if star_y < 0 or (star_y+50) > 600:
       speed_y= speed_y*-1
    print(star_x,star_y)

    #hmmm sometimes when it converts it to the opposite direction,
    #it stays that way, making it the wrong direction sometimes
       
    keys = pygame.key.get_pressed()

    if keys[pygame.K_1]:
        speed_x,speed_y = 2,2
    if keys[pygame.K_2]:
        speed_x,speed_y = 4,4
    
    if keys[pygame.K_LEFT]:
        star_x = star_x - speed_x
        CLR = BLUE
    if keys[pygame.K_RIGHT]:
        star_x = star_x + speed_x
        CLR = RED
    if keys[pygame.K_UP]:
        star_y = star_y - speed_y
        CLR = YELL
    if keys[pygame.K_DOWN]:
        star_y = star_y + speed_y
        CLR = GREEN

    redraw_canvas()
    pygame.time.delay(2) ##2 millisecond pause

pygame.quit()
