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
sqImage = pygame.image.load("square.png")

font = pygame.font.SysFont("comicsansms",24)
text = font.render("hello, world", True, (0,128,0))

def square(x, y):
    game_display.blit(sqImage, (x,y))

x = 10
y = 10
x_chage = 0

while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_chage = -5
            elif event.key == pygame.K_RIGHT:
                x_chage = +5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                x_change = 0
    x += x_chage
    game_display.fill(white)
    square(x,y)
    game_display.blit(text,(300,10))
    pygame.display.update()
    clock.tick(60)

  

pygame.quit()
quit()