import pygame
pygame.init()
# while P1.hp != 0 or P2.hp != 0:
    # print(List.insultes)


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

def hoverboutons(curseur, boutonjouer, boutonregles, boutonparametres, boutonquitter, boutonjouerhover, boutonregleshover, boutonparametreshover, boutonquitterhover, display_surface):

    # Hover bouton "Jouer"
    if curseur[0] > 664 and curseur[0] < 776 and curseur[1] > 570 and curseur[1] < 611 :
        display_surface.blit(boutonjouerhover,(664,570))
    else :
        display_surface.blit(boutonjouer,(664,570))

    # Hover bouton "Règles"
    if curseur[0] > 652 and curseur[0] < 788 and curseur[1] > 651 and curseur[1] < 696 :
        display_surface.blit(boutonregleshover,(652,651))
    else :
        display_surface.blit(boutonregles,(652,651))

    # Hover bouton "Paramètres"
    if curseur[0] > 606.5 and curseur[0] < 833.5 and curseur[1] > 736 and curseur[1] < 771 :
        display_surface.blit(boutonparametreshover,(606.5,736))
    else :
        display_surface.blit(boutonparametres,(606.5,736))

    # Hover bouton "Quitter"
    if curseur[0] > 646 and curseur[0] < 794 and curseur[1] > 811 and curseur[1] < 853 :
        display_surface.blit(boutonquitterhover,(646,811))
    else :
        display_surface.blit(boutonquitter,(646,811))

''' Test dictionnaire de sons
sounds = {
    'click' : pygame.mixer.Sound("assets/son/click.ogg"),
}'''