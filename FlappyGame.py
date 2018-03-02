#======================================================
#
#   Author:         Beau Shirdavani
#   Date:           March 1, 2018
#   Description:    Flappy Bird with PyGame
#
#======================================================

import pygame

pygame.init()

game_display = pygame.display.set_mode((900,900))
pygame.display.set_caption("pyGame Practice")

clock = pygame.time.Clock()
crashed = False

white = (255, 255, 255)
blue = (0, 0, 255)

font = pygame.font.SysFont("comicsansms",24)
text = font.render("hello, world", True, (0,128,0))


# pygame.draw.circle(gameDisplay, white, (x,y), 75)

def makeCircle(x,y):
    pygame.draw.circle(game_display, blue, (x,y), 75)

x = 450
y = 450
y_change = 0

while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True
        if event.type == pygame.KEYDOWN:
            # if event.key == pygame.K_LEFT:
                y_change = -5
            # elif event.key == pygame.K_RIGHT:
                # y_change = +5
        if event.type == pygame.KEYUP:
            # if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                y_change = +5
    y += y_change
    game_display.fill(white)
    makeCircle(x,y)
    game_display.blit(text,(300,10))
    pygame.display.update()
    clock.tick(60)

  

pygame.quit()
quit()