import pygame
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
Position_rect(game.rect['bouton_jouer_hover_rect'],664, 570)
Position_rect(game.rect['bouton_regles_hover_rect'],652, 651)
Position_rect(game.rect['bouton_parametres_hover_rect'],606.5, 736)
Position_rect(game.rect['bouton_quitter_hover_rect'],646, 811)
Position_rect(game.rect['bouton_fermer_rect'], 1319, 465)

while game.is_running:

    display_surface.blit(game.image['background_menu'],(0,0))

    curseur = pygame.mouse.get_pos()
    pygame.mouse.set_visible(False)

    # Fonction hover boutons menu
    hover_boutons(curseur, display_surface)

    if game.menu_regles:
        display_surface.blit(game.image['fond_regles'],(60,440))
        
        display_surface.blit(game.image['bouton_fermer'],(1319,465))

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
            if game.menu_regles == False:
                if game.rect['bouton_jouer_hover_rect'].collidepoint(event.pos):
                    menu_jouer = True
                elif game.rect['bouton_regles_hover_rect'].collidepoint(event.pos):
                    game.menu_regles = True
                elif game.rect['bouton_parametres_hover_rect'].collidepoint(event.pos):
                    menu_parametres = True
                elif game.rect['bouton_quitter_hover_rect'].collidepoint(event.pos):
                    game.is_running = False
                    pygame.quit()
            else:
                if game.rect['bouton_fermer_rect'].collidepoint(event.pos):
                    game.menu_regles = True

            '''# TEST SON CLICK ( liée au test dictionnaire de sons dans le dossier fonctions ) 
            fonctions.sounds.play('click')'''

        else :
            game.mouse = False

    frame_per_sec.tick(60)
    