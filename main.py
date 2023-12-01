#This file was created by: Ryder Davis
'''
I want To create a game where you shoot a ball into a goal
I want to create mobs that repesent shot blocker that are moving left and right
I want to create an image of a goal net as a background image
I want to also create a AI goalie that you play against when you shoot
I want to create mobs that are tagrets in the goal.
'''

# Base code helped by https://trinket.io/python/909d6c5804

import random
direction=["left","middle","right"]
totalPenalties=0
userTeamScore=0
computerTeamScore=0
print("------WELCOME TO THE PYTHON PENALTY SHOOTOUT------")
print("The options you can choose are left,right or middle")


#sourcecodecomment


# import libraries and modules
import pygame as pg
from pygame.sprite import Sprite
import random
from random import randint
import os
from settings import *
from sprites import *
import math

    

# setup asset folders here - images sounds etc.
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, 'images')
snd_folder = os.path.join(game_folder, 'sounds')


def __int__(self):
    self.image

def penaltyFor():
    global totalPenalties
    global userTeamScore
    totalPenalties+=1
    playerShotDirection=input("Pick your spot:").lower()
    keeperDive=random.choice(direction)
    print("The keeper dives to the "+ keeperDive.upper())
    if playerShotDirection=="left" and keeperDive=="right":
        print ( "it's a save!")
    elif playerShotDirection=="right" and keeperDive=="left":
        print ("it's a save!")
    elif playerShotDirection=="middle" and keeperDive=="middle":
        print ("it's a save!")
    else:
        print("It's a GOOOAAALLLLL!!!!!!!")
        userTeamScore+=1

def penaltyAgainst():
    global totalPenalties
    global computerTeamScore
    totalPenalties+=1
    playerKeeperDive=input("Choose dive direction:").lower()
    computerShotDirection=random.choice(direction)
    print ("The computer hits the ball to the "+computerShotDirection)
    if computerShotDirection=="left" and playerKeeperDive=="right":
        print ( "It's a SSSAVVVVEEEEE!!!!!!")
    elif computerShotDirection=="right" and playerKeeperDive=="left":
        print ("It's a SSSAVVVVEEEEE!!!!!!")
    elif computerShotDirection=="middle" and playerKeeperDive=="middle":
        print ("It's a SSSAVVVVEEEEE!!!!!!")
    else:
        print("It's a Goal!!!!")
        computerTeamScore+=1

def printScores():
    print("The score is now USER:"+str(userTeamScore)+" "+"COMPUTER:"+str(computerTeamScore))

def finalScore():
    print("FINAL SCORE "+str(userTeamScore) +"-" +str(computerTeamScore)) 
    if userTeamScore>computerTeamScore:
        print ("Well done you won")
    elif userTeamScore==computerTeamScore:
        print("A draw")
    else:
        print("You Lose") 
    
while totalPenalties<10:
    penaltyFor()
    penaltyAgainst()
    printScores()
finalScore()
    