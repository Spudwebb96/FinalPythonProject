import pygame
from ingame import *
from menu import *
from choix_legends import *
from fonctions import *
from class_game import *
from pygame import mixer 

pygame.init()
mixer.init()
pygame.mixer.Channel(0).set_volume(0.08)
pygame.mixer.Channel(0).play(pygame.mixer.Sound('assets/son/menu.wav'),-1)


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

while game.is_running:

    curseur = pygame.mouse.get_pos()
    pygame.mouse.set_visible(False)

    # Menu principal
    if game.in_menu:
        menu(game,curseur, display_surface)
        for key in game.rect_menu:
            game.rect_menu[key]
            for key in game.rect_position_menu:
                game.rect_position_menu[key]

    # Menu choix_legends
    elif game.in_choix_legends:
        choix_legends(game,curseur,display_surface)
        for key in game.rect_choix_legends:
            game.rect_choix_legends[key]
            for key in game.rect_position_choix_legends:
                game.rect_position_choix_legends[key]

    elif game.in_game:
        in_game(game,display_surface)
        for key in game.rect_ingame:
            game.rect_ingame[key]
        if game.player.p1_phrase[1] and game.player.p2_phrase[1]:
            Combat(game, 13, display_surface)


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

        elif event.type == pygame.MOUSEBUTTONDOWN:
            pygame.mixer.Channel(2).set_volume(0.05)
            pygame.mixer.Channel(2).play(pygame.mixer.Sound('assets/son/click.wav'))
            game.mouse = True
            # event dans le menu principal
            if game.in_menu:
                if game.menu_regles == False:
                    if game.rect_menu['bouton_jouer_hover_rect'].collidepoint(event.pos):
                        game.in_choix_legends = True
                        game.in_menu = False
                    elif game.rect_menu['bouton_regles_hover_rect'].collidepoint(event.pos):
                        game.menu_regles = True
                    elif game.rect_menu['bouton_parametres_hover_rect'].collidepoint(event.pos):
                        menu_parametres = True
                    elif game.rect_menu['bouton_quitter_hover_rect'].collidepoint(event.pos):
                        game.is_running = False
                        pygame.quit()
                else:
                    if game.rect_menu['bouton_fermer_rect'].collidepoint(event.pos):
                        game.menu_regles = False
                    elif game.rect_menu['bouton_regles_1'].collidepoint(event.pos):
                        game.menu_regles_page = 2
                    elif game.rect_menu['bouton_regles_2'].collidepoint(event.pos):
                        game.menu_regles_page = 1

            # event dans le menu choix legends
            elif game.in_choix_legends:
                # Bouton retour
                if game.rect_choix_legends['bouton_retour_rect'].collidepoint(event.pos):
                    game.in_choix_legends = False
                    game.in_menu = True
                    game.pret_J1 = False
                    game.pret_J2 = False
                    game.infos_legends_j1 = False
                    game.infos_legends_j2 = False


                # Boutons pret
                if game.infos_legends_j1 == False:
                    if game.rect_choix_legends['pret_rect_J1'].collidepoint(event.pos):
                        if game.pret_J1:
                            game.pret_J1 = False
                        else:
                            game.pret_J1 = True
                if game.infos_legends_j2 == False:
                    if game.rect_choix_legends['pret_rect_J2'].collidepoint(event.pos):
                        if game.pret_J2:
                            game.pret_J2 = False
                        else:
                            game.pret_J2 = True

                # Boutons infos
                if game.pret_J1 == False :
                    if game.rect_choix_legends['bouton_infos_j1'].collidepoint(event.pos):
                        game.infos_legends_j1 = True
                    if game.rect_choix_legends['bouton_fermer_infos_j1'].collidepoint(event.pos):
                        game.infos_legends_j1 = False
                if game.pret_J2 == False:
                    if game.rect_choix_legends['bouton_infos_j2'].collidepoint(event.pos):
                        game.infos_legends_j2 = True
                    if game.rect_choix_legends['bouton_fermer_infos_j2'].collidepoint(event.pos):
                        game.infos_legends_j2 = False
                    

                # Bouton jouer
                if game.pret_J1 and game.pret_J2:
                    if game.rect_choix_legends['jouer_rect'].collidepoint(event.pos):
                        game.player.legends_J1 = game.list_legends[game.menu_legends_J1]
                        game.player.legends_J2 = game.list_legends[game.menu_legends_J2]
                        game.player.faiblesse_J1 = game.stats[game.player.legends_J1]
                        game.player.faiblesse_J2 = game.stats[game.player.legends_J2]
                        game.in_choix_legends = False
                        game.in_game = True
                        game.stage_select = randint(1,6)
                        pygame.mixer.Channel(0).stop()

                        # Musiques stages
                        if game.stage_select == 1:
                            pygame.mixer.Channel(1).set_volume(0.06)
                            pygame.mixer.Channel(1).play(pygame.mixer.Sound('assets/son/isis_musique.wav'),-1)
                        elif game.stage_select == 2:
                            pygame.mixer.Channel(1).set_volume(0.04)
                            pygame.mixer.Channel(1).play(pygame.mixer.Sound('assets/son/gunnar_musique.wav'),-1)
                        elif game.stage_select == 3:
                            pygame.mixer.Channel(1).set_volume(0.05)
                            pygame.mixer.Channel(1).play(pygame.mixer.Sound('assets/son/bigband_musique.wav'),-1)
                        elif game.stage_select == 4:
                            pygame.mixer.Channel(1).set_volume(0.04)
                            pygame.mixer.Channel(1).play(pygame.mixer.Sound('assets/son/kitt_musique.wav'),-1)
                        elif game.stage_select == 5:
                            pygame.mixer.Channel(1).set_volume(0.06)
                            pygame.mixer.Channel(1).play(pygame.mixer.Sound('assets/son/harry_musique.wav'),-1)
                        else:
                            pygame.mixer.Channel(1).set_volume(0.06)
                            pygame.mixer.Channel(1).play(pygame.mixer.Sound('assets/son/lucie_musique.wav'),-1)


                # Carrousel
                if game.rect_choix_legends['fleche_gauche_rect_J1'].collidepoint(event.pos) and game.pret_J1 == False:
                    if game.menu_legends_J1 != 0:
                        game.menu_legends_J1 = game.menu_legends_J1 - 1
                    else:
                        game.menu_legends_J1 = 5
                elif game.rect_choix_legends['fleche_droite_rect_J1'].collidepoint(event.pos) and game.pret_J1 == False:
                    if game.menu_legends_J1 != 5:
                        game.menu_legends_J1 = game.menu_legends_J1 + 1
                    else:
                        game.menu_legends_J1 = 0

                if game.rect_choix_legends['fleche_gauche_rect_J2'].collidepoint(event.pos) and game.pret_J2 == False:
                    if game.menu_legends_J2 != 0:
                        game.menu_legends_J2 = game.menu_legends_J2 - 1
                    else:
                        game.menu_legends_J2 = 5
                elif game.rect_choix_legends['fleche_droite_rect_J2'].collidepoint(event.pos) and game.pret_J2 == False:
                    if game.menu_legends_J2 != 5:
                        game.menu_legends_J2 = game.menu_legends_J2 + 1
                    else:
                        game.menu_legends_J2 = 0

            elif game.in_game:
                if len(game.player.p1_phrase[0]) + len(game.player.p2_phrase[0]) < 10:
                    if game.rect_ingame['rect_1'].collidepoint(event.pos):
                        if game.rect_utilisé[0]:
                            Combat(game, 0, display_surface)
                            game.rect_utilisé[0] = False
                    elif game.rect_ingame['rect_2'].collidepoint(event.pos):
                        if game.rect_utilisé[1]:
                            Combat(game, 1, display_surface)
                            game.rect_utilisé[1] = False
                    elif game.rect_ingame['rect_3'].collidepoint(event.pos):
                        if game.rect_utilisé[2]:
                            Combat(game, 2, display_surface)
                            game.rect_utilisé[2] = False
                    elif game.rect_ingame['rect_4'].collidepoint(event.pos):
                        if game.rect_utilisé[3]:
                            Combat(game, 3, display_surface)
                            game.rect_utilisé[3] = False
                    elif game.rect_ingame['rect_5'].collidepoint(event.pos):
                        if game.rect_utilisé[4]:
                            Combat(game, 4, display_surface)
                            game.rect_utilisé[4] = False
                    elif game.rect_ingame['rect_6'].collidepoint(event.pos):
                        if game.rect_utilisé[5]:
                            Combat(game, 5, display_surface)
                            game.rect_utilisé[5] = False
                    elif game.rect_ingame['rect_7'].collidepoint(event.pos):
                        if game.rect_utilisé[6]:
                            Combat(game, 6, display_surface)
                            game.rect_utilisé[6] = False
                    elif game.rect_ingame['rect_8'].collidepoint(event.pos):
                        if game.rect_utilisé[7]:
                            Combat(game, 7, display_surface)
                            game.rect_utilisé[7] = False
                    elif game.rect_ingame['rect_9'].collidepoint(event.pos):
                        if game.rect_utilisé[8]:
                            Combat(game, 8, display_surface)
                            game.rect_utilisé[8] = False
                    elif game.rect_ingame['rect_10'].collidepoint(event.pos):
                        if game.rect_utilisé[9]:
                            Combat(game, 9, display_surface)
                            game.rect_utilisé[9] = False
                    elif game.rect_ingame['rect_11'].collidepoint(event.pos):
                        if game.rect_utilisé[10]:
                            Combat(game, 10, display_surface)
                            game.rect_utilisé[10] = False
                    elif game.rect_ingame['rect_12'].collidepoint(event.pos):
                        if game.rect_utilisé[11]:
                            Combat(game, 11, display_surface)
                            game.rect_utilisé[11] = False
                if game.rect_ingame['rect_13'].collidepoint(event.pos):
                        Combat(game, 12, display_surface)
                if game.rect_ingame['rect_14'].collidepoint(event.pos):
                    Combat(game ,13, display_surface)


        # Bouton clavier
        elif event.type == pygame.KEYDOWN:
            # Menu
            if game.in_menu == True:
                if event.key == pygame.K_ESCAPE:
                    game.menu_regles = False

            # Choix legends

            # In_game
            if game.in_game == True:
                if event.key == pygame.K_ESCAPE:
                    game.in_game = False
                    game.in_choix_legends = True
                    game.prop = []
                    game.sujets = game.sujetsref
                    game.verbes = game.verbesref
                    game.complement = game.complementref
                    game.liaison = game.liaisonref
                    pygame.mixer.Channel(0).play(pygame.mixer.Sound('assets/son/menu.wav'),-1)
                    pygame.mixer.Channel(1).stop()

        else:
            game.mouse = False

    frame_per_sec.tick(60)
    