import pygame
from ingame import *
from menu import *
from choix_legends import *
from fonctions import *
from class_game import *
from pygame import mixer 

pygame.init()
mixer.init()

frame_per_sec = pygame.time.Clock()

display_surface = pygame.display.set_mode((1440,1024))

'''icon = pygame.image.load("assets/image/test_logo.png")
pygame.display.set_icon(icon)'''

pygame.display.set_caption("Words Legends",)

game = game()

pygame.mixer.Channel(0).set_volume(game.musique)
pygame.mixer.Channel(0).play(pygame.mixer.Sound('assets/son/menu.wav'),-1)

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

    pygame.mixer.Channel(0).set_volume(game.musique)
    pygame.mixer.Channel(1).set_volume(game.effet_sonore)
    pygame.mixer.Channel(2).set_volume(game.effet_sonore)

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
        in_game(game,curseur,display_surface)
        for key in game.rect_ingame:
            game.rect_ingame[key]
        for key in game.rect_position_ingame:
            game.rect_position_ingame[key]
        if game.player.p1_phrase[1] and game.player.p2_phrase[1]:
            Combat(game, 13, display_surface)


    # Changement du curseur
    if game.mouse:
        display_surface.blit(game.image['image_curseur_click'], (curseur[0],curseur[1]))
    else :
        display_surface.blit(game.image['image_curseur'],(curseur[0],curseur[1]))

    luminosite(game, display_surface)

    pygame.display.update()

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            game.is_running = False
            pygame.quit()

        # Click sur rect
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pygame.mixer.Channel(2).play(pygame.mixer.Sound('assets/son/effet sonore/click.wav'))
            game.mouse = True
            # dans le menu principal
            if game.in_menu:
                if game.menu_regles == False and game.menu_parametre == False:
                    if game.rect_menu['bouton_jouer_hover_rect'].collidepoint(event.pos):
                        pygame.mixer.Channel(1).play(pygame.mixer.Sound('assets/son/effet sonore/effet click button.wav'))
                        game.in_choix_legends = True
                        game.in_menu = False
                    elif game.rect_menu['bouton_regles_hover_rect'].collidepoint(event.pos):
                        pygame.mixer.Channel(1).play(pygame.mixer.Sound('assets/son/effet sonore/effet click button.wav'))
                        game.menu_regles = True
                    elif game.rect_menu['bouton_parametres_hover_rect'].collidepoint(event.pos):
                        game.menu_parametre = True
                        pygame.mixer.Channel(1).play(pygame.mixer.Sound('assets/son/effet sonore/effet click button.wav'))
                        game.menu_parametres = True
                    elif game.rect_menu['bouton_quitter_hover_rect'].collidepoint(event.pos):
                        game.is_running = False
                        pygame.quit()
                elif game.menu_regles:
                    if game.rect_menu['bouton_fermer_rect'].collidepoint(event.pos):
                        game.menu_regles = False
                    elif game.rect_menu['bouton_regles_1'].collidepoint(event.pos):
                        game.menu_regles_page = 2
                    elif game.rect_menu['bouton_regles_2'].collidepoint(event.pos):
                        game.menu_regles_page = 1
                elif game.menu_parametre:
                    if game.rect_menu['moins_1'].collidepoint(event.pos) and game.musique != 0:
                        game.musique -= 0.1
                        if game.musique < 0.05 :
                            game.musique = 0
                    elif game.rect_menu['moins_2'].collidepoint(event.pos) and game.effet_sonore != 0:
                        game.effet_sonore -= 0.1
                        if game.effet_sonore < 0.05 :
                            game.effet_sonore = 0
                    elif game.rect_menu['moins_3'].collidepoint(event.pos) and game.luminosite != 0:
                        game.luminosite -= 20

                    elif game.rect_menu['plus_1'].collidepoint(event.pos) and game.musique != 1:
                        game.musique = game.musique + 0.1
                        if game.musique > 0.79 and game.musique < 0.8 :
                            game.musique = 0.8
                        elif game.musique > 0.89 and game.musique < 0.9:
                            game.musique = 0.9
                        elif game.musique > 0.99 :
                            game.musique = 1
                    elif game.rect_menu['plus_2'].collidepoint(event.pos) and game.effet_sonore != 1:

                        game.effet_sonore += 0.1
                        if game.effet_sonore > 0.79 and game.effet_sonore < 0.8 :
                            game.effet_sonore = 0.8
                        elif game.effet_sonore > 0.89 and game.effet_sonore < 0.9:
                            game.effet_sonore = 0.9
                        elif game.effet_sonore > 0.99 :
                            game.effet_sonore = 1
                    elif game.rect_menu['plus_3'].collidepoint(event.pos) and game.luminosite != 100:
                        game.luminosite += 20
                    elif game.rect_menu['bouton_fermer_parametre_rect'].collidepoint(event.pos) :
                        game.menu_parametre = False

            # dans le menu choix legends
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
                        musique_ingame(game)

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

            # Dans Ingame
            elif game.in_game:
                # tableau phrase :
                if game.menu_pause == False and game.menu_parametre == False:
                    if game.menu_pause == False or game.menu_parametre == False:
                        if (len(game.player.p1_phrase[0]) < 5  and game.player.p1_phrase[1] == False) or (len(game.player.p2_phrase[0]) < 5  and game.player.p2_phrase[1] == False):
                            if game.player.p1_phrase[1] == False or game.player.p2_phrase[1] == False:
                                if game.rect_ingame['rect_1'].collidepoint(event.pos):
                                    if game.rect_utilise[0]:
                                        Combat(game, 0, display_surface)
                                        game.rect_utilise[0] = False
                                elif game.rect_ingame['rect_2'].collidepoint(event.pos):
                                    if game.rect_utilise[1]:
                                        Combat(game, 1, display_surface)
                                        game.rect_utilise[1] = False
                                elif game.rect_ingame['rect_3'].collidepoint(event.pos):
                                    if game.rect_utilise[2]:
                                        Combat(game, 2, display_surface)
                                        game.rect_utilise[2] = False
                                elif game.rect_ingame['rect_4'].collidepoint(event.pos):
                                    if game.rect_utilise[3]:
                                        Combat(game, 3, display_surface)
                                        game.rect_utilise[3] = False
                                elif game.rect_ingame['rect_5'].collidepoint(event.pos):
                                    if game.rect_utilise[4]:
                                        Combat(game, 4, display_surface)
                                        game.rect_utilise[4] = False
                                elif game.rect_ingame['rect_6'].collidepoint(event.pos):
                                    if game.rect_utilise[5]:
                                        Combat(game, 5, display_surface)
                                        game.rect_utilise[5] = False
                                elif game.rect_ingame['rect_7'].collidepoint(event.pos):
                                    if game.rect_utilise[6]:
                                        Combat(game, 6, display_surface)
                                        game.rect_utilise[6] = False
                                elif game.rect_ingame['rect_8'].collidepoint(event.pos):
                                    if game.rect_utilise[7]:
                                        Combat(game, 7, display_surface)
                                        game.rect_utilise[7] = False
                                elif game.rect_ingame['rect_9'].collidepoint(event.pos):
                                    if game.rect_utilise[8]:
                                        Combat(game, 8, display_surface)
                                        game.rect_utilise[8] = False
                                elif game.rect_ingame['rect_10'].collidepoint(event.pos):
                                    if game.rect_utilise[9]:
                                        Combat(game, 9, display_surface)
                                        game.rect_utilise[9] = False
                                elif game.rect_ingame['rect_11'].collidepoint(event.pos):
                                    if game.rect_utilise[10]:
                                        Combat(game, 10, display_surface)
                                        game.rect_utilise[10] = False
                                elif game.rect_ingame['rect_12'].collidepoint(event.pos):
                                    if game.rect_utilise[11]:
                                        Combat(game, 11, display_surface)
                                        game.rect_utilise[11] = False
                        if game.rect_ingame['rect_13'].collidepoint(event.pos):
                                Combat(game, 12, display_surface)
                        if game.rect_ingame['rect_14'].collidepoint(event.pos):
                            Combat(game ,13, display_surface)

                # Paremetres en pleine partie
                if game.menu_parametre:
                    if game.rect_menu['moins_1'].collidepoint(event.pos) and game.musique != 0:
                        game.musique -= 0.1
                        if game.musique < 0.05 :
                            game.musique = 0
                    elif game.rect_menu['moins_2'].collidepoint(event.pos) and game.effet_sonore != 0:
                        game.effet_sonore -= 0.1
                        if game.effet_sonore < 0.05 :
                            game.effet_sonore = 0
                    elif game.rect_menu['moins_3'].collidepoint(event.pos) and game.luminosite != 0:
                        game.luminosite -= 20

                    elif game.rect_menu['plus_1'].collidepoint(event.pos) and game.musique != 1:
                        game.musique = game.musique + 0.1
                        if game.musique > 0.79 and game.musique < 0.8 :
                            game.musique = 0.8
                        elif game.musique > 0.89 and game.musique < 0.9:
                            game.musique = 0.9
                        elif game.musique > 0.99 :
                            game.musique = 1
                    elif game.rect_menu['plus_2'].collidepoint(event.pos) and game.effet_sonore != 1:

                        game.effet_sonore += 0.1
                        if game.effet_sonore > 0.79 and game.effet_sonore < 0.8 :
                            game.effet_sonore = 0.8
                        elif game.effet_sonore > 0.89 and game.effet_sonore < 0.9:
                            game.effet_sonore = 0.9
                        elif game.effet_sonore > 0.99 :
                            game.effet_sonore = 1
                    elif game.rect_menu['plus_3'].collidepoint(event.pos) and game.luminosite != 100:
                        game.luminosite += 20
                    elif game.rect_menu['bouton_fermer_parametre_rect'].collidepoint(event.pos) :
                        game.menu_parametre = False
                        game.menu_pause = True

                # Boutons du menu pause
                elif game.menu_pause:
                    if game.rect_ingame['bouton_reprendre_hover_rect'].collidepoint(event.pos):
                        game.menu_pause = False
                        pygame.mixer.Channel(0).unpause()
                    elif game.rect_ingame['bouton_reset_hover_rect'].collidepoint(event.pos):
                        game.menu_pause = False
                        reset_match(game)
                        musique_ingame(game)
                    elif game.rect_ingame['bouton_retour_pause_hover_rect'].collidepoint(event.pos):
                        game.menu_pause = False
                        reset_match(game)
                        game.in_game = False
                        game.in_choix_legends = True
                        pygame.mixer.Channel(0).play(pygame.mixer.Sound('assets/son/menu.wav'), -1)
                    elif game.rect_ingame['bouton_parametres_pause_hover_rect'].collidepoint(event.pos):
                        game.menu_pause = False
                        game.menu_parametre = True
                    elif game.rect_ingame['bouton_quitter_pause_hover_rect'].collidepoint(event.pos):
                        pygame.mixer.Channel(0).play(pygame.mixer.Sound('assets/son/menu.wav'), -1)
                        game.menu_pause = False
                        game.in_game = False
                        reset_match(game)
                        game.in_menu = True

                elif game.player.max_Hp_J2 == 0 or game.player.max_Hp_J1 == 0:
                    if game.rect_ingame['non_hover_rect'].collidepoint(event.pos):
                        reset_match(game)
                        game.in_game = False
                        game.in_choix_legends = True
                    elif game.rect_ingame['oui_hover_rect'].collidepoint(event.pos):
                        reset_match(game)
                        musique_ingame(game)




        # Bouton clavier
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE: #bouton echap

                if game.in_menu :
                        game.menu_regles = False

                elif game.in_choix_legends :
                        pygame.mixer.Channel(1).play(pygame.mixer.Sound('assets/son/effet sonore/Sortie.wav'))
                        game.in_choix_legends = False
                        game.in_menu = True

                elif game.in_game :
                    if game.menu_pause and game.menu_parametre == False:
                        game.menu_pause = False
                        pygame.mixer.Channel(0).unpause()
                        pygame.mixer.Channel(1).unpause()
                    elif game.menu_pause == False and game.menu_parametre == False:
                        game.menu_pause = True
                        pygame.mixer.Channel(1).pause()
                        pygame.mixer.Channel(0).pause()

        else:
            game.mouse = False
    frame_per_sec.tick(60)
    