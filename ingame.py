from random import randint
import pygame
import class_game
import time
from fonctions import *
from class_game import *
pygame.init()

def in_game(game,display_surface):
    choix_background_local(game,display_surface)
    tableau_prop(game, display_surface)
    ''' neutre, un coup, je meurs, gagné, mon tours'''
    def affichage_joueur(game,display_surface):
        if game.tour == 1 :
            if game.player.legends_J1 == 'bigband':
                display_surface.blit(game.image['bigband_J1_1'], (0, 224))
            elif game.player.legends_J1 == 'gunnar':
                display_surface.blit(game.image['gunnar_J1_1'], (-10, 224))
            elif game.player.legends_J1 == 'harry':
                display_surface.blit(game.image['harry_J1_1'], (0, 224))
            elif game.player.legends_J1 == 'isis':
                display_surface.blit(game.image['isis_J1_1'], (0, 224))
            elif game.player.legends_J1 == 'kitt':
                display_surface.blit(game.image['kitt_J1_1'], (0, 224))
            elif game.player.legends_J1 == 'lucie':
                display_surface.blit(game.image['lucie_J1_1'], (0, 224))
        elif game.player.max_Hp_J1 != game.player.Hp_J1:
            if game.player.legends_J1 == 'bigband':
                display_surface.blit(game.image['bigband_J1_2'], (0, 224))
            elif game.player.legends_J1 == 'gunnar':
                display_surface.blit(game.image['gunnar_J1_2'], (-10, 224))
            elif game.player.legends_J1 == 'harry':
                display_surface.blit(game.image['harry_J1_2'], (0, 224))
            elif game.player.legends_J1 == 'isis':
                display_surface.blit(game.image['isis_J1_2'], (0, 224))
            elif game.player.legends_J1 == 'kitt':
                display_surface.blit(game.image['kitt_J1_2'], (0, 224))
            elif game.player.legends_J1 == 'lucie':
                display_surface.blit(game.image['lucie_J1_2'], (0, 224))
        elif game.player.max_Hp_J1 == 0:
            if game.player.legends_J1 == 'bigband':
                display_surface.blit(game.image['bigband_J1_3'], (0, 224))
            elif game.player.legends_J1 == 'gunnar':
                display_surface.blit(game.image['gunnar_J1_3'], (-10, 224))
            elif game.player.legends_J1 == 'harry':
                display_surface.blit(game.image['harry_J1_3'], (0, 224))
            elif game.player.legends_J1 == 'isis':
                display_surface.blit(game.image['isis_J1_3'], (0, 224))
            elif game.player.legends_J1 == 'kitt':
                display_surface.blit(game.image['kitt_J1_3'], (0, 224))
            elif game.player.legends_J1 == 'lucie':
                display_surface.blit(game.image['lucie_J1_3'], (0, 224))
        elif game.player.max_Hp_J2 == 0:
            if game.player.legends_J1 == 'bigband':
                display_surface.blit(game.image['bigband_J1_4'], (0, 224))
            elif game.player.legends_J1 == 'gunnar':
                display_surface.blit(game.image['gunnar_J1_4'], (-10, 224))
            elif game.player.legends_J1 == 'harry':
                display_surface.blit(game.image['harry_J1_4'], (0, 224))
            elif game.player.legends_J1 == 'isis':
                display_surface.blit(game.image['isis_J1_4'], (0, 224))
            elif game.player.legends_J1 == 'kitt':
                display_surface.blit(game.image['kitt_J1_4'], (0, 224))
            elif game.player.legends_J1 == 'lucie':
                display_surface.blit(game.image['lucie_J1_4'], (0, 224))
        else:
            if game.player.legends_J1 == 'bigband':
                display_surface.blit(game.image['bigband_J1_5'], (0, 224))
            elif game.player.legends_J1 == 'gunnar':
                display_surface.blit(game.image['gunnar_J1_5'], (-10, 224))
            elif game.player.legends_J1 == 'harry':
                display_surface.blit(game.image['harry_J1_5'], (0, 224))
            elif game.player.legends_J1 == 'isis':
                display_surface.blit(game.image['isis_J1_5'], (0, 224))
            elif game.player.legends_J1 == 'kitt':
                display_surface.blit(game.image['kitt_J1_5'], (0, 224))
            elif game.player.legends_J1 == 'lucie':
                display_surface.blit(game.image['lucie_J1_5'], (0, 224))



        if game.tour == 0:
            if game.player.legends_J2 == 'bigband':
                display_surface.blit(game.image['bigband_J2_1'], (924.02, 224))
            elif game.player.legends_J2 == 'gunnar':
                display_surface.blit(game.image['gunnar_J2_1'], (738.76, 224))
            elif game.player.legends_J2 == 'harry':
                display_surface.blit(game.image['harry_J2_1'], (777.14, 224))
            elif game.player.legends_J2 == 'isis':
                display_surface.blit(game.image['isis_J2_1'], (824.62, 224))
            elif game.player.legends_J2 == 'kitt':
                display_surface.blit(game.image['kitt_J2_1'], (728.76, 224))
            else:
                display_surface.blit(game.image['lucie_J2_1'], (836.91, 224))
        elif game.player.max_Hp_J2 != game.player.Hp_J2:
            if game.player.legends_J2 == 'bigband':
                display_surface.blit(game.image['bigband_J2_2'], (924.02, 224))
            elif game.player.legends_J2 == 'gunnar':
                display_surface.blit(game.image['gunnar_J2_2'], (738.76, 224))
            elif game.player.legends_J2 == 'harry':
                display_surface.blit(game.image['harry_J2_2'], (777.14, 224))
            elif game.player.legends_J2 == 'isis':
                display_surface.blit(game.image['isis_J2_2'], (824.62, 224))
            elif game.player.legends_J2 == 'kitt':
                display_surface.blit(game.image['kitt_J2_2'], (728.76, 224))
            else:
                display_surface.blit(game.image['lucie_J2_2'], (836.91, 224))
        elif game.player.max_Hp_J2 == 0 :
            if game.player.legends_J2 == 'bigband':
                display_surface.blit(game.image['bigband_J2_3'], (924.02, 224))
            elif game.player.legends_J2 == 'gunnar':
                display_surface.blit(game.image['gunnar_J2_3'], (738.76, 224))
            elif game.player.legends_J2 == 'harry':
                display_surface.blit(game.image['harry_J2_3'], (777.14, 224))
            elif game.player.legends_J2 == 'isis':
                display_surface.blit(game.image['isis_J2_3'], (824.62, 224))
            elif game.player.legends_J2 == 'kitt':
                display_surface.blit(game.image['kitt_J2_3'], (728.76, 224))
            else:
                display_surface.blit(game.image['lucie_J2_3'], (836.91, 224))
        elif game.player.max_Hp_J1 == 0:
            if game.player.legends_J2 == 'bigband':
                display_surface.blit(game.image['bigband_J2_4'], (924.02, 224))
            elif game.player.legends_J2 == 'gunnar':
                display_surface.blit(game.image['gunnar_J2_4'], (738.76, 224))
            elif game.player.legends_J2 == 'harry':
                display_surface.blit(game.image['harry_J2_4'], (777.14, 224))
            elif game.player.legends_J2 == 'isis':
                display_surface.blit(game.image['isis_J2_4'], (824.62, 224))
            elif game.player.legends_J2 == 'kitt':
                display_surface.blit(game.image['kitt_J2_4'], (728.76, 224))
            else:
                display_surface.blit(game.image['lucie_J2_4'], (836.91, 224))
        else :
            if game.player.legends_J1 == 'bigband':
                display_surface.blit(game.image['bigband_J2_5'], (0, 224))
            elif game.player.legends_J1 == 'gunnar':
                display_surface.blit(game.image['gunnar_J2_5'], (-10, 224))
            elif game.player.legends_J1 == 'harry':
                display_surface.blit(game.image['harry_J2_5'], (0, 224))
            elif game.player.legends_J1 == 'isis':
                display_surface.blit(game.image['isis_J2_5'], (0, 224))
            elif game.player.legends_J1 == 'kitt':
                display_surface.blit(game.image['kitt_J2_5'], (0, 224))
            elif game.player.legends_J1 == 'lucie':
                display_surface.blit(game.image['lucie_J2_5'], (0, 224))
    affichage_joueur(game,display_surface)


    display_surface.blit(game.image['nuage_J1'], (20,87))
    display_surface.blit(game.image['nuage_J2'], (767,87))
    nuage(game, display_surface)

    barre_de_vie(game,display_surface)
   

    # Effet fond noir transparent
    if game.alpha != 0:
        fond_noir_surface = pygame.Surface((1440, 1024))
        fond_noir_surface.set_alpha(game.alpha)
        fond_noir_surface.fill((0, 0, 0))
        display_surface.blit(fond_noir_surface, (0, 0))
        game.alpha = game.alpha - 5



