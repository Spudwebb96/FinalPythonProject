import pygame

# from joueur import *

pygame.init()

class game:

    def __init__(self):

        '''self.player_one = player_one()'''
        self.is_running = True
        self.in_menu = True
        self.in_choix_legends = False
        self.menu_regles = False
        self.mouse = False
        self.tour = 1
        ### IMAGE DU JEU
        self.image = {
            ### MENU
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

                # Image regles
                'fond_regles' : pygame.image.load('assets/image/fond_regles.png'),
                'bouton_fermer' : pygame.image.load('assets/image/fermer.png'),

            ### MENU JOUER
                # Background
                'background_menu_jouer': pygame.image.load('assets/image/Personnages/Menu/fond_menu_jouer.jpg'),

                # Image statique
                'choisir': pygame.image.load('assets/image/Personnages/Menu/choisir.png'),

                # boutton dynamique
                'jouer_off': pygame.image.load('assets/image/Personnages/Menu/bouton_jouer_menu_jouer.png'),
                'jouer_on': pygame.image.load('assets/image/Personnages/Menu/bouton_jouer_menu_jouer.png'),

                'pret_off': pygame.image.load('assets/image/Personnages/Menu/bouton_jouer_menu_jouer.png'),
                'pret_on': pygame.image.load('assets/image/Personnages/Menu/bouton_jouer_menu_jouer.png'),


        }


        ### RECT DU JEU
        self.rect = {
            'bouton_jouer_hover_rect' : self.image['bouton_jouer_hover'].get_rect(),
            'bouton_regles_hover_rect' : self.image['bouton_regles_hover'].get_rect(),
            'bouton_parametres_hover_rect' : self.image['bouton_parametres_hover'].get_rect(),
            'bouton_quitter_hover_rect' : self.image['bouton_quitter_hover'].get_rect(),
            'bouton_fermer_rect' : self.image['bouton_fermer'].get_rect(),
        }

        ''' POUR LE FICHIER INGAME.PY
        self.sujetsref = [ 1, 2, 3, 4 ,5 ,6 ,7 ,8 ,9]
        self.sujets = [ 1, 2, 3, 4 ,5 ,6 ,7 ,8 ,9]
        self.verbesref = [ "a", "b", "c", "d" ,"e" ,"f" ,"g" ,"h" ,"i"]
        self.verbes = [ "a", "b", "c", "d" ,"e" ,"f" ,"g" ,"h" ,"i"]
        self.complementref = [ 10, 11, 12, 13 ,14 ,15 ,16 ,17 ,18]
        self.complement = [ 10, 11, 12, 13 ,14 ,15 ,16 ,17 ,18]

        x = randint(0,8)

        self.prop.append(self.sujets[x])
        self.prop.pop[x]

        # rajouter les liaisons INCHALLAH
        # La liste ne doit pas se remplir apres le debut du round, seulement une fois au debut de chaque round.

        
        # def proposition() :
        #     self.prop = []
        #     while len(self.prop) < 9 and self.tour < 1 :
        #         x = randint(0,8)
        #         y = randint(0,8)
        #         z = randint(0,8)

        #         self.prop += self.verbes[x]
        #         self.prop += self.sujets[y]
        #         self.prop += self.complement[z]

        #         if self.prop[x] == self.prop[x-3] :'''

                

