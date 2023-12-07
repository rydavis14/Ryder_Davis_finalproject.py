#This file was created by: Ryder Davis

#help Run and close game
import pygame, sys

#Iniiates all pygame modules
pygame.init()
clock = pygame.time.Clock()

screen_width = 1280
screen_hight = 960
#displays the surface object we stored in the variables
screen = pygame.display.set_mode((screen_width,screen_hight))
pygame.display.set_caption('Shootout')

ball = pygame.rect(screen_width/2 - 15, screen_hight/2 - 15, 40,40)
player  = pygame.rect(screen_width - 20, screen_hight/2 - 70, 10,140)
opponent = pygame.rect(10,screen_hight/2 - 70, 10,140)

bg_color = pygame.color('grey12')
light_grey  = (200,200,200)


#Ends the game/closes
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(bg_color)
    pygame.draw.rect(screen,light_grey,player)
    pygame.draw.rect(screen,light_grey,opponent)
    pygame.draw.ellipse(screen,light_grey,ball)
    pygame.draw.aaline(screen,light_grey, (screen_width/2,0),(screen_width/2,screen_hight))




    pygame.display.flip()
    #limits/controls how fast the game runs
    clock.tick(60)





