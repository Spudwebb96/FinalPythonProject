import pygame
from ingame import *
from menu import *
from choix_legends import *
from fonctions import *
from class_game import *
from pygame import mixer 

pygame.init()
mixer.init()
mixer.music.load('assets/son/musique.wav')
mixer.music.set_volume(0.01)
mixer.music.play()

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
game.image['fleche_regles_1'] = pygame.transform.scale(game.image['fleche_regles_1'], (30, 37))
game.image['fleche_regles_2'] = pygame.transform.scale(game.image['fleche_regles_2'], (30, 37))


# create rect
for key in game.rect:
    game.rect[key]

### POSITION RECT
# Menu
position_rect(game.rect['bouton_jouer_hover_rect'],664, 570)
position_rect(game.rect['bouton_regles_hover_rect'],652, 651)
position_rect(game.rect['bouton_parametres_hover_rect'],606.5, 736)
position_rect(game.rect['bouton_quitter_hover_rect'],646, 811)
position_rect(game.rect['bouton_fermer_rect'], 1319, 465)
position_rect(game.rect['bouton_regles_1'], 1325, 902)
position_rect(game.rect['bouton_regles_2'], 1223, 902)
# Choix legends
position_rect(game.rect['bouton_retour_rect'], 80, 20)
position_rect(game.rect['jouer_rect'], 550, 452)
position_rect(game.rect['pret_rect_J1'], 198, 900)
position_rect(game.rect['pret_rect_J2'], 1028, 900)
position_rect(game.rect['fleche_gauche_rect_J1'], 105, 806)
position_rect(game.rect['fleche_gauche_rect_J2'], 935, 806)
position_rect(game.rect['fleche_droite_rect_J1'], 465, 806)
position_rect(game.rect['fleche_droite_rect_J2'], 1295, 806)
# Infos legends
position_rect(game.rect['bouton_infos_j1'], 100, 210)
position_rect(game.rect['bouton_infos_j2'], 1305, 210)
position_rect(game.rect['bouton_fermer_infos_j1'], 492, 204)
position_rect(game.rect['bouton_fermer_infos_j2'], 926, 204)

while game.is_running:

    curseur = pygame.mouse.get_pos()
    pygame.mouse.set_visible(False)

    if game.in_menu:
        menu(game,curseur, display_surface)
    elif game.in_choix_legends:
        choix_legends(game,curseur,display_surface)
    elif game.in_game:
            in_game(game,display_surface)

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
                    elif game.rect['bouton_regles_1'].collidepoint(event.pos):
                        game.menu_regles_page = 2
                    elif game.rect['bouton_regles_2'].collidepoint(event.pos):
                        game.menu_regles_page = 1
            elif game.in_choix_legends:

                # Bouton retour
                if game.rect['bouton_retour_rect'].collidepoint(event.pos):
                    game.in_choix_legends = False
                    game.in_menu = True
                    game.pret_J1 = False
                    game.pret_J2 = False
                    game.infos_legends_j1 = False
                    game.infos_legends_j2 = False


                # Boutons pret
                if game.infos_legends_j1 == False:
                    if game.rect['pret_rect_J1'].collidepoint(event.pos):
                        if game.pret_J1:
                            game.pret_J1 = False
                        else:
                            game.pret_J1 = True
                if game.infos_legends_j2 == False:
                    if game.rect['pret_rect_J2'].collidepoint(event.pos):
                        if game.pret_J2:
                            game.pret_J2 = False
                        else:
                            game.pret_J2 = True

                # Boutons infos
                if game.pret_J1 == False :
                    if game.rect['bouton_infos_j1'].collidepoint(event.pos):
                        game.infos_legends_j1 = True
                    if game.rect['bouton_fermer_infos_j1'].collidepoint(event.pos):
                        game.infos_legends_j1 = False
                if game.pret_J2 == False:
                    if game.rect['bouton_infos_j2'].collidepoint(event.pos):
                        game.infos_legends_j2 = True
                    if game.rect['bouton_fermer_infos_j2'].collidepoint(event.pos):
                        game.infos_legends_j2 = False
                    

                # Bouton jouer
                if game.pret_J1 and game.pret_J2:
                    if game.rect['jouer_rect'].collidepoint(event.pos):
                        game.player.legends_J1 = game.list_legends[game.menu_legends_J1]
                        game.player.legends_J2 = game.list_legends[game.menu_legends_J2]
                        game.player.faiblesse_J1 = game.stats[game.player.legends_J1]
                        game.player.faiblesse_J2 = game.stats[game.player.legends_J2]
                        print(game.player.legends_J1, game.player.legends_J2)
                        game.in_choix_legends = False
                        game.in_game = True
                        game.stage_select = randint(1,6)
                        print("bouton jouer fonctionne")

                # Carrousel
                if game.rect['fleche_gauche_rect_J1'].collidepoint(event.pos) and game.pret_J1 == False:
                    if game.menu_legends_J1 != 0:
                        game.menu_legends_J1 = game.menu_legends_J1 - 1
                    else:
                        game.menu_legends_J1 = 5
                elif game.rect['fleche_droite_rect_J1'].collidepoint(event.pos) and game.pret_J1 == False:
                    if game.menu_legends_J1 != 5:
                        game.menu_legends_J1 = game.menu_legends_J1 + 1
                    else:
                        game.menu_legends_J1 = 0

                if game.rect['fleche_gauche_rect_J2'].collidepoint(event.pos) and game.pret_J2 == False:
                    if game.menu_legends_J2 != 0:
                        game.menu_legends_J2 = game.menu_legends_J2 - 1
                    else:
                        game.menu_legends_J2 = 5
                elif game.rect['fleche_droite_rect_J2'].collidepoint(event.pos) and game.pret_J2 == False:
                    if game.menu_legends_J2 != 5:
                        game.menu_legends_J2 = game.menu_legends_J2 + 1
                    else:
                        game.menu_legends_J2 = 0


        else:
            game.mouse = False

    frame_per_sec.tick(60)
    