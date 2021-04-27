import pygame
from fonctions import * 
from class_game import *
pygame.init()

game = game()

def choix_personnage(game,display_surface) :
    display_surface.blit(game.image['background_menu_jouer'],(0,0))
    display_surface.blit(game.image['choisir'],(80,50))

    