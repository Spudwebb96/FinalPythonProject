import pygame
from fonctions import *
pygame.init()

def menu(game,curseur, display_surface):
    display_surface.blit(game.image['background_menu'], (0, 0))

    # Fonction hover boutons menu
    hover_boutons(curseur, display_surface)

    # Affichage des regles
    if game.menu_regles:
        display_surface.blit(game.image['fond_regles'], (60, 440))
        display_surface.blit(game.image['bouton_fermer'], (1319, 465))


    # Faire l'onglet parametre