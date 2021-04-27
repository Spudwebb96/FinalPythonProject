import pygame
from class_game import *
pygame.init()

game = game()
### Fonction gameplay

def grammaire ():
    for i in sujetlist:
        if i == userchoice :
            continue
        else :
            insultepower -= -1
            print("Bad grammar !")
            continue
    for i in verbelist:
        if i == userchoice:
            continue
        else :
            insultepower -= -1
            print("Bad grammar !")
            continue
    for i in complement :
        if i == userchoice:
            continue
        else :
            insultepower -= -1
            print("Bad grammar !")
            continue

def weaknesscalc(self):
    for i in weakness.P2:
        if i == sujet :
            insultepower += 1
        if i == verbe :
            insultepower += 1
        if i == complement :
            insultepower += 1
    
    for i in weakness.P1:
        if i == sujet :
            insultepower += 1
        if i == verbe :
            insultepower += 1
        if i == complement :
            insultepower += 1


### Fonction graphique
def hover_boutons(curseur,display_surface):
    if game.menu_regles == False :

        # Hover bouton "Jouer"
        if curseur[0] > 664 and curseur[0] < 776 and curseur[1] > 570 and curseur[1] < 611 :
            display_surface.blit(game.image['bouton_jouer_hover'],(664,570))
        else :
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

### Fonction utile
def position_rect(rect, x, y):
    rect.x = x
    rect.y = y



'''# Test dictionnaire de sons
sounds = {
    'click' : pygame.mixer.Sound("assets/son/click.ogg"),
}'''