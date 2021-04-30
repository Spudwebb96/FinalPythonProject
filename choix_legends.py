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

    if game.pret_J1 == False and game.infos_legends_j1 == False:
        display_surface.blit(game.image['fleche_gauche'], (105, 806))
        display_surface.blit(game.image['fleche_droite'], (465, 806))
    else:
        display_surface.blit(game.image['bouton_fermer_infos'], (492, 204))
    if game.pret_J2 == False and game.infos_legends_j2 == False:
        display_surface.blit(game.image['fleche_gauche'], (935, 806))
        display_surface.blit(game.image['fleche_droite'], (1295, 806))
    else:
        display_surface.blit(game.image['bouton_fermer_infos'], (1322, 204))



def carroussel_perso(game,display_surface,position_cards_J1,position_cards_J2):

    # cards J1
    if game.menu_legends_J1 == 0:
        if game.infos_legends_j1 == False :
            if game.pret_J1:
                display_surface.blit(game.image['bigband_J1_on'], (position_cards_J1[0], position_cards_J1[1]))
            else:
                display_surface.blit(game.image['bigband_J1_off'], (position_cards_J1[0], position_cards_J1[1]))
        else:
            display_surface.blit(game.image['bigband_infos'], (position_cards_J1[0], position_cards_J1[1]))
    elif game.menu_legends_J1 == 1:
        if game.infos_legends_j1 == False :
            if game.pret_J1:
                display_surface.blit(game.image['isis_J1_on'], (position_cards_J1[0], position_cards_J1[1]))
            else:
                display_surface.blit(game.image['isis_J1_off'], (position_cards_J1[0], position_cards_J1[1]))
        else:
            display_surface.blit(game.image['isis_infos'], (position_cards_J1[0], position_cards_J1[1]))
    elif game.menu_legends_J1 == 2:
        if game.infos_legends_j1 == False :
            if game.pret_J1:
                display_surface.blit(game.image['gunnar_J1_on'], (position_cards_J1[0], position_cards_J1[1]))
            else:
                display_surface.blit(game.image['gunnar_J1_off'], (position_cards_J1[0], position_cards_J1[1]))
        else:
            display_surface.blit(game.image['isis_infos'], (position_cards_J1[0], position_cards_J1[1]))

    elif game.menu_legends_J1 == 3:
        if game.infos_legends_j1 == False :
            if game.pret_J1:
                display_surface.blit(game.image['kitt_J1_on'], (position_cards_J1[0], position_cards_J1[1]))
            else:
                display_surface.blit(game.image['kitt_J1_off'], (position_cards_J1[0], position_cards_J1[1]))
        else:
            display_surface.blit(game.image['kitt_infos'], (position_cards_J1[0], position_cards_J1[1]))
    elif game.menu_legends_J1 == 4:
        if game.infos_legends_j1 == False :
            if game.pret_J1:
                display_surface.blit(game.image['harry_J1_on'], (position_cards_J1[0], position_cards_J1[1]))
            else:
                display_surface.blit(game.image['harry_J1_off'], (position_cards_J1[0], position_cards_J1[1]))
        else:
            display_surface.blit(game.image['harry_infos'], (position_cards_J1[0], position_cards_J1[1]))
    else:
        if game.infos_legends_j1 == False :
            if game.pret_J1:
                display_surface.blit(game.image['lucie_J1_on'], (position_cards_J1[0], position_cards_J1[1]))
            else:
                display_surface.blit(game.image['lucie_J1_off'], (position_cards_J1[0], position_cards_J1[1]))
        else:
            display_surface.blit(game.image['harry_infos'], (position_cards_J1[0], position_cards_J1[1]))

    if game.infos_legends_j1 == False:       
        display_surface.blit(game.image['bouton_infos_j1'], (100, 210))


    #cards J2
    if game.menu_legends_J2 == 0:
        if game.infos_legends_j2 == False :
            if game.pret_J2:
                display_surface.blit(game.image['bigband_J2_on'], (position_cards_J2[0], position_cards_J2[1]))
            else:
                display_surface.blit(game.image['bigband_J2_off'], (position_cards_J2[0], position_cards_J2[1]))
        else:
            display_surface.blit(game.image['bigband_infos'], (position_cards_J2[0], position_cards_J2[1]))
    elif game.menu_legends_J2 == 1:
        if game.infos_legends_j2 == False:
            if game.pret_J2:
                display_surface.blit(game.image['isis_J2_on'], (position_cards_J2[0], position_cards_J2[1]))
            else:
                display_surface.blit(game.image['isis_J2_off'], (position_cards_J2[0], position_cards_J2[1]))
        else:
            display_surface.blit(game.image['isis_infos'], (position_cards_J2[0], position_cards_J2[1])) 
    elif game.menu_legends_J2 == 2:
        if game.infos_legends_j2 == False:
            if game.pret_J2:    
                display_surface.blit(game.image['gunnar_J2_on'], (position_cards_J2[0], position_cards_J2[1]))
            else:
                display_surface.blit(game.image['gunnar_J2_off'], (position_cards_J2[0], position_cards_J2[1]))
        else:
            display_surface.blit(game.image['gunnar_infos'], (position_cards_J2[0], position_cards_J2[1]))               
    elif game.menu_legends_J2 == 3:
        if game.infos_legends_j2 == False:
            if game.pret_J2:
                display_surface.blit(game.image['kitt_J2_on'], (position_cards_J2[0], position_cards_J2[1]))
            else:
                display_surface.blit(game.image['kitt_J2_off'], (position_cards_J2[0], position_cards_J2[1]))
        else:
            display_surface.blit(game.image['kitt_infos'], (position_cards_J2[0], position_cards_J2[1]))               
    elif game.menu_legends_J2 == 4:
        if game.infos_legends_j2 == False:
            if game.pret_J2:
                display_surface.blit(game.image['harry_J2_on'], (position_cards_J2[0], position_cards_J2[1]))
            else:
                display_surface.blit(game.image['harry_J2_off'], (position_cards_J2[0], position_cards_J2[1]))
        else:
            display_surface.blit(game.image['harry_infos'], (position_cards_J2[0], position_cards_J2[1]))               
    else:
        if game.infos_legends_j2 == False:
            if game.pret_J2:
                display_surface.blit(game.image['lucie_J2_on'], (position_cards_J2[0], position_cards_J2[1]))
            else:
                display_surface.blit(game.image['lucie_J2_off'], (position_cards_J2[0], position_cards_J2[1]))
        else:
            display_surface.blit(game.image['lucie_infos'], (position_cards_J2[0], position_cards_J2[1]))      
    if game.infos_legends_j2 == False:
        display_surface.blit(game.image['bouton_infos_j2'], (1305, 210))