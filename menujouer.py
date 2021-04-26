import pygame
import class_game
from fonctions import * 
from class_game import *
pygame.init()

game = game()

while game.is_running :

    display_surface.blit(game.image['background_menu'],(0,0)) # Trouver un autre BG

    