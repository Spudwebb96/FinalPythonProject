import pygame
pygame.init()
from classjoueur import joueur


# donner le nom a la fenetre de jeu :
pygame.display.set_caption("Words Legends")

# definir la taille de la fenetre :
fenetre = pygame.display.set_mode((1440, 1024))

joueur = joueur()

running = True

# ## LE MENU

# le background
backgroundmenu = pygame.image.load('assets/ecran menu.jpg')

# le titre
Title_game = pygame.image.load('assets/titre.png')
Title_game = pygame.transform.scale(Title_game, (1500, 1100))

# le button
Button_play = pygame.image.load('assets/button play.png')
Button_play = pygame.transform.scale(Button_play, (200, 200))
Button_play_rect = Button_play.get_rect()
Button_play_rect.x = 633
Button_play_rect.y = 500
# les backgrounds

background1 = pygame.image.load('assets/arène.jpg')


while joueur.is_playing:

    if joueur.in_menu:
        joueur.update(fenetre)

        fenetre.blit(backgroundmenu, (0, 0))

        fenetre.blit(Title_game, (-50, -50))

        fenetre.blit(Button_play, (633, 500))


    else:
        # chargement de background
        fenetre.blit(background1, (-300, 0))

        # test chargement joueur
        fenetre.blit(joueur.image, joueur.rect)


    # permet de mettre a jour l'écran :
    pygame.display.flip()

    for event in pygame.event.get():

        if event.type == pygame.MOUSEBUTTONDOWN:
            if Button_play_rect.collidepoint(event.pos):
                joueur.in_menu = False

        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
