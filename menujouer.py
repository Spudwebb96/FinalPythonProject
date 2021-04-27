import pygame
import class_game
from fonctions import * 
from class_game import * # Pas besoin ?
pygame.init()

game = game()

while game.is_running :

    display_surface.blit(game.image['fond_menu_jouer'],(0,0)) 

    