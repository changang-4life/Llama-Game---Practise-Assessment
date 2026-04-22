""" Llama Game
v3 - Obstacles
    > Cactus PNG
    > Beginning of the game loop functionality (for tests)
"""

import pygame
import time

pygame.init() # initialises pygame so it's ready to use

llama_sprite = pygame.image.load("Llama.png")
screen = pygame.display.set_mode((1100, 550)) # sets up the screen display

obstacle = pygame.image.load("cactus.png")


def game_loop():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # when user wants to close out the window
                running = False 

        screen.blit(llama_sprite, (100, 100)) # displays the llama sprite
        screen.blit(obstacle, (150, 150)) # displays the cactus obstacle

        pygame.display.update()

game_loop()

pygame.quit()
quit()
