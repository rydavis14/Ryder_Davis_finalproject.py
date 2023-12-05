#https://chat.openai.com/c/0f65127f-a1f0-493b-8c60-3359ee5ef202 

import pygame
import sys
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

# Initialize Pygame
pygame.init()
def __init__(self):
    self.image = self.image = pg.image.load(os.path.join(img_folder, 'pologoal.png')).convert()


# Set up the display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Soccer Goal Sprite")

# Define colors
white = (255, 255, 255)
black = (0, 0, 0)

# Load goal image
goal_image = pygame.image.load("pologoal.png")  # You need to have a soccer_goal.png image file

# Get the rect of the goal image
goal_rect = goal_image.get_rect()

# Position the goal in the center of the screen
goal_rect.center = (width // 2, height // 2)

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Fill the screen with white
    screen.fill(white)

    # Draw the goal sprite on the screen
    screen.blit(goal_image, goal_rect)

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    pygame.time.Clock().tick(60)
