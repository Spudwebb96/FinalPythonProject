from random import randint
import pygame

# from joueur import *

pygame.init()

class game:

    def __init__(self):

        '''self.player_one = player_one()'''
        self.is_running = True
        self.in_menu = True
        self.in_choix_legends = False
        self.mouse = False

        ## CONSTANTES MENU
        self.menu_regles = False
        self.parametres = False

        ## CONSTANTES CHOIX LEGENDS
        self.pret_J1 = False
        self.pret_J2 = False
        self.jouer = False
        self.legends_J1 = 1
        self.legends_J2 = 1

        ## CONSTANTES INGAME
        self.tour = 1
        self.sujetsref = ["Ta mere", "Ton pere", "Ta femme", "Ton nez", "Tes chaussures", "Ton visage", "Ton art martial", "Ta facon de marcher", "Tes techniques"]
        self.sujets = ["Ta mere", "Ton pere", "Ta femme", "Ton nez", "Tes chaussures", "Ton visage", "Ton art martial", "Ta facon de marcher", "Tes techniques"]
        self.verbesref = ["est", "sera", "deviendra", "ressemblent a", "ne corresponds pas", "n'est pas capable de", "me fait penser a ", "palit en comparaison avec", "est si moche"]
        self.verbes = ["est", "sera", "deviendra", "ressemblent a", "ne corresponds pas", "n'est pas capable de", "me fait penser a ", "palit en comparaison avec ", "est si moche"]
        self.complementref = ["une veritable chevre ", "a un bouillon de legumes", "de la mienne/du mien", "vivre librement", "etre a ma hauteur", "aux marche aux esclaves", "un poulet roti", "te porter chance", "me rendre sourd"]
        self.complement = ["une veritable chevre ", "a un bouillon de legumes", "de la mienne/du mien", "vivre librement", "etre a ma hauteur", "aux marche aux esclaves", "un poulet roti", "te porter chance", "me rendre sourd"]
        self.liaisonref = ["a", "de", "pour", "des", "et", "car", "alors que", "sous pretexte que", "a l'image de"]
        self.liaison = ["a", "de", "pour", "des", "et", "car", "alors que", "sous pretexte que", "a l'image de"]
        self.finalref = [",c'est repugnant !", ",quelle honte !", ". Tu n'as pas la moindre chance contre moi !", ", vieux plouc !", ", grand pignouf !", ", sagounins des herbes !", ", babolard de premiere !", ",tete de sac a patate !", ", sale paysan !"]
        self.final = [",c'est repugnant !", ",quelle honte !", ". Tu n'as pas la moindre chance contre moi !", ", vieux plouc !", ", grand pignouf !", ", sagounins des herbes !", ", babolard de premiere !", ",tete de sac a patate !", ", sale paysan !"]
        x = randint(0,8) 

        '''self.prop.append(self.sujets[x])
        self.prop.pop[x]'''
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
                'fond_regles' : pygame.image.load('assets/image/regles.png'),
                'bouton_fermer' : pygame.image.load('assets/image/fermer.png'),

            ### CHOIX LEGENDS

                # Background
                'background_menu_jouer': pygame.image.load('assets/image/Personnages/Menu/fond_choix_legends.jpg'),

                # Image statique
                'choisir': pygame.image.load('assets/image/Personnages/Menu/choisir.png'),

                # Bouton retour
                'bouton_retour': pygame.image.load('assets/image/Personnages/Menu/bouton_retour.png'),

                # Bouton dynamique
                'jouer_off': pygame.image.load('assets/image/Personnages/Menu/bouton_jouer_choix_legends.png'),
                'jouer_on': pygame.image.load('assets/image/Personnages/Menu/bouton_jouer_hover_choix_legends.png'),

                'pret_off': pygame.image.load('assets/image/Personnages/Menu/bouton_pret.png'),
                'pret_on': pygame.image.load('assets/image/Personnages/Menu/bouton_pret_hover.png'),

                # Bouton carrousel
                'fleche_droite': pygame.image.load('assets/image/Personnages/Menu/fleche_droite.png'),
                'fleche_gauche': pygame.image.load('assets/image/Personnages/Menu/fleche_gauche.png'),

                ## Carte personnage

                    # Bigband
                    'bigband_J1_off': pygame.image.load('assets/image/Personnages/Menu/Cartes_J1/bigband_J1.png'),
                    'bigband_J1_on': pygame.image.load('assets/image/Personnages/Menu/Cartes_J1/bigband_selectionne_J1.png'),
                    'bigband_J2_off': pygame.image.load('assets/image/Personnages/Menu/Cartes_J2/bigband_J2.png'),
                    'bigband_J2_on': pygame.image.load('assets/image/Personnages/Menu/Cartes_J2/bigband_selectionne_J2.png'),

                    # Gunnar
                    'gunnar_J1_off': pygame.image.load('assets/image/Personnages/Menu/Cartes_J1/gunnar_J1.png'),
                    'gunnar_J1_on': pygame.image.load('assets/image/Personnages/Menu/Cartes_J1/gunnar_selectionne_J1.png'),
                    'gunnar_J2_off': pygame.image.load('assets/image/Personnages/Menu/Cartes_J2/gunnar_J2.png'),
                    'gunnar_J2_on': pygame.image.load('assets/image/Personnages/Menu/Cartes_J2/gunnar_selectionne_J2.png'),

                    # Harry
                    'harry_J1_off': pygame.image.load('assets/image/Personnages/Menu/Cartes_J1/harry_J1.png'),
                    'harry_J1_on': pygame.image.load('assets/image/Personnages/Menu/Cartes_J1/harry_selectionne_J1.png'),
                    'harry_J2_off': pygame.image.load('assets/image/Personnages/Menu/Cartes_J2/harry_J2.png'),
                    'harry_J2_on': pygame.image.load('assets/image/Personnages/Menu/Cartes_J2/harry_selectionne_J2.png'),

                    # Isis
                    'isis_J1_off': pygame.image.load('assets/image/Personnages/Menu/Cartes_J1/isis_J1.png'),
                    'isis_J1_on': pygame.image.load('assets/image/Personnages/Menu/Cartes_J1/isis_selectionnee_J1.png'),
                    'isis_J2_off': pygame.image.load('assets/image/Personnages/Menu/Cartes_J2/isis_J2.png'),
                    'isis_J2_on': pygame.image.load('assets/image/Personnages/Menu/Cartes_J2/isis_selectionnee_J2.png'),

                    # Kitt_J2
                    'kitt_J1_off': pygame.image.load('assets/image/Personnages/Menu/Cartes_J1/kitt_J1.png'),
                    'kitt_J1_on': pygame.image.load('assets/image/Personnages/Menu/Cartes_J1/kitt_selectionnee_J1.png'),
                    'kitt_J2_off': pygame.image.load('assets/image/Personnages/Menu/Cartes_J2/kitt_J2.png'),
                    'kitt_J2_on': pygame.image.load('assets/image/Personnages/Menu/Cartes_J2/kitt_selectionnee_J2.png'),

                    # Lucie_J2
                    'lucie_J1_off': pygame.image.load('assets/image/Personnages/Menu/Cartes_J1/lucie_J1.png'),
                    'lucie_J1_on': pygame.image.load('assets/image/Personnages/Menu/Cartes_J1/lucie_selectionnee_J1.png'),
                    'lucie_J2_off': pygame.image.load('assets/image/Personnages/Menu/Cartes_J2/lucie_J2.png'),
                    'lucie_J2_on': pygame.image.load('assets/image/Personnages/Menu/Cartes_J2/lucie_selectionnee_J2.png'),

            ### IN-GAME
            
        }

        ### RECT DU JEU
        self.rect = {
            ## MENU
            'bouton_jouer_hover_rect' : self.image['bouton_jouer_hover'].get_rect(),
            'bouton_regles_hover_rect' : self.image['bouton_regles_hover'].get_rect(),
            'bouton_parametres_hover_rect' : self.image['bouton_parametres_hover'].get_rect(),
            'bouton_quitter_hover_rect' : self.image['bouton_quitter_hover'].get_rect(),
            'bouton_fermer_rect' : self.image['bouton_fermer'].get_rect(),

            ## CHOIX LEGENDS
            'jouer_rect': self.image['jouer_off'].get_rect(),
            'pret_rect_J1': self.image['pret_off'].get_rect(),
            'pret_rect_J2': self.image['pret_off'].get_rect(),
            'fleche_gauche_rect_J1': self.image['fleche_gauche'].get_rect(),
            'fleche_droite_rect_J1': self.image['fleche_droite'].get_rect(),
            'fleche_gauche_rect_J2': self.image['fleche_gauche'].get_rect(),
            'fleche_droite_rect_J2': self.image['fleche_droite'].get_rect(),
            'bouton_retour_rect': self.image['bouton_retour'].get_rect(),

            ## IN-GAME

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

                

