from random import randint
import pygame

# from joueur import *

pygame.init()

class game:

    def __init__(self):

        self.player = player()

        self.is_running = True
        self.in_menu = True
        self.in_game = False
        self.in_choix_legends = False
        self.mouse = False

        ## CONSTANTES MENU
        self.menu_regles = False
        self.menu_regles_page = 1
        self.parametres = False

        ## CONSTANTES CHOIX LEGENDS
        self.pret_J1 = False
        self.pret_J2 = False
        self.menu_legends_J1 = 0
        self.menu_legends_J2 = 0
        self.list_legends = ['bigband', 'isis', 'gunnar', 'kitt', 'harry', 'lucie']

        #INFOS LEGENDS
        self.infos_legends_j1 = False
        self.infos_legends_j2 = False

        ## CONSTANTES INGAME
        self.tour = 1
        self.sujetsref = ["Ta mere", "Ton pere", "Ta femme", "Ton nez", "Tes chaussures", "Ton visage", "Ton art martial", "Ta facon de marcher", "Tes techniques"]
        self.sujets = ["Ta mere", "Ton pere", "Ta femme", "Ton nez", "Tes chaussures", "Ton visage", "Ton art martial", "Ta facon de marcher", "Tes techniques"]
        self.verbesref = ["est", "sera", "deviendra", "ressemblent a", "ne corresponds pas", "n'est pas capable de", "me fait penser a ", "palit en comparaison avec", "est si moche"]
        self.verbes = ["est", "sera", "deviendra", "ressemblent a", "ne corresponds pas", "n'est pas capable de", "me fait penser a ", "palit en comparaison avec ", "est si moche"]
        self.complementref = ["une chevre ", "a un bouillon de legumes", "de la mienne/du mien", "vivre librement", "etre a ma hauteur", "aux marche aux esclaves", "un poulet roti", "te porter chance", "me rendre sourd"]
        self.complement = ["une chevre ", "a un bouillon de legumes", "de la mienne/du mien", "vivre librement", "etre a ma hauteur", "aux marche aux esclaves", "un poulet roti", "te porter chance", "me rendre sourd"]
        self.liaisonref = ["a", "de", "pour", "des", "et", "car", "alors que", "sous pretexte que", "a l'image de"]
        self.liaison = ["a", "de", "pour", "des", "et", "car", "alors que", "sous pretexte que", "a l'image de"]
        self.finalref = [",c'est repugnant !", ",quelle honte !", ". Tu n'as pas la moindre chance contre moi !", ", vieux plouc !", ", grand pignouf !", ", sagounins des herbes !", ", babolard de premiere !", ",tete de sac a patate !", ", sale paysan !"]
        self.final = [",c'est repugnant !", ",quelle honte !", ". Tu n'as pas la moindre chance contre moi !", ", vieux plouc !", ", grand pignouf !", ", sagounins des herbes !", ", babolard de premiere !", ",tete de sac a patate !", ", sale paysan !"]
        self.stage_select = None
        self.alpha = 300

        ### STATS DES LEGENDS
        self.stats = {
            'bigband': ('Musique', 'Laboratoire'),
            'gunnar': ('Passe', 'Look'),
            'harry': ('Famille', 'Look'),
            'isis': ('Age', 'Look'),
            'kitt': ('Laboratoire', 'Musique'),
            'lucie': ('Famille', 'Age'),
        }
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
                'fond_regles_1' : pygame.image.load('assets/image/regles_1.png'),
                'fond_regles_2' : pygame.image.load('assets/image/regles_2.png'),
                'fleche_regles_1' : pygame.image.load('assets/image/Personnages/Menu/fleche_droite.png'),
                'fleche_regles_2' : pygame.image.load('assets/image/Personnages/Menu/fleche_gauche.png'),
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

                # Bouton cartes info
                "bouton_fermer_infos" : pygame.image.load('assets/image/Personnages/Menu/infos/fermer_infos.png'),
                "bouton_infos_j1" : pygame.image.load('assets/image/Personnages/Menu/infos/bouton_infos.png'),
                "bouton_infos_j2" : pygame.image.load('assets/image/Personnages/Menu/infos/bouton_infos.png'),

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

                    # Kitt
                    'kitt_J1_off': pygame.image.load('assets/image/Personnages/Menu/Cartes_J1/kitt_J1.png'),
                    'kitt_J1_on': pygame.image.load('assets/image/Personnages/Menu/Cartes_J1/kitt_selectionnee_J1.png'),
                    'kitt_J2_off': pygame.image.load('assets/image/Personnages/Menu/Cartes_J2/kitt_J2.png'),
                    'kitt_J2_on': pygame.image.load('assets/image/Personnages/Menu/Cartes_J2/kitt_selectionnee_J2.png'),

                    # Lucie
                    'lucie_J1_off': pygame.image.load('assets/image/Personnages/Menu/Cartes_J1/lucie_J1.png'),
                    'lucie_J1_on': pygame.image.load('assets/image/Personnages/Menu/Cartes_J1/lucie_selectionnee_J1.png'),
                    'lucie_J2_off': pygame.image.load('assets/image/Personnages/Menu/Cartes_J2/lucie_J2.png'),
                    'lucie_J2_on': pygame.image.load('assets/image/Personnages/Menu/Cartes_J2/lucie_selectionnee_J2.png'),
                
                ## Infos personnages

                    'isis_infos' : pygame.image.load('assets/image/Personnages/Menu/infos/info_isis.png'),
                    'gunnar_infos' : pygame.image.load('assets/image/Personnages/Menu/infos/info_gunnar.png'),
                    'kitt_infos' : pygame.image.load('assets/image/Personnages/Menu/infos/info_kitt.png'),
                    'lucie_infos' : pygame.image.load('assets/image/Personnages/Menu/infos/info_lucie.png'),
                    'harry_infos' : pygame.image.load('assets/image/Personnages/Menu/infos/info_harry.png'),
                    'bigband_infos' : pygame.image.load('assets/image/Personnages/Menu/infos/info_bigband.png'),




            ### IN-GAME

                ## Personnage en jeu

                    # Bigband
                    'bigband_J1_1': pygame.image.load('assets/image/Personnages/Bigband/bigband_J1/Bigband_neutre_J1.png'),
                    'bigband_J1_2': pygame.image.load('assets/image/Personnages/Bigband/bigband_J1/Bigband_neutre_J1.png'),
                    'bigband_J1_3': pygame.image.load('assets/image/Personnages/Bigband/bigband_J1/Bigband_neutre_J1.png'),
                    'bigband_J2_1': pygame.image.load('assets/image/Personnages/Bigband/bigband_J2/Bigband_neutre_J2.png'),
                    'bigband_J2_2': pygame.image.load('assets/image/Personnages/Bigband/bigband_J2/Bigband_neutre_J2.png'),
                    'bigband_J2_3': pygame.image.load('assets/image/Personnages/Bigband/bigband_J2/Bigband_neutre_J2.png'),

                    # Gunnar
                    'gunnar_J1_1': pygame.image.load('assets/image/Personnages/Gunnar/gunnar_J1/Gunnar_neutre_J1.png'),
                    'gunnar_J1_2': pygame.image.load('assets/image/Personnages/Gunnar/gunnar_J1/Gunnar_neutre_J1.png'),
                    'gunnar_J1_3': pygame.image.load('assets/image/Personnages/Gunnar/gunnar_J1/Gunnar_neutre_J1.png'),
                    'gunnar_J2_1': pygame.image.load('assets/image/Personnages/Gunnar/gunnar_J2/Gunnar_neutre_J2.png'),
                    'gunnar_J2_2': pygame.image.load('assets/image/Personnages/Gunnar/gunnar_J2/Gunnar_neutre_J2.png'),
                    'gunnar_J2_3': pygame.image.load('assets/image/Personnages/Gunnar/gunnar_J2/Gunnar_neutre_J2.png'),

                    # Harry
                    'harry_J1_1': pygame.image.load('assets/image/Personnages/Harry/harry_J1/Harry_neutre_J1.png'),
                    'harry_J1_2': pygame.image.load('assets/image/Personnages/Harry/harry_J1/Harry_neutre_J1.png'),
                    'harry_J1_3': pygame.image.load('assets/image/Personnages/Harry/harry_J1/Harry_neutre_J1.png'),
                    'harry_J2_1': pygame.image.load('assets/image/Personnages/Harry/harry_J2/Harry_neutre_J2.png'),
                    'harry_J2_2': pygame.image.load('assets/image/Personnages/Harry/harry_J2/Harry_neutre_J2.png'),
                    'harry_J2_3': pygame.image.load('assets/image/Personnages/Harry/harry_J2/Harry_neutre_J2.png'),

                    # Isis
                    'isis_J1_1': pygame.image.load('assets/image/Personnages/Isis/isis_J1/Isis_neutre_J1.png'),
                    'isis_J1_2': pygame.image.load('assets/image/Personnages/Isis/isis_J1/Isis_neutre_J1.png'),
                    'isis_J1_3': pygame.image.load('assets/image/Personnages/Isis/isis_J1/Isis_neutre_J1.png'),
                    'isis_J2_1': pygame.image.load('assets/image/Personnages/Isis/isis_J2/Isis_neutre_J2.png'),
                    'isis_J2_2': pygame.image.load('assets/image/Personnages/Isis/isis_J2/Isis_neutre_J2.png'),
                    'isis_J2_3': pygame.image.load('assets/image/Personnages/Isis/isis_J2/Isis_neutre_J2.png'),

                    # Kitt
                    'kitt_J1_1': pygame.image.load('assets/image/Personnages/K.I.T.T/kitt_J1/Kitt_1_J1.png'),
                    'kitt_J1_2': pygame.image.load('assets/image/Personnages/K.I.T.T/kitt_J1/Kitt_1_J1.png'),
                    'kitt_J1_3': pygame.image.load('assets/image/Personnages/K.I.T.T/kitt_J1/Kitt_1_J1.png'),
                    'kitt_J2_1': pygame.image.load('assets/image/Personnages/K.I.T.T/kitt_J2/Kitt_1_J2.png'),
                    'kitt_J2_2': pygame.image.load('assets/image/Personnages/K.I.T.T/kitt_J2/Kitt_1_J2.png'),
                    'kitt_J2_3': pygame.image.load('assets/image/Personnages/K.I.T.T/kitt_J2/Kitt_1_J2.png'),

                    # Lucie
                    'lucie_J1_1': pygame.image.load('assets/image/Personnages/Lucie/lucie_J1/Lucie_neutre_J1.png'),
                    'lucie_J1_2': pygame.image.load('assets/image/Personnages/Lucie/lucie_J1/Lucie_neutre_J1.png'),
                    'lucie_J1_3': pygame.image.load('assets/image/Personnages/Lucie/lucie_J1/Lucie_neutre_J1.png'),
                    'lucie_J2_1': pygame.image.load('assets/image/Personnages/Lucie/lucie_J2/Lucie_neutre_J2.png'),
                    'lucie_J2_2': pygame.image.load('assets/image/Personnages/Lucie/lucie_J2/Lucie_neutre_J2.png'),
                    'lucie_J2_3': pygame.image.load('assets/image/Personnages/Lucie/lucie_J2/Lucie_neutre_J2.png'),

                ## Nuages de texte
                'nuage_J1' : pygame.image.load('assets/image/en_jeu/nuage_J1.png'),
                'nuage_J2' : pygame.image.load('assets/image/en_jeu/nuage_J2.png'),

                ## Background

                    #Isis
                    'isis_back' : pygame.image.load('assets/image/en_jeu/background/isis_background.jpg'),

                    #Bigband
                    'bigband_back' : pygame.image.load('assets/image/en_jeu/background/bigband_background.jpg'),

                    #K.I.T.T
                    'kitt_back' : pygame.image.load('assets/image/en_jeu/background/kitt_background.jpg'),

                    #Gunnar
                    'gunnar_back' : pygame.image.load('assets/image/en_jeu/background/gunnar_background.jpg'),

                    #Lucie
                    'lucie_back' : pygame.image.load('assets/image/en_jeu/background/lucie_background.jpg'),

                    #Harry
                    'harry_back' : pygame.image.load('assets/image/en_jeu/background/harry_background.jpg'),
        }

        ### RECT DU JEU
        self.rect = {
            ## MENU
            'bouton_jouer_hover_rect' : self.image['bouton_jouer_hover'].get_rect(),
            'bouton_regles_hover_rect' : self.image['bouton_regles_hover'].get_rect(),
            'bouton_parametres_hover_rect' : self.image['bouton_parametres_hover'].get_rect(),
            'bouton_quitter_hover_rect' : self.image['bouton_quitter_hover'].get_rect(),
            'bouton_fermer_rect' : self.image['bouton_fermer'].get_rect(),
            'bouton_regles_1' : self.image['fleche_regles_1'].get_rect(),
            'bouton_regles_2' : self.image['fleche_regles_2'].get_rect(),

            ## CHOIX LEGENDS
            'jouer_rect': self.image['jouer_off'].get_rect(),
            'pret_rect_J1': self.image['pret_off'].get_rect(),
            'pret_rect_J2': self.image['pret_off'].get_rect(),
            'fleche_gauche_rect_J1': self.image['fleche_gauche'].get_rect(),
            'fleche_droite_rect_J1': self.image['fleche_droite'].get_rect(),
            'fleche_gauche_rect_J2': self.image['fleche_gauche'].get_rect(),
            'fleche_droite_rect_J2': self.image['fleche_droite'].get_rect(),
            'bouton_retour_rect': self.image['bouton_retour'].get_rect(),
            'bouton_infos_j1' : self.image['bouton_infos_j1'].get_rect(),
            'bouton_infos_j2' : self.image['bouton_infos_j2'].get_rect(),
            'bouton_fermer_infos_j1' : self.image['bouton_fermer_infos'].get_rect(),
            'bouton_fermer_infos_j2' : self.image['bouton_fermer_infos'].get_rect(),

            ## IN-GAME
            

        }


class player:
    def __init__(self):
        self.Hp_J1 = 500
        self.Hp_J2 = 500
        self.max_Hp_J1 = 500
        self.max_Hp_J2 = 500
        self.Hp_J1 = 500
        self.Hp_J2 = 500
        # barre de vie
        self.bar_position_J2 = [920, 20, self.max_Hp_J2, 50]
        self.bar_vie_J1 = (0, 204, 82)
        self.bar_vie_J2 = (0, 204, 82)
        self.legends_J1 = None
        self.legends_J2 = None
        self.faiblesse_J1 = None
        self.faiblesse_J2 = None


