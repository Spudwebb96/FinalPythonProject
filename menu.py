import pygame
from fonctions import *
pygame.init()

def menu(game,curseur, display_surface):
    display_surface.blit(game.image['background_menu'], (0, 0))

    # Fonction hover boutons menu
    hover_boutons(game,curseur, display_surface)

    # Affichage des regles
    if game.menu_regles:
        if game.menu_regles_page == 1:
            display_surface.blit(game.image['fond_regles_1'], (60, 440))
            display_surface.blit(game.image['fleche_regles_1'], (1325, 902))

        elif game.menu_regles_page == 2:
            display_surface.blit(game.image['fond_regles_2'], (60, 440))
            display_surface.blit(game.image['fleche_regles_2'], (1223, 902))
        display_surface.blit(game.image['bouton_fermer'], (1319, 465))

    # Faire l'onglet parametre