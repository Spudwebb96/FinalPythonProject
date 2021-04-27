import pygame
from fonctions import * 
from class_game import *
pygame.init()

game = game()

def choix_personnage(game,display_surface) :
    display_surface.blit(game.image['background_menu_jouer'],(0,0))
    display_surface.blit(game.image['bouton_retour'], (80, 20))
    display_surface.blit(game.image['choisir'],(0,68))
    display_surface.blit(game.image['jouer_off'], (550, 452))
    display_surface.blit(game.image['pret_off'], (198, 900))
    display_surface.blit(game.image['pret_off'], (1028, 900))


    position_cards_J1 = [80, 190]
    position_cards_J2 = [910, 193]
    carroussel_perso(display_surface, position_cards_J1, position_cards_J2)

    display_surface.blit(game.image['fleche_gauche'], (105, 806))
    display_surface.blit(game.image['fleche_gauche'], (935, 806))
    display_surface.blit(game.image['fleche_droite'], (465, 806))
    display_surface.blit(game.image['fleche_droite'], (1295, 806))





def carroussel_perso(display_surface,position_cards_J1,position_cards_J2):
    if game.legends_J1 == 1:
        display_surface.blit(game.image['bigband_J1_off'], (position_cards_J1[0], position_cards_J1[1]))
    elif game.legends_J1 == 2:
        display_surface.blit(game.image['isis_J1_off'], (position_cards_J1[0], position_cards_J1[1]))
    elif game.legends_J1 == 3:
        display_surface.blit(game.image['gunnar_J1_off'], (position_cards_J1[0], position_cards_J1[1]))
    elif game.legends_J1 == 4:
        display_surface.blit(game.image['kitt_J1_off'], (position_cards_J1[0], position_cards_J1[1]))
    elif game.legends_J1 == 5:
        display_surface.blit(game.image['harry_J1_off'], (position_cards_J1[0], position_cards_J1[1]))
    else:
        display_surface.blit(game.image['lucie_J1_off'], (position_cards_J1[0], position_cards_J1[1]))

    if game.legends_J2 == 1:
        display_surface.blit(game.image['bigband_J2_off'], (position_cards_J2[0], position_cards_J2[1]))
    elif game.legends_J2 == 2:
        display_surface.blit(game.image['isis_J2_off'], (position_cards_J2[0], position_cards_J2[1]))
    elif game.legends_J2 == 3:
        display_surface.blit(game.image['gunnar_J2_off'], (position_cards_J2[0], position_cards_J2[1]))
    elif game.legends_J2 == 4:
        display_surface.blit(game.image['kitt_J2_off'], (position_cards_J2[0], position_cards_J2[1]))
    elif game.legends_J2 == 5:
        display_surface.blit(game.image['harry_J2_off'], (position_cards_J2[0], position_cards_J2[1]))
    else:
        display_surface.blit(game.image['lucie_J2_off'], (position_cards_J2[0], position_cards_J2[1]))




