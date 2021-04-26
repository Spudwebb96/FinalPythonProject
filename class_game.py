import pygame

from joueur import player_one

pygame.init()

class game:

    def __init__(self):

        '''self.player_one = player_one()'''
        self.is_running = True
        self.menu_regles = False
        self.mouse = False
        ### IMAGE DU JEU
        self.image = {

            # Background
            'background_menu' : pygame.image.load('assets/image/fond_menu.jpg'),

            # Curseurs
            'image_curseur' : pygame.image.load('assets/image/curseur.png'),
            'image_curseur_click' : pygame.image.load('assets/image/curseur_click.png'),

            # Bouton menu
            'bouton_jouer' : pygame.image.load('assets/image/bouton_jouer.png'),
            'bouton_regles' : pygame.image.load('assets/image/bouton_regles.png'),
            'bouton_parametres' : pygame.image.load('assets/image/bouton_parametres.png'),
            'bouton_quitter' : pygame.image.load('assets/image/bouton_quitter.png'),

            # Bouton menu hover
            'bouton_jouer_hover' : pygame.image.load('assets/image/bouton_jouer_hover.png'),
            'bouton_regles_hover' : pygame.image.load('assets/image/bouton_regles_hover.png'),
            'bouton_parametres_hover' : pygame.image.load('assets/image/bouton_parametres_hover.png'),
            'bouton_quitter_hover' : pygame.image.load('assets/image/bouton_quitter_hover.png'),

            'fond_regles' : pygame.image.load('assets/image/fond_regles.png'),
            'bouton_fermer' : pygame.image.load('assets/image/fermer.png'),

        }


        ### RECT DU JEU
        self.rect = {
            'bouton_jouer_hover_rect' : self.image['bouton_jouer_hover'].get_rect(),
            'bouton_regles_hover_rect' : self.image['bouton_regles_hover'].get_rect(),
            'bouton_parametres_hover_rect' : self.image['bouton_parametres_hover'].get_rect(),
            'bouton_quitter_hover_rect' : self.image['bouton_quitter_hover'].get_rect(),
            'bouton_fermer_rect' : self.image['bouton_fermer'].get_rect(),
            
        }