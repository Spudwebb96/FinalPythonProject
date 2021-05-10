import pygame
from random import randint
from class_game import *
pygame.init()

### Fonction graphique
def hover_boutons(game,curseur,display_surface):
    if game.in_menu:
        if game.menu_regles == False:

            # Hover bouton "Jouer"
            if curseur[0] > 664 and curseur[0] < 776 and curseur[1] > 570 and curseur[1] < 611 :
                if game.son_hover[0] == False :
                    pygame.mixer.Channel(1).play(pygame.mixer.Sound('assets/son/effet sonore/hover.wav'))
                game.son_hover[0] = True
                display_surface.blit(game.image['bouton_jouer_hover'],(664,570))
            else :
                game.son_hover[0] = False
                display_surface.blit(game.image['bouton_jouer'],(664,570))

            # Hover bouton "Règles"
            if curseur[0] > 652 and curseur[0] < 788 and curseur[1] > 651 and curseur[1] < 696 :
                if game.son_hover[1] == False :
                    pygame.mixer.Channel(1).play(pygame.mixer.Sound('assets/son/effet sonore/hover.wav'))
                game.son_hover[1] = True
                display_surface.blit(game.image['bouton_regles_hover'],(652,651))
            else :
                game.son_hover[1] = False
                display_surface.blit(game.image['bouton_regles'],(652,651))

            # Hover bouton "Paramètres"
            if curseur[0] > 606.5 and curseur[0] < 833.5 and curseur[1] > 736 and curseur[1] < 771 :
                if game.son_hover[2] == False :
                    pygame.mixer.Channel(1).play(pygame.mixer.Sound('assets/son/effet sonore/hover.wav'))
                game.son_hover[2] = True
                display_surface.blit(game.image['bouton_parametres_hover'],(606.5,736))
            else :
                game.son_hover[2] = False
                display_surface.blit(game.image['bouton_parametres'],(606.5,736))

            # Hover bouton "Quitter"
            if curseur[0] > 646 and curseur[0] < 794 and curseur[1] > 811 and curseur[1] < 853 :
                if game.son_hover[3] == False :
                    pygame.mixer.Channel(1).play(pygame.mixer.Sound('assets/son/effet sonore/hover.wav'))
                game.son_hover[3] = True
                display_surface.blit(game.image['bouton_quitter_hover'],(646,811))
            else :
                game.son_hover[3] = False
                display_surface.blit(game.image['bouton_quitter'],(646,811))

    if game.in_choix_legends:

        # Hover bouton "Pret J1"
        if game.infos_legends_j1 == False:
            if curseur[0] > 198 and curseur[0] < 413 and curseur[1] > 900 and curseur[1] < 1000 :
                if game.son_hover[4] == False :
                    pygame.mixer.Channel(1).play(pygame.mixer.Sound('assets/son/effet sonore/hover.wav'))
                game.son_hover[4] = True
                display_surface.blit(game.image['pret_on'],(198,900))
            else :
                game.son_hover[4] = False
                if game.pret_J1 == False:
                    display_surface.blit(game.image['pret_off'],(198,900))

        # Hover bouton "Pret J2"
        if game.infos_legends_j2 == False:
            if curseur[0] > 1028 and curseur[0] < 1243 and curseur[1] > 900 and curseur[1] < 1000 :
                if game.son_hover[5] == False :
                    pygame.mixer.Channel(1).play(pygame.mixer.Sound('assets/son/effet sonore/hover.wav'))
                game.son_hover[5] = True
                display_surface.blit(game.image['pret_on'],(1028,900))
            else :
                game.son_hover[5] = False
                if game.pret_J2 == False:
                    display_surface.blit(game.image['pret_off'],(1028,900))

        # Hover bouton "Jouer"
        if curseur[0] > 550 and curseur[0] < 890 and curseur[1] > 452 and curseur[1] < 572 :
            if game.pret_J1 and game.pret_J2:
                if game.son_hover[6] == False :
                    pygame.mixer.Channel(1).play(pygame.mixer.Sound('assets/son/effet sonore/hover.wav'))
                game.son_hover[6] = True
                display_surface.blit(game.image['jouer_on'],(550,452))
            else:
                game.son_hover[6] = False
                display_surface.blit(game.image['jouer_off'], (550, 452))
        else :
            display_surface.blit(game.image['jouer_off'],(550,452))

    if game.in_game:
        if game.menu_pause:
            display_surface.blit(game.image['fond_menu_pause'], (508, 270))
            if curseur[0] > 632 and curseur[0] < 808 and curseur[1] > 481 and curseur[1] < 521:
                display_surface.blit(game.image['bouton_reprendre_hover'], (632, 481))
            else:
                display_surface.blit(game.image['bouton_reprendre'], (632, 481))

            if curseur[0] > 528 and curseur[0] < 904 and curseur[1] > 578 and curseur[1] < 618:
                display_surface.blit(game.image['bouton_reset_hover'], (536, 578))
            else:
                display_surface.blit(game.image['bouton_reset'], (536, 578))

            if curseur[0] > 575 and curseur[0] < 849 and curseur[1] > 675 and curseur[1] < 706:
                display_surface.blit(game.image['bouton_retour_pause_hover'], (591, 675))
            else:
                display_surface.blit(game.image['bouton_retour_pause'], (591, 675))

            if curseur[0] > 610 and curseur[0] < 808 and curseur[1] > 772 and curseur[1] < 803:
                display_surface.blit(game.image['bouton_parametres_pause_hover'], (631, 771))
            else:
                display_surface.blit(game.image['bouton_parametres_pause'], (632, 772))

            if curseur[0] > 630 and curseur[0] < 778 and curseur[1] > 869 and curseur[1] < 907:
                display_surface.blit(game.image['bouton_quitter_pause_hover'], (662, 869))
            else:
                display_surface.blit(game.image['bouton_quitter_pause'], (662, 869))

def luminosite(game, display_surface):
    if game.luminosite == 80:
        display_surface.blit(game.image['80%'], (0,0))
    elif game.luminosite == 60:
        display_surface.blit(game.image['60%'], (0,0))
    elif game.luminosite == 40:
        display_surface.blit(game.image['40%'], (0,0))
    elif game.luminosite == 20:
        display_surface.blit(game.image['20%'], (0,0))
    if game.luminosite == 0:
        display_surface.blit(game.image['0%'], (0,0))

### Fonction utile
def position_rect(rect, x, y):
    rect.x = x
    rect.y = y

### Fonction Menu
def parametres(game, display_surface):
    display_surface.blit(game.image['fond_parametre'], (277, 440))
    display_surface.blit(game.image['bouton_fermer'], (1104, 456))
    display_surface.blit(game.image['plus'], (784, 647))
    display_surface.blit(game.image['plus'], (784, 760))
    display_surface.blit(game.image['plus'], (784, 871))
    display_surface.blit(game.image['moins'], (625, 648))
    display_surface.blit(game.image['moins'], (625, 761))
    display_surface.blit(game.image['moins'], (625, 872))

    font1 = pygame.font.SysFont("palatinolinotype", 40, bold=True, italic=False)
    # Affichage volume musique
    musique = font1.render(str(int(game.musique * 100)), True, (0, 0, 0))
    if game.musique == 0:
        display_surface.blit(musique, (707, 647))
    elif game.musique > 0 and game.musique < 1 :
        display_surface.blit(musique, (703, 647))
    else :
        display_surface.blit(musique, (688, 647))

    # Affichage volume effet sonore
    effet_sonore = font1.render(str(int(game.effet_sonore * 100)), True, (0, 0, 0))
    if game.effet_sonore == 0:
        display_surface.blit(effet_sonore, (707, 760))
    elif game.effet_sonore > 0 and game.effet_sonore < 1 :
        display_surface.blit(effet_sonore, (703, 760))
    else:
        display_surface.blit(effet_sonore, (688, 760))


    # Affichage pourcentage luminosite
    luminosite = font1.render(str(game.luminosite), True, (0, 0, 0))
    if game.luminosite == 0:
        display_surface.blit(luminosite, (707, 871))
    elif game.luminosite > 0 and game.luminosite < 100:
        display_surface.blit(luminosite, (703, 871))
    else:
        display_surface.blit(luminosite, (688, 871))

### Fonction ChoixLegends
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
            display_surface.blit(game.image['gunnar_infos'], (position_cards_J1[0], position_cards_J1[1]))

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
            display_surface.blit(game.image['lucie_infos'], (position_cards_J1[0], position_cards_J1[1]))

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

### Fonction INGAME
def musique_ingame(game):
    if game.stage_select == 1:
        pygame.mixer.Channel(0).play(pygame.mixer.Sound('assets/son/isis_musique.wav'), -1)
    elif game.stage_select == 2:
        pygame.mixer.Channel(0).play(pygame.mixer.Sound('assets/son/gunnar_musique.wav'), -1)
    elif game.stage_select == 3:
        pygame.mixer.Channel(0).play(pygame.mixer.Sound('assets/son/bigband_musique.wav'), -1)
    elif game.stage_select == 4:
        pygame.mixer.Channel(0).play(pygame.mixer.Sound('assets/son/kitt_musique.wav'), -1)
    elif game.stage_select == 5:
        pygame.mixer.Channel(0).play(pygame.mixer.Sound('assets/son/harry_musique.wav'), -1)
    else:
        pygame.mixer.Channel(0).play(pygame.mixer.Sound('assets/son/lucie_musique.wav'), -1)
def grammaire(game):
    #Joueur 1
    if len(game.player.p1_phrase[0]) > 1:
        if game.player.p1_phrase[0][0] in game.sujetsref:
            game.player.score_J1 += 1
        else:
            game.player.score_J1 -= 1
    else :
        game.player.score_J1 -= 1
    if len(game.player.p1_phrase[0]) > 2:
        if game.player.p1_phrase[0][1] in game.verbesref:
            game.player.score_J1 += 1
        else:
            game.player.score_J1 -= 1
    else :
        game.player.score_J1 -= 1
    if len(game.player.p1_phrase[0]) > 3:
        if game.player.p1_phrase[0][2] in game.complementref:
            game.player.score_J1 += 1
        else:
            game.player.score_J1 -= 1
    else :
        game.player.score_J1 -= 1
    if len(game.player.p1_phrase[0]) > 4:
        if game.player.p1_phrase[0][3] in game.liaisonref:
            game.player.score_J1 += 1
        else:
            game.player.score_J1 -= 1
    if len(game.player.p1_phrase[0]) > 5:
        if game.player.p1_phrase[0][4] in game.complementref:
            game.player.score_J1 += 1
        else:
            game.player.score_J1 -= 1

    #Joueur 2
    if len(game.player.p2_phrase[0]) > 1:
        if game.player.p2_phrase[0][0] in game.sujetsref:
            game.player.score_J2 += 1
        else:
            game.player.score_J2 -= 1
    else :
        game.player.score_J2 -= 1
    if len(game.player.p2_phrase[0]) > 2:
        if game.player.p2_phrase[0][1] in game.verbesref:
            game.player.score_J2 += 1
        else:
            game.player.score_J2 -= 1
    else :
        game.player.score_J2 -= 1
    if len(game.player.p2_phrase[0]) > 3:
        if game.player.p2_phrase[0][2] in game.complementref:
            game.player.score_J2 += 1
        else:
            game.player.score_J2 -= 1
    else :
        game.player.score_J2 -= 1
    if len(game.player.p2_phrase[0]) > 4:
        if game.player.p2_phrase[0][3] in game.liaisonref:
            game.player.score_J2 += 1
        else:
            game.player.score_J2 -= 1
    if len(game.player.p2_phrase[0]) > 5:
        if game.player.p2_phrase[0][4] in game.complementref:
            game.player.score_J2 += 1
        else:
            game.player.score_J2 -= 1

def round(game):
    if game.round[0] != game.round[1]:
        game.tour = randint(0, 1)
        game.prop = []
        game.sujets = game.sujetsref.copy()
        game.verbes = game.verbesref.copy()
        game.complement = game.complementref.copy()
        game.liaison = game.liaisonref.copy()
        game.player.score_J1 = 0
        game.player.score_J2 = 0
        game.player.p1_phrase = [[], False]
        game.player.p2_phrase = [[], False]
        game.rect_utilise = [True, True, True, True, True, True, True, True, True, True, True, True]
        game.round[1] = game.round[0]

def degats(game):
    if game.player.score_J1 > game.player.score_J2 and game.player.max_Hp_J2 == 500 :
        game.player.Hp_J2 = game.player.Hp_J2 - 150
    elif game.player.score_J1 > game.player.score_J2 and game.player.max_Hp_J2 == 350 :
        game.player.Hp_J2 = game.player.Hp_J2 - 150
    elif game.player.score_J1 > game.player.score_J2 and game.player.max_Hp_J2 == 200 :
        game.player.Hp_J2 = game.player.Hp_J2 - 200

    elif game.player.score_J2 > game.player.score_J1 and game.player.max_Hp_J1 == 500 :
        game.player.Hp_J1 = game.player.Hp_J1 - 150
    elif game.player.score_J2 > game.player.score_J1 and game.player.max_Hp_J1 == 350 :
        game.player.Hp_J1 = game.player.Hp_J1 - 150
    elif game.player.score_J2 > game.player.score_J1 and game.player.max_Hp_J1 == 200 :
        game.player.Hp_J1 = game.player.Hp_J1 - 200

def Combat(game, x, display_surface):
    if game.player.p1_phrase[1] == False or game.player.p2_phrase[1] == False or game.player.p1_phrase[1] == False and game.player.p2_phrase[1] == False:
        if game.tour == 0:
            if x < 12 and len(game.player.p1_phrase[0]) < 5:
                game.player.p1_phrase[0].append(game.prop[x])
            elif x == 12:
                game.player.p1_phrase[0].append(".")
                game.player.p1_phrase[1] = True
            else :
                game.player.p1_phrase[0].append("!")
                game.player.p1_phrase[1] = True
            if game.player.p2_phrase[1] == False :
                game.tour = 1
        else :
            if x < 12 and len(game.player.p2_phrase[0]) < 5:
                game.player.p2_phrase[0].append(game.prop[x])
            elif x == 12:
                game.player.p2_phrase[0].append(".")
                game.player.p2_phrase[1] = True
            else :
                game.player.p2_phrase[0].append("!")
                game.player.p2_phrase[1] = True
            if game.player.p1_phrase[1] == False:
                game.tour = 0
    elif game.player.Hp_J2 > 0 and game.player.Hp_J1 > 0:
    # Calcul score de la phrase

        # longueur phrase
        if len(game.player.p1_phrase[0]) > len(game.player.p2_phrase[0]):
            game.player.score_J1 = len(game.player.p1_phrase[0]) - len(game.player.p2_phrase[0])
            game.player.score_J2 = 0
            print("joueur 1 a la phrase la plus longue")
        elif len(game.player.p2_phrase[0]) > len(game.player.p1_phrase[0]):
            game.player.score_J1 = 0
            game.player.score_J2 = len(game.player.p2_phrase[0]) - len(game.player.p1_phrase[0])
            print("joueur 2 a la phrase la plus longue")
        print(game.player.score_J1, game.player.score_J2)

        # faiblesse phrase
        for i in game.player.p1_phrase[0]:
            for s in game.stats[game.player.legends_J2]:
                for j in game.faiblesse[s]:
                    if i == j:
                        game.player.score_J1 += 5
        for i in game.player.p2_phrase[0]:
            for s in game.stats[game.player.legends_J1]:
                for j in game.faiblesse[s]:
                    if i == j:
                        game.player.score_J2 += 5
        print(game.player.score_J1, game.player.score_J2)

        # grammaire phrase
        grammaire(game)
        print(game.player.score_J1, game.player.score_J2)
        degats(game)
        if game.player.Hp_J1 != 0 and game.player.Hp_J2 != 0:
            game.round[0] += 1
            round(game)

def nuage(game, display_surface):
    font1 = pygame.font.SysFont("palatinolinotype", 20, bold=True, italic=False)
    concatenationJ1 = ""
    concatenationJ2 = ""
    for i in game.player.p1_phrase[0]:
        concatenationJ1 = concatenationJ1 + " " + i
    for i in game.player.p2_phrase[0]:
        concatenationJ2 = concatenationJ2 + " " + i
    phraseJ1 = font1.render(concatenationJ1, True, (0, 0, 0))
    phraseJ2 = font1.render(concatenationJ2, True, (0, 0, 0))
    display_surface.blit(phraseJ1, (76, 173))
    display_surface.blit(phraseJ2, (818, 173))

def barre_de_vie(game,display_surface):
    bar_border = (0, 0, 0)
    bar_losehp = (255, 211, 121)
    bar_position_J1 = [20, 20, game.player.max_Hp_J1, 50]
    #j1
    if game.player.max_Hp_J1 != game.player.Hp_J1:
        if game.player.max_Hp_J1 == 380:
            game.player.bar_vie_J1 = (232, 170, 14)
        elif game.player.max_Hp_J1 == 240:
            game.player.bar_vie_J1 = (205, 0, 0)
        pygame.draw.rect(display_surface, bar_losehp, [20, 20, 500, 50], 0, 25)
        pygame.draw.rect(display_surface, game.player.bar_vie_J1, bar_position_J1, 0, 25)
        pygame.draw.rect(display_surface, bar_border, [20, 20, 500, 50], 3, 25)
        game.player.max_Hp_J1 = game.player.max_Hp_J1 - 2

    else:
        pygame.draw.rect(display_surface, bar_losehp, [20, 20, 500, 50], 0, 25)
        pygame.draw.rect(display_surface, game.player.bar_vie_J1, bar_position_J1, 0, 25)
        pygame.draw.rect(display_surface, bar_border, [20, 20, 500, 50], 3, 25)

    #j2
    if game.player.max_Hp_J2 != game.player.Hp_J2:
        if game.player.max_Hp_J2 == 380:
            game.player.bar_vie_J2 = (232, 170, 14)
        elif game.player.max_Hp_J2 == 240:
            game.player.bar_vie_J2 = (205, 0, 0)
        pygame.draw.rect(display_surface, bar_losehp, [920, 20, 500, 50], 0, 25)
        pygame.draw.rect(display_surface, game.player.bar_vie_J2, game.player.bar_position_J2, 0, 25)
        pygame.draw.rect(display_surface, bar_border, [920, 20, 500, 50], 3, 25)
        game.player.max_Hp_J2 = game.player.max_Hp_J2 - 2
        game.player.bar_position_J2[0] = game.player.bar_position_J2[0] + 2
        game.player.bar_position_J2[2] = game.player.max_Hp_J2
    else:
        pygame.draw.rect(display_surface, bar_losehp, [920, 20, 500, 50], 0, 25)
        pygame.draw.rect(display_surface, game.player.bar_vie_J2, game.player.bar_position_J2, 0, 25)
        pygame.draw.rect(display_surface, bar_border, [920, 20, 500, 50], 3, 25)

    # Alerte low pv
    if game.player.max_Hp_J1 == 220 or game.player.max_Hp_J2 == 220 or game.player.max_Hp_J1 + game.player.max_Hp_J2 == 440:
        pygame.mixer.Channel(1).play(pygame.mixer.Sound('assets/son/effet sonore/alerte.wav'))

def choix_background_local(game,display_surface):
    if game.stage_select == 1:
        display_surface.blit(game.image['isis_back'], (0, 0))
    if game.stage_select == 2:
        display_surface.blit(game.image['gunnar_back'], (0, 0))
    if game.stage_select == 3:
        display_surface.blit(game.image['bigband_back'], (0, 0))
    if game.stage_select == 4:
        display_surface.blit(game.image['kitt_back'], (0, 0))
    if game.stage_select == 5:
        display_surface.blit(game.image['harry_back'], (0, 0))
    if game.stage_select == 6:
        display_surface.blit(game.image['lucie_back'], (0, 0))

def remplir_tableau(game, display_surface):
    RED = (125, 0, 0)
    BLUE = (0, 48, 170)
    GREEN = (0, 116, 19)
    YELLOW = (255, 135, 0)

    font1 = pygame.font.SysFont("palatinolinotype", 40, bold=True, italic=False)


    if len(game.prop) != 12:
        v = randint(0,len(game.sujets) - 1)
        w = randint(0,len(game.verbes) - 1)
        game.prop.append(game.sujets[v])
        game.sujets.pop(v)
        game.prop.append(game.verbes[w])
        game.verbes.pop(w)
        if len(game.prop) != 12 :
            x = randint(0, len(game.complement) - 1)
            game.prop.append(game.complement[x])
            game.complement.pop(x)
            y = randint(0, len(game.liaison) - 1)
            game.prop.append(game.liaison[y])
            game.liaison.pop(y)
            z = randint(0, len(game.complement) - 1)
            game.prop.append(game.complement[z])
            game.complement.pop(z)

    img1 = font1.render(game.prop[0], True, RED)
    img2 = font1.render(game.prop[1], True, BLUE)
    img3 = font1.render(game.prop[2], True, GREEN)
    img4 = font1.render(game.prop[3], True, YELLOW)
    img5 = font1.render(game.prop[4], True, GREEN)

    if game.rect_utilise[0]:
        display_surface.blit(img1, (555, 331))
    if game.rect_utilise[1]:
        display_surface.blit(img2, (555, 381))
    if game.rect_utilise[2]:
        display_surface.blit(img3, (555, 431))
    if game.rect_utilise[3]:
        display_surface.blit(img4, (555, 481))
    if game.rect_utilise[4]:
        display_surface.blit(img5, (555, 531))

    if len(game.prop) > 5 :
        img6 = font1.render(game.prop[5], True, RED)
        img7 = font1.render(game.prop[6], True, BLUE)
        img8 = font1.render(game.prop[7], True, GREEN)
        img9 = font1.render(game.prop[8], True, YELLOW)
        img10 = font1.render(game.prop[9], True, GREEN)

        if game.rect_utilise[5]:
            display_surface.blit(img6, (555, 581))
        if game.rect_utilise[6]:
            display_surface.blit(img7, (555, 631))
        if game.rect_utilise[7]:
            display_surface.blit(img8, (555, 681))
        if game.rect_utilise[8]:
            display_surface.blit(img9, (555, 731))
        if game.rect_utilise[9]:
            display_surface.blit(img10, (555, 781))

    if len(game.prop) > 10 :
        img11 = font1.render(game.prop[10], True, RED)
        img12 = font1.render(game.prop[11], True, BLUE)
        if game.rect_utilise[10]:
            display_surface.blit(img11, (555, 831))
        if game.rect_utilise[11]:
            display_surface.blit(img12, (555, 881))
    img13 = font1.render(".", True, (0,0,0))
    img14 = font1.render("!", True, (0,0,0))
    display_surface.blit(img13, (632.5,931))
    display_surface.blit(img14, (801.5,931))

def tableau_prop(game, display_surface):
    tableau_prop = (212,212,212)
    tableau_position = [545, 324, 350, 650]
    pygame.draw.rect(display_surface, tableau_prop, tableau_position)
    pygame.draw.rect(display_surface, (0,0,0), tableau_position, 3)

    line_couleur = (0,0,0)
    line_position_start = [545, 374]
    line_position_end = [895, 374]
    line_position_start_vert = [720, 973]
    line_position_end_vert = [720, 923]
    pygame.draw.line(display_surface,line_couleur,line_position_start_vert,line_position_end_vert,3)

    for i in range(1,13):
        pygame.draw.line(display_surface,line_couleur,line_position_start,line_position_end,3)
        line_position_start[1] += 50
        line_position_end[1] += 50
    remplir_tableau(game, display_surface)

def affichage_joueur(game,display_surface):
    if game.player.max_Hp_J2 != game.player.Hp_J2 or game.player.max_Hp_J2 == 0 :
        if game.player.legends_J1 == 'bigband':
            display_surface.blit(game.image['bigband_J1_4'], (0, 224))
        elif game.player.legends_J1 == 'gunnar':
            display_surface.blit(game.image['gunnar_J1_4'], (-10, 224))
        elif game.player.legends_J1 == 'harry':
            display_surface.blit(game.image['harry_J1_4'], (-20, 224))
        elif game.player.legends_J1 == 'isis':
            display_surface.blit(game.image['isis_J1_4'], (0, 224))
        elif game.player.legends_J1 == 'kitt':
            display_surface.blit(game.image['kitt_J1_4'], (0, 224))
        elif game.player.legends_J1 == 'lucie':
            display_surface.blit(game.image['lucie_J1_4'], (0, 224))
    elif game.player.max_Hp_J1 == 0:
        if game.player.legends_J1 == 'bigband':
            display_surface.blit(game.image['bigband_J1_3'], (0, 224))
        elif game.player.legends_J1 == 'gunnar':
            display_surface.blit(game.image['gunnar_J1_3'], (-10, 224))
        elif game.player.legends_J1 == 'harry':
            display_surface.blit(game.image['harry_J1_3'], (-20, 224))
        elif game.player.legends_J1 == 'isis':
            display_surface.blit(game.image['isis_J1_3'], (0, 224))
        elif game.player.legends_J1 == 'kitt':
            display_surface.blit(game.image['kitt_J1_3'], (0, 224))
        elif game.player.legends_J1 == 'lucie':
            display_surface.blit(game.image['lucie_J1_3'], (0, 224))
    elif game.player.max_Hp_J1 != game.player.Hp_J1:
        if game.player.legends_J1 == 'bigband':
            display_surface.blit(game.image['bigband_J1_2'], (0, 224))
        elif game.player.legends_J1 == 'gunnar':
            display_surface.blit(game.image['gunnar_J1_2'], (-10, 224))
        elif game.player.legends_J1 == 'harry':
            display_surface.blit(game.image['harry_J1_2'], (-20, 224))
        elif game.player.legends_J1 == 'isis':
            display_surface.blit(game.image['isis_J1_2'], (0, 224))
        elif game.player.legends_J1 == 'kitt':
            display_surface.blit(game.image['kitt_J1_2'], (0, 224))
        elif game.player.legends_J1 == 'lucie':
            display_surface.blit(game.image['lucie_J1_2'], (0, 224))
    elif game.tour == 0:
        if game.player.legends_J1 == 'bigband':
            display_surface.blit(game.image['bigband_J1_5'], (0, 224))
        elif game.player.legends_J1 == 'gunnar':
            display_surface.blit(game.image['gunnar_J1_5'], (-10, 224))
        elif game.player.legends_J1 == 'harry':
            display_surface.blit(game.image['harry_J1_5'], (-20, 224))
        elif game.player.legends_J1 == 'isis':
            display_surface.blit(game.image['isis_J1_5'], (0, 224))
        elif game.player.legends_J1 == 'kitt':
            display_surface.blit(game.image['kitt_J1_5'], (0, 224))
        elif game.player.legends_J1 == 'lucie':
            display_surface.blit(game.image['lucie_J1_5'], (0, 224))
    elif game.tour == 1 :
        if game.player.legends_J1 == 'bigband':
            display_surface.blit(game.image['bigband_J1_1'], (0, 224))
        elif game.player.legends_J1 == 'gunnar':
            display_surface.blit(game.image['gunnar_J1_1'], (-10, 224))
        elif game.player.legends_J1 == 'harry':
            display_surface.blit(game.image['harry_J1_1'], (-20, 224))
        elif game.player.legends_J1 == 'isis':
            display_surface.blit(game.image['isis_J1_1'], (0, 224))
        elif game.player.legends_J1 == 'kitt':
            display_surface.blit(game.image['kitt_J1_1'], (0, 224))
        elif game.player.legends_J1 == 'lucie':
            display_surface.blit(game.image['lucie_J1_1'], (0, 224))


    if game.player.max_Hp_J1 != game.player.Hp_J1 or game.player.max_Hp_J1 == 0:
        if game.player.legends_J2 == 'bigband':
            display_surface.blit(game.image['bigband_J2_4'], (924.02, 224))
        elif game.player.legends_J2 == 'gunnar':
            display_surface.blit(game.image['gunnar_J2_4'], (738.76, 224))
        elif game.player.legends_J2 == 'harry':
            display_surface.blit(game.image['harry_J2_4'], (797.14, 224))
        elif game.player.legends_J2 == 'isis':
            display_surface.blit(game.image['isis_J2_4'], (824.62, 224))
        elif game.player.legends_J2 == 'kitt':
            display_surface.blit(game.image['kitt_J2_4'], (728.76, 224))
        else:
            display_surface.blit(game.image['lucie_J2_4'], (836.91, 224))
    elif game.player.max_Hp_J2 == 0 :
        if game.player.legends_J2 == 'bigband':
            display_surface.blit(game.image['bigband_J2_3'], (924.02, 224))
        elif game.player.legends_J2 == 'gunnar':
            display_surface.blit(game.image['gunnar_J2_3'], (738.76, 224))
        elif game.player.legends_J2 == 'harry':
            display_surface.blit(game.image['harry_J2_3'], (797.14, 224))
        elif game.player.legends_J2 == 'isis':
            display_surface.blit(game.image['isis_J2_3'], (824.62, 224))
        elif game.player.legends_J2 == 'kitt':
            display_surface.blit(game.image['kitt_J2_3'], (728.76, 224))
        else:
            display_surface.blit(game.image['lucie_J2_3'], (836.91, 224))
    elif game.player.max_Hp_J2 != game.player.Hp_J2:
        if game.player.legends_J2 == 'bigband':
            display_surface.blit(game.image['bigband_J2_2'], (924.02, 224))
        elif game.player.legends_J2 == 'gunnar':
            display_surface.blit(game.image['gunnar_J2_2'], (738.76, 224))
        elif game.player.legends_J2 == 'harry':
            display_surface.blit(game.image['harry_J2_2'], (797.14, 224))
        elif game.player.legends_J2 == 'isis':
            display_surface.blit(game.image['isis_J2_2'], (824.62, 224))
        elif game.player.legends_J2 == 'kitt':
            display_surface.blit(game.image['kitt_J2_2'], (728.76, 224))
        else:
            display_surface.blit(game.image['lucie_J2_2'], (836.91, 224))
    elif game.tour == 1:
        if game.player.legends_J2 == 'bigband':
            display_surface.blit(game.image['bigband_J2_5'], (924.02, 224))
        elif game.player.legends_J2 == 'gunnar':
            display_surface.blit(game.image['gunnar_J2_5'], (738.76, 224))
        elif game.player.legends_J2 == 'harry':
            display_surface.blit(game.image['harry_J2_5'], (797.14, 224))
        elif game.player.legends_J2 == 'isis':
            display_surface.blit(game.image['isis_J2_5'], (824.62, 224))
        elif game.player.legends_J2 == 'kitt':
            display_surface.blit(game.image['kitt_J2_5'], (728.76, 224))
        elif game.player.legends_J2 == 'lucie':
            display_surface.blit(game.image['lucie_J2_5'], (836.91, 224))
    elif game.tour == 0:
        if game.player.legends_J2 == 'bigband':
            display_surface.blit(game.image['bigband_J2_1'], (924.02, 224))
        elif game.player.legends_J2 == 'gunnar':
            display_surface.blit(game.image['gunnar_J2_1'], (738.76, 224))
        elif game.player.legends_J2 == 'harry':
            display_surface.blit(game.image['harry_J2_1'], (797.14, 224))
        elif game.player.legends_J2 == 'isis':
            display_surface.blit(game.image['isis_J2_1'], (824.62, 224))
        elif game.player.legends_J2 == 'kitt':
            display_surface.blit(game.image['kitt_J2_1'], (728.76, 224))
        else:
            display_surface.blit(game.image['lucie_J2_1'], (836.91, 224))

def tour(game, display_surface):
    font1 = pygame.font.SysFont("palatinolinotype", 45, bold=True, italic=False)
    pygame.draw.rect(display_surface,(212,212,212), [555, 16, 330, 60])
    pygame.draw.rect(display_surface, (0, 0, 0), [555, 16, 330, 60], 3)
    if game.player.max_Hp_J1 > 0 and game.player.max_Hp_J2 > 0:
        if game.tour == 0:
            phrase = font1.render("Joueur 1 joue :", True, (0, 48, 170))
            display_surface.blit(phrase, (577, 25))
        else :
            phrase = font1.render("Joueur 2 joue :", True, (180, 0, 0))
            display_surface.blit(phrase, (577, 25))
    elif game.player.max_Hp_J1 == 0 :
        phrase = font1.render("Joueur 2 gagne", True, (180, 0, 0))
        display_surface.blit(phrase, (568, 25))
    else :
        phrase = font1.render("Joueur 1 gagne", True, (0, 48, 170))
        display_surface.blit(phrase, (568, 25))

def reset_match(game):
    if game.in_game:
        game.stage_select = randint(1,6)
    else:
        game.stage_select = None
        game.player.legends_J1 = None
        game.player.legends_J2 = None
        game.player.faiblesse_J1 = None
        game.player.faiblesse_J2 = None

    game.pret_J1 = False
    game.pret_J2 = False
    game.tour = randint(0, 1)
    game.round = [1, 1]
    game.alpha = 300
    game.rect_utilise = [True, True, True, True, True, True, True, True, True, True, True, True]
    game.prop = []
    game.player.Hp_J1 = 500
    game.player.Hp_J2 = 500
    game.player.max_Hp_J1 = 500
    game.player.max_Hp_J2 = 500
    game.player.bar_position_J2 = [920, 20, game.player.max_Hp_J2, 50]
    game.player.bar_vie_J1 = (0, 204, 82)
    game.player.bar_vie_J2 = (0, 204, 82)
    game.player.p1_phrase = [[], False]
    game.player.p2_phrase = [[], False]
    game.player.score_J1 = 0
    game.player.score_J2 = 0
    game.sujets = game.sujetsref.copy()
    game.verbes = game.verbesref.copy()
    game.complement = game.complementref.copy()
    game.liaison = game.liaisonref.copy()
    return game




