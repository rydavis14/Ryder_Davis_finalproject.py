#This file was created by: Ryder Davis

#help Run and close game
import pygame, sys

def ball_animation():
    global ball_speed_x, ball_speed_y
    ball.x += ball_speed_x
    ball.y += ball_speed_y
# reverses both axis ball speed speratley 
# use >=, <= instead of == because it
    if ball.top <= 0 or ball.bottom >=screen_hight:
        # vertical ball speed
        ball_speed_y *= -1
    if ball.left <= 0 or ball.right >= screen_width:
        # horizontal ball speed
        ball_speed_x *= -1

    if ball.colliderect(player) or ball.colliderect(opponent):
        ball_speed_x *= -1
def player_animation():
    player.y += player_speed
    #if player top is higher then 0, put player top at 0
    if player.top <= 0:
        player.top = 0
    if player.bottom >= screen_hight:
        player.bottom = screen_hight

    



#Iniiates all pygame modules
pygame.init()
clock = pygame.time.Clock()

screen_width = 1180
screen_hight = 860
#displays the surface object we stored in the variables
screen = pygame.display.set_mode((screen_width,screen_hight))
pygame.display.set_caption('Shootout')

ball = pygame.Rect(screen_width/2 - 15,screen_hight/2 - 15,30,30)
player  = pygame.Rect(screen_width - 20,screen_hight/2 - 70, 10,140)
opponent = pygame.Rect(10,screen_hight/2 - 70, 10,140)

bg_color = (0,0,255)
light_grey  = (200,200,200)

ball_speed_x = 7
ball_speed_y = 7
player_speed = 0
opponent_speed = 7


#Ends the game/closes
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type ==pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                # allows player movemrnt to stay constant
                player_speed +=7
            if event.key == pygame.K_UP:
                player_speed -=7
        if event.type ==pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                # allows player movemrnt to stay constant
                player_speed -=7
            if event.key == pygame.K_UP:
                player_speed +=7



    ball_animation()
    player_animation()
    if opponent.top < ball.y:
        opponent.top += opponent_speed
    if opponent.bottom >ball.y:
        opponent.bottom += opponent_speed



    screen.fill(bg_color)
    pygame.draw.rect(screen,light_grey,player)
    pygame.draw.rect(screen,light_grey,opponent)
    pygame.draw.ellipse(screen,light_grey,ball)
    pygame.draw.aaline(screen,light_grey, (screen_width/2,0),(screen_width/2,screen_hight))




    pygame.display.flip()
    #limits/controls how fast the game runs
    clock.tick(60)







