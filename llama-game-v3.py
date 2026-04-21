""" Llama Game
v3 - Running the Game
"""

import pygame
import time

pygame.init() # initialises pygame so it's ready to use

llama_sprite = pygame.image.load("Llama.png")
screen = pygame.display.set_mode((1100, 550)) # sets up the screen display

def game_loop():
    screen.blit(llama_sprite, 100, 100)
    
time.sleep(10) # wait period for testing purposes

game_loop()

pygame.quit()
quit()
