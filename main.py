import pygame
from fonctions import *
pygame.init()

frame_per_sec = pygame.time.Clock()

display_surface = pygame.display.set_mode((1440,1024))

pygame.display.set_caption("Words Legends")

backgroundmenu = pygame.image.load('assets/fond_menu.jpg')

'''#curseurs
imagecurseur = pygame.image.load('assets/curseur.png')
imagecurseurhover = pygame.image.load('assets/curseur_hover.png')'''

#Bouton menu
boutonjouer = pygame.image.load('assets/bouton_jouer.png')
boutonregles = pygame.image.load('assets/bouton_regles.png')
boutonparametres = pygame.image.load('assets/bouton_parametres.png')
boutonquitter = pygame.image.load('assets/bouton_quitter.png')

#Bouton menu hover
boutonjouerhover = pygame.image.load('assets/bouton_jouer_hover.png')
boutonregleshover = pygame.image.load('assets/bouton_regles_hover.png')
boutonparametreshover = pygame.image.load('assets/bouton_parametres_hover.png')
boutonquitterhover = pygame.image.load('assets/bouton_quitter_hover.png')

# Essayer de changer notre curseur

x = True

while x:

    curseur = pygame.mouse.get_pos()

    #curseur(curseur, imagecurseur, imagecurseurhover)

    pygame.display.update()

    display_surface.blit(backgroundmenu,(0,0))

    # Fonction hover boutons menu
    hoverboutons(curseur, boutonjouer, boutonregles, boutonparametres, boutonquitter, boutonjouerhover, boutonregleshover, boutonparametreshover, boutonquitterhover, display_surface)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

        # if pygame.mouse.get_focused():
            # x, y = pygame.mouse.get_pos()

    frame_per_sec.tick(60)
    