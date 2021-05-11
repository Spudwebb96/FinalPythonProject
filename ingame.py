from random import randint
import pygame
import class_game
import time
from fonctions import *
from class_game import *
pygame.init()

def in_game(game,curseur, display_surface):
    choix_background_local(game,display_surface)
    tour(game, display_surface)
    if game.player.Hp_J1 != 0 and game.player.Hp_J2 != 0 and game.menu_pause == False and game.menu_parametre == False:
        display_surface.blit(game.image['nuage_J1'], (20,87))
        display_surface.blit(game.image['nuage_J2'], (767,87))
        tableau_prop(game, display_surface)
        nuage(game, display_surface)
    barre_de_vie(game,display_surface)
    affichage_joueur(game, display_surface)
    if game.menu_parametre :
        parametres(game, display_surface)

    # Effet fond noir transparent
    if game.alpha != 0:
        fond_noir_surface = pygame.Surface((1440, 1024))
        fond_noir_surface.set_alpha(game.alpha)
        fond_noir_surface.fill((0, 0, 0))
        display_surface.blit(fond_noir_surface, (0, 0))
        game.alpha = game.alpha - 5

    if game.player.max_Hp_J2 == 0 or game.player.max_Hp_J1 == 0:
        display_surface.blit(game.image['fond_end'], (480, 230))
    hover_boutons(game, curseur, display_surface)


