#This file was created by: Ryder Davis

#Sources
'''
Mr. Chris Cozort
https://trinket.io/python/909d6c5804
Chat GbT
https://www.youtube.com/watch?v=Qf3-aDXG8q4
https://www.youtube.com/watch?v=E4Ih9mpn5tk 
'''



#help Run and close game
import pygame, sys, random 

def ball_animation():
    global ball_speed_x, ball_speed_y, player_score, opponent_score, score_timer
    
    ball.x += ball_speed_x
    ball.y += ball_speed_y
# reverses both axis ball speed speratley 
# use >=, <= instead of == because it
    if ball.top <= 0 or ball.bottom >=screen_hight:
        # vertical ball speed
        ball_speed_y *= -1
    #when player scores
    if ball.left <= 0:
        #adds a point to the player after scoring
        player_score += 1
        #How much time the game has been running
        score_timer = pygame.time.get_ticks()

    #when opponet scores
    if ball.right >= screen_width:
        # horizontal ball speed
        #adds a point to opponent after scoring
        opponent_score += 1
        score_timer = pygame.time.get_ticks()

    if ball.colliderect(player) or ball.colliderect(opponent):
        ball_speed_x *= -1
def player_animation():
    player.y += player_speed
    #if player top is higher then 0, put player top at 0
    if player.top <= 0:
        player.top = 0
    if player.bottom >= screen_hight:
        player.bottom = screen_hight
# Moves AI player up and down
def opponent_ai():
    if opponent.top < ball.y:
        opponent.top += opponent_speed
    if opponent.bottom >ball.y:
        opponent.bottom -= opponent_speed
    if opponent.top <= 0:
        opponent.top = 0
    if opponent.bottom >= screen_hight:
        opponent.bottom = screen_hight
#brings ball to center after goal
def ball_restart():
    global ball_speed_x, ball_speed_y,score_timer
    #time for ball restart
    current_time = pygame.time.get_ticks()
    #where text will be displayed
    ball.center = (screen_width/2, screen_hight/2)
    #display number 3 for 700miliseconds
    if current_time - score_timer < 700:
        number_three = game_font.render("3",False,light_grey)
        screen.blit(number_three,(screen_width/2 - 10, screen_hight/2 +20))
    #display number 2 for 700miliseconds
    if current_time - score_timer < 1400:
        number_two = game_font.render("2",False,light_grey)
        screen.blit(number_two,(screen_width/2 - 10, screen_hight/2 +20))
    #display number 1 for 700miliseconds
    if current_time - score_timer < 2100:
        number_one = game_font.render("1",False,light_grey)
        screen.blit(number_one,(screen_width/2 - 10, screen_hight/2 +20))
    if current_time - score_timer < 2100:
        ball_speed_x, ball_speed_y = 0,0
    else:
    #randmizes direction of ball after reset
        ball_speed_y = 7 * random.choice((1,-1))
        ball_speed_x = 7 * random.choice((1,-1))
        score_timer = None





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

ball_speed_x = 7 * random.choice((1,-1))
ball_speed_y = 7 * random.choice((1,-1))
player_speed = 0 
opponent_speed = 7

player_score = 0 
opponent_score = 0
game_font = pygame.font.Font("freesansbold.ttf",32)

# score timer
score_timer = True

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
            #allows up key to move player up
            if event.key == pygame.K_UP:
                player_speed -=7
        if event.type ==pygame.KEYUP:
            #allows player to move down
            if event.key == pygame.K_DOWN:
                # allows player movemrnt to stay constant
                player_speed -=7
            if event.key == pygame.K_UP:
                player_speed +=7



    ball_animation()
    player_animation()
    opponent_ai()



    screen.fill(bg_color)
    pygame.draw.rect(screen,light_grey,player)
    pygame.draw.rect(screen,light_grey,opponent)
    pygame.draw.ellipse(screen,light_grey,ball)
    pygame.draw.aaline(screen,light_grey, (screen_width/2,0),(screen_width/2,screen_hight))

    if score_timer:
        ball_restart()


    
    #creates display surface
    player_text = game_font.render(f"{player_score}",False,light_grey)
    #puts one surface on another
    screen.blit(player_text,(600,400))
    opponent_text = game_font.render(f"{opponent_score}",False,light_grey)
    #puts one surface on another
    screen.blit(opponent_text,(560,400))


    pygame.display.flip()
    #limits/controls how fast the game runs
    clock.tick(60)







