import pygame
from menu import *
from choix_legends import *
from fonctions import *
from class_game import *



pygame.init()

frame_per_sec = pygame.time.Clock()

display_surface = pygame.display.set_mode((1440,1024))

pygame.display.set_caption("Words Legends")

game = game()

# Load Image
for key in game.image:
    game.image[key]
# transform scale Image
game.image['image_curseur'] = pygame.transform.scale(game.image['image_curseur'], (36, 57))
game.image['image_curseur_click'] = pygame.transform.scale(game.image['image_curseur_click'], (36, 57))

# create rect
for key in game.rect:
    game.rect[key]
# change position rect
position_rect(game.rect['bouton_jouer_hover_rect'],664, 570)
position_rect(game.rect['bouton_regles_hover_rect'],652, 651)
position_rect(game.rect['bouton_parametres_hover_rect'],606.5, 736)
position_rect(game.rect['bouton_quitter_hover_rect'],646, 811)
position_rect(game.rect['bouton_fermer_rect'], 1319, 465)

while game.is_running:

    curseur = pygame.mouse.get_pos()
    pygame.mouse.set_visible(False)

    if game.in_menu:
        menu(game,curseur, display_surface)
    elif game.in_choix_legends:
        choix_personnage(game,display_surface)

    # Changement du curseur
    if game.mouse:
        display_surface.blit(game.image['image_curseur_click'], (curseur[0],curseur[1]))
    else :
        display_surface.blit(game.image['image_curseur'],(curseur[0],curseur[1]))

    pygame.display.update()

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            game.is_running = False
            pygame.quit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            game.mouse = True
            if game.in_menu:
                if game.menu_regles == False:
                    if game.rect['bouton_jouer_hover_rect'].collidepoint(event.pos):
                        game.in_choix_legends = True
                        game.in_menu = False
                    elif game.rect['bouton_regles_hover_rect'].collidepoint(event.pos):
                        game.menu_regles = True
                    elif game.rect['bouton_parametres_hover_rect'].collidepoint(event.pos):
                        menu_parametres = True
                    elif game.rect['bouton_quitter_hover_rect'].collidepoint(event.pos):
                        game.is_running = False
                        pygame.quit()
                else:
                    if game.rect['bouton_fermer_rect'].collidepoint(event.pos):
                        game.menu_regles = False

        else:
            game.mouse = False

    frame_per_sec.tick(60)
    