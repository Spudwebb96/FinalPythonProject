import pygame
pygame.init()

frame_per_sec = pygame.time.Clock()

display_surface = pygame.display.set_mode((1440,1024))

pygame.display.set_caption("Words Legends")

backgroundmenu = pygame.image.load('assets/fond_menu.jpg')
boutonjouer = pygame.image.load('assets/bouton_jouer.png')
boutonregles = pygame.image.load('assets/bouton_regles.png')
boutonparametres = pygame.image.load('assets/bouton_parametres.png')
boutonquitter = pygame.image.load('assets/bouton_quitter.png')
# Essayer de changer notre curseur

x = True

while x:

    pygame.display.update()

    display_surface.blit(backgroundmenu,(0,0))
    display_surface.blit(boutonjouer,(664,570)) # espace = 40
    display_surface.blit(boutonregles,(652,651))
    display_surface.blit(boutonparametres,(606.5,736))
    display_surface.blit(boutonquitter,(646,811))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

        # if pygame.mouse.get_focused():
            # x, y = pygame.mouse.get_pos()

    frame_per_sec.tick(60)
    curseur = pygame.mouse.get_pos()
    print(curseur)