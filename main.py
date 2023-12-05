#This file was created by: Ryder Davis
'''
I want To create a game where you shoot a ball into a goal
I want to create mobs that repesent shot blocker that are moving left and right
I want to create an image of a goal net as a background image
I want to also create a AI goalie that you play against when you shoot
I want to create mobs that are tagrets in the goal.
'''

# Base code helped by https://trinket.io/python/909d6c5804
# Chat GBT
# Youtube

import random
direction=["left","middle","right"]
totalPenalties=0
PlayerScore=0
CpuScore=0
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
    global PlayerScore
    totalPenalties+=1
    playerShotDirection=input("Pick your spot:").lower()
    TendeyDive=random.choice(direction)
    print("The Tendey dives to the "+ TendeyDive.upper())
    if playerShotDirection=="left" and TendeyDive=="right":
        print ( "it's a save!")
    elif playerShotDirection=="right" and TendeyDive=="left":
        print ("it's a save!")
    elif playerShotDirection=="middle" and TendeyDive=="middle":
        print ("it's a save!")
    else:
        print("It's a GOOOAAALLLLL!!!!!!!")
        PlayerScore+=1

def penaltyAgainst():
    global totalPenalties
    global CpuScore
    totalPenalties+=1
    playerTendeyDive=input("Choose dive direction:").lower()
    computerShotDirection=random.choice(direction)
    print ("The computer hits the ball to the "+computerShotDirection)
    if computerShotDirection=="left" and playerTendeyDive=="right":
        print ( "It's a SSSAVVVVEEEEE!!!!!!")
    elif computerShotDirection=="right" and playerTendeyDive=="left":
        print ("It's a SSSAVVVVEEEEE!!!!!!")
    elif computerShotDirection=="middle" and playerTendeyDive=="middle":
        print ("It's a SSSAVVVVEEEEE!!!!!!")
    else:
        print("It's a Goal!!!!")
        computerTeamScore+=1

def printScores():
    print("The score is now USER:"+str(PlayerScore)+" "+"COMPUTER:"+str(CpuScore))

def finalScore():
    print("FINAL SCORE "+str(PlayerScore) +"-" +str(CpuScore)) 
    if PlayerScore>CpuScore:
        print ("Well done you won")
    elif PlayerScore==CpuScore:
        print("A draw")
    else:
        print("You Lose") 
    
while totalPenalties<10:
    penaltyFor()
    penaltyAgainst()
    printScores()
finalScore()
    