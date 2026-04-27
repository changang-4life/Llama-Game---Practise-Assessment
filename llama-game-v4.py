""" Llama Game
v4 - Import Ground
"""

import pygame
import time

pygame.init() # initialises pygame so it's ready to use

llama = pygame.image.load("Llama.png")
llama_resized = pygame.transform.scale(llama, (70, 70))
ground = pygame.image.load("ground.png")
ground_resized = pygame.transform.scale(ground, (1100, 550)) # changes width and height of the ground (to match the screen window)
obstacle = pygame.image.load("cactus.png")

screen = pygame.display.set_mode((1100, 550)) # sets up the screen display

def game_loop():
    quit_game = False # variable name change from last version (stylistic purposes)

    while not quit_game: # white quit game = false
        # Variables v
        screen.fill("White") # fills the screen background with white
        screen.blit(llama_resized, (100, 355)) # displays the llama sprite at the set coordinates
        screen.blit(ground_resized, (0,100))

        # Executes if statements when certain events fire
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # when the user wants to clsoe the window
                quit_game = True

        pygame.display.update()

game_loop()

pygame.quit()
quit()
