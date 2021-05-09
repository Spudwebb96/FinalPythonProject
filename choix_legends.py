import pygame
from fonctions import * 
from class_game import *
pygame.init()

def choix_legends(game,curseur,display_surface) :
    display_surface.blit(game.image['background_menu_jouer'],(0,0))
    display_surface.blit(game.image['bouton_retour'], (80, 20))
    display_surface.blit(game.image['choisir'],(0,68))

    if game.pret_J1:
        display_surface.blit(game.image['pret_on'], (198, 900))
    else:
        display_surface.blit(game.image['pret_off'], (198, 900))

    if game.pret_J2:
        display_surface.blit(game.image['pret_on'], (1028, 900))
    else:
        display_surface.blit(game.image['pret_off'], (1028, 900))

    hover_boutons(game, curseur, display_surface)

    position_cards_J1 = [80, 190]
    position_cards_J2 = [910, 193]
    carroussel_perso(game,display_surface, position_cards_J1, position_cards_J2)

    if game.pret_J1 == False:
        display_surface.blit(game.image['fleche_gauche'], (105, 806))
        display_surface.blit(game.image['fleche_droite'], (465, 806))
    if game.infos_legends_j1 == True:
        display_surface.blit(game.image['bouton_fermer_infos'], (492, 204))
        display_surface.blit(game.image['fleche_gauche_info'], (105, 806))
        display_surface.blit(game.image['fleche_droite_info'], (465, 806))
    if game.pret_J2 == False:
        display_surface.blit(game.image['fleche_gauche'], (935, 806))
        display_surface.blit(game.image['fleche_droite'], (1295, 806))
    if game.infos_legends_j2 == True:
        display_surface.blit(game.image['bouton_fermer_infos'], (926, 204))
        display_surface.blit(game.image['fleche_gauche_info'], (935, 806))
        display_surface.blit(game.image['fleche_droite_info'], (1295, 806))
