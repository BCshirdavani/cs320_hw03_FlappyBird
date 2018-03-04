#======================================================
#
#   Author:         Beau Shirdavani
#   Date:           March 1, 2018
#   Description:    Flappy Bird with PyGame
#
#======================================================

# TODO:
#   add start button

import pygame
import random

pygame.init()

# set screen size
display_w = 900
display_h = 900
game_display = pygame.display.set_mode((display_w, display_h))
pygame.display.set_caption("pyGame Practice")

clock = pygame.time.Clock()
crashed = False

# define colors
white = (255, 255, 255)
red = (255, 0, 0)
orange = (255, 125, 0)
yellow = (255, 255, 0)
green = (0, 200, 0)
bright_green = (00, 255, 0)
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

# make the circle that represents the flappy bird
# uses x and y position parameters
def makeCircle(x,y):
    pygame.draw.circle(game_display, yellow, (x,y), 25)

# make the pipes
pipe_x = 900
pipe_y = 450
gap_y = 450
def makePipes(x, y):
    pygame.draw.rect(game_display, green, (x, y, 100 ,800))
    pygame.draw.rect(game_display, green, (x, (y - 1000), 100 ,800))
    gap_y = y

# random numbers for vertical position of pipe gap
rand = random.Random()

# initialize the position of the bird, at middle of screen
# half the max screen dimensions (900, 900)
x = 450
y = 450
y_change = 0
x_dist = int(pipe_x - x)
y_dist = int(pipe_y - y)
score = 0
# Kinematics, Physics Estimates
gravity = 2
velocity_I = 0
flap = False
velocity_F = (velocity_I + gravity)

# intro screen function with start button
def text_objects(text, font):
    textSurface = font.render(text, True, white)
    return textSurface, textSurface.get_rect()

intro = True









# while loop for the bird movement up/down
while not crashed:

    #-----------------------------------------------------------------  intro screen
    # game intro screen was pasted in here because the function call 
    # implementation of it was causing problems...
    mouse_pos = pos = pygame.mouse.get_pos()
    pressed1, pressed2, pressed3 = pygame.mouse.get_pressed()
    
    while intro:
        for event in pygame.event.get():
            # print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        game_display.fill(black)
        largeText = pygame.font.Font('freesansbold.ttf',115)
        TextSurf, TextRect = text_objects("Flappy Bird", largeText)
        TextRect.center = ((display_w/2),(display_h/2))
        game_display.blit(TextSurf, TextRect)

        mouse = pygame.mouse.get_pos()

        if 400+100 > mouse[0] > 400 and 550+50 > mouse[1] > 550:
            pygame.draw.rect(game_display, bright_green,(400,550,100,50))
            if pressed1:
                intro = False
                # return
            if event.type == pygame.MOUSEBUTTONDOWN:
                intro = False
                # return
        else:
            pygame.draw.rect(game_display, green,(400,550,100,50))

        smallText = pygame.font.Font("freesansbold.ttf",20)
        textSurf, textRect = text_objects("GO!", smallText)
        textRect.center = ( (400+(100/2)), (550+(50/2)) )
        game_display.blit(textSurf, textRect)
        pygame.display.update()
        clock.tick(60)
        #-----------------------------------------------------------------  intro screen


    #-----------------------------------------------------------------  game loop 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True
        # key down = FLAP UP
        if event.type == pygame.KEYDOWN:
            flap = True
        # key up = FALL
        if event.type == pygame.KEYUP:
            flap = False

    # collision detection
    x_dist = int(pipe_x - x)
    y_dist = int(pipe_y - y)
    if x_dist <= 0 and x_dist >= -100:
        # collision event
        if (pipe_y - y) >= 0 and (pipe_y - y) <= 200:
            crashed = False
        elif (pipe_y - y) < 0 or (pipe_y - y) > 200:
            crashed = True
    if y > 900 or y < 0:
        crashed = True


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
    # draw new bird position
    makeCircle(x,y)
    # draw piped to screen
    makePipes(pipe_x, pipe_y)
    # update pipe scrolling left location
    pipe_x -= 10
    # when pipe is off screen, restart pipe scroll from right again
    if pipe_x < -100:
        pipe_x = 900
        pipe_y = gap_y = rand.uniform(100, 700)
        score += 1
    # pygame.draw.rect(game_display, green, (600,-600,100,800))
    # pygame.draw.rect(game_display, green, (600, 400,100,800))
    # game_display.blit(text,(300,10))
    myCounter += 1
    # print points to screen
    format_count = "POINTS: %d" % score
    show_count = font.render(format_count, True, red)
    # print locations to screen
    # locations = "bird x: %d x_dist: %d \n brid y: %d y_dist: %x pipeY: %d gapAT: %d" % (x, x_dist, y, y_dist, pipe_y, gap_y)
    # show_locations = font.render(locations, True, red)


    game_display.blit(show_count,(600,20))
    # game_display.blit(show_locations,(0,500))
    pygame.display.update()
    clock.tick(60)
    #-----------------------------------------------------------------  game loop



  

pygame.quit()
quit()

















