#======================================================
#
#   Author:         Beau Shirdavani
#   Date:           March 1, 2018
#   Description:    Flappy Bird with PyGame
#
#======================================================

# TODO:
#   make pipes - keep it simple, one pipe group at a time...
#   make collision detector
#   track score
#   add start button

import pygame
import random

pygame.init()

# set screen size
game_display = pygame.display.set_mode((900,900))
pygame.display.set_caption("pyGame Practice")

clock = pygame.time.Clock()
crashed = False

# define colors
white = (255, 255, 255)
red = (255, 0, 0)
orange = (255, 125, 0)
yellow = (255, 255, 0)
green = (0, 255, 0)
cyan = (0, 255, 255)
blue = (0, 0, 255)
violet = (125, 0, 255)
magenta = (255, 0, 255)
black = (0, 0, 0)

# make counter object to keep track of game time
#   use this as a parameter to make new pipes, and guage speed
myCounter = 0

# sample text at top of screen
#   ...later a similar method will present the scores
font = pygame.font.SysFont("comicsansms",24)
text = font.render("hello, world", True, (0,128,0))


# make the circle that represents the flappy bird
# uses x and y position parameters
def makeCircle(x,y):
    pygame.draw.circle(game_display, yellow, (x,y), 25)

# make the pipes
# def makePipes():
    

# initialize the position of the bird, at middle of screen
# half the max screen dimensions (900, 900)
x = 450
y = 450
y_change = 0
# Kinematics, Physics Estimates
gravity = 2
velocity_I = 0
flap = False
velocity_F = (velocity_I + gravity)


# while loop for the bird movement up/down
while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True
        # key down = FLAP UP
        if event.type == pygame.KEYDOWN:
            flap = True
        # key up = FALL
        if event.type == pygame.KEYUP:
            flap = False

    # bird flaps = boost velocity up with no gravity
    if flap == True:
        velocity_F = -20
        y_change = velocity_F
        velocity_I = velocity_F
    # no flap = fall with gravity
    elif flap == False:
        velocity_F = (velocity_I + gravity)
        y_change = velocity_F
        velocity_I = velocity_F
    # update the vertical position of the bird
    y += int(y_change)
    game_display.fill(black)
    makeCircle(x,y)
    pygame.draw.rect(game_display, green, (600,-600,100,800))
    pygame.draw.rect(game_display, green, (600, 400,100,800))
    game_display.blit(text,(300,10))
    myCounter += 1
    format_count = "myCounter: %d" % myCounter
    show_count = font.render(format_count, True, red)
    game_display.blit(show_count,(600,20))
    pygame.display.update()
    clock.tick(60)

  

pygame.quit()
quit()