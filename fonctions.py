import pygame
from class_game import *
pygame.init()

### Fonction graphique
def hover_boutons(game,curseur,display_surface):
    if game.in_menu:
        if game.menu_regles == False:

            # Hover bouton "Jouer"
            if curseur[0] > 664 and curseur[0] < 776 and curseur[1] > 570 and curseur[1] < 611 :
                display_surface.blit(game.image['bouton_jouer_hover'],(664,570))
            else :
                if game.in_menu :
                    display_surface.blit(game.image['bouton_jouer'],(664,570))

            # Hover bouton "Règles"
            if curseur[0] > 652 and curseur[0] < 788 and curseur[1] > 651 and curseur[1] < 696 :
                display_surface.blit(game.image['bouton_regles_hover'],(652,651))
            else :
                display_surface.blit(game.image['bouton_regles'],(652,651))

            # Hover bouton "Paramètres"
            if curseur[0] > 606.5 and curseur[0] < 833.5 and curseur[1] > 736 and curseur[1] < 771 :
                display_surface.blit(game.image['bouton_parametres_hover'],(606.5,736))
            else :
                display_surface.blit(game.image['bouton_parametres'],(606.5,736))

            # Hover bouton "Quitter"
            if curseur[0] > 646 and curseur[0] < 794 and curseur[1] > 811 and curseur[1] < 853 :
                display_surface.blit(game.image['bouton_quitter_hover'],(646,811))
            else :
                display_surface.blit(game.image['bouton_quitter'],(646,811))

    if game.in_choix_legends:

        # Hover bouton "Pret J1"
        if game.infos_legends_j1 == False:
            if curseur[0] > 198 and curseur[0] < 413 and curseur[1] > 900 and curseur[1] < 1000 :
                display_surface.blit(game.image['pret_on'],(198,900))
            else :
                if game.pret_J1 == False:
                    display_surface.blit(game.image['pret_off'],(198,900))

        # Hover bouton "Pret J2"
        if game.infos_legends_j2 == False:
            if curseur[0] > 1028 and curseur[0] < 1243 and curseur[1] > 900 and curseur[1] < 1000 :
                display_surface.blit(game.image['pret_on'],(1028,900))
            else :
                if game.pret_J2 == False:
                    display_surface.blit(game.image['pret_off'],(1028,900))

        # Hover bouton "Jouer"
        if curseur[0] > 550 and curseur[0] < 890 and curseur[1] > 452 and curseur[1] < 572 :
            if game.pret_J1 and game.pret_J2:
                display_surface.blit(game.image['jouer_on'],(550,452))
            else:
                display_surface.blit(game.image['jouer_off'], (550, 452))
        else :
            display_surface.blit(game.image['jouer_off'],(550,452))

### Fonction utile
def position_rect(rect, x, y):
    rect.x = x
    rect.y = y

def grammaire(game):
    #Joueur 1
    if game.player.p1_phrase[0][0] in game.sujetsref:
        game.player.score_J1 += 1
    else:
        game.player.score_J1 -= 1
    if len(game.player.p1_phrase[0]) > 1:
        if game.player.p1_phrase[0][1] in game.verbesref:
            game.player.score_J1 += 1
        else:
            game.player.score_J1 -= 1
    if len(game.player.p1_phrase[0]) > 2:
        if game.player.p1_phrase[0][2] in game.complementref:
            game.player.score_J1 += 1
        else:
            game.player.score_J1 -= 1
    if len(game.player.p1_phrase[0]) > 3:
        if game.player.p1_phrase[0][3] in game.liaisonref:
            game.player.score_J1 += 1
        else:
            game.player.score_J1 -= 11
    if len(game.player.p1_phrase[0]) > 4:
        if game.player.p1_phrase[0][4] in game.complementref:
            game.player.score_J1 += 1
        else:
            game.player.score_J1 -= 11

    #Joueur 2
    if game.player.p2_phrase[0][0] in game.sujetsref:
        game.player.score_J2 += 1
    else:
        game.player.score_J2 -= 1
    if len(game.player.p1_phrase[0]) > 1:
        if game.player.p2_phrase[0][1] in game.verbesref:
            game.player.score_J2 += 1
        else:
            game.player.score_J2 -= 1
    if len(game.player.p1_phrase[0]) > 2:
        if game.player.p2_phrase[0][2] in game.complementref:
            game.player.score_J2 += 1
        else:
            game.player.score_J2 -= 1
    if len(game.player.p2_phrase[0]) > 3:
        if game.player.p2_phrase[0][3] in game.liaisonref:
            game.player.score_J2 += 1
        else:
            game.player.score_J2 -= 11
    if len(game.player.p2_phrase[0]) > 4:
        if game.player.p2_phrase[0][4] in game.complementref:
            game.player.score_J2 += 1
        else:
            game.player.score_J2 -= 11


def round(game):
    if game.round_ref != game.round:
        game.tour = randint(0, 1)
        game.prop = []
        game.sujets = game.sujetsref
        game.verbes = game.verbesref
        game.complement = game.complementref
        game.liaison = game.liaisonref
        game.player.score_J1 = 0
        game.player.score_J2 = 0
        game.player.p1_phrase = [[], False]
        game.player.p2_phrase = [[], False]
        game.rect_utilisé = [True, True, True, True, True, True, True, True, True, True, True, True]
        game.round_ref = game.round

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




'''# Test dictionnaire de sons
sounds = {
    'click' : pygame.mixer.Sound("assets/son/click.ogg"),
}'''