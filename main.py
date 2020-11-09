import pygame
import os

# setup display
pygame.init()
win = WIDTH, HEIGHT = 800, 500
pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Hangman game !")

# load images
images = 
# setup game loop
FPS = 60
clock = pygame.time.Clock(FPS)
run = True

while run:
    clock.tick(FPS)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygam.mouse.get_pos()
            print(pos)
pygame.quit()
