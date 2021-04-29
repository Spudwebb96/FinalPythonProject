import pygame
import class_game
from fonctions import *
from class_game import *
pygame.init()

'''p1 = player("P1")
P2 = player("P2")'''

def Combat():
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            while len(p1.phrase1) < 3 and len(p2.phrase2) < 3:
                if game.tour%2 == 1:
                    p1.phrase1.append(p1.prop[x])
                    p1.tour += 1
                if game.tour%2 == 0:
                    p2.phrase2.append(p2.prop[x])
                    p2.tour += 1

def barre_de_vie(game,display_surface):
    bar_vie = (111, 210, 46)
    bar_losehp = (255, 211, 121)
    bar_background = (0,0,0)
    bar_position_J1 = [20, 20, 500, 50]
    bar_position_J2 = [ 920, 20, 500, 50]

    #j1
    pygame.draw.rect(display_surface, bar_vie, bar_position_J1,0,25)
    pygame.draw.rect(display_surface, bar_losehp, bar_position_J1,0,25)
    pygame.draw.rect(display_surface, bar_background, bar_position_J1,5,25)

    #j2
    pygame.draw.rect(display_surface, bar_vie, bar_position_J2,0,25)
    pygame.draw.rect(display_surface, bar_losehp, bar_position_J2,0,25)
    pygame.draw.rect(display_surface, bar_background, bar_position_J2,5,25)
    
    bar_position_J1[2] = game.player.Hp_J1

def choix_background(game,display_surface):
    if game.player.legends_J1 == 'bigband':
        display_surface.blit(game.image['isis_back'], (0, 0))


def remplir_tableau():
    x = randint(0,8)
    game.prop.append(self.sujets[x])
    game.prop.pop[x]

def tableau_prop(display_surface):
    tableau_prop = (179,148,85)
    tableau_position = [545, 324, 350, 650]
    pygame.draw.rect(display_surface, tableau_prop, tableau_position)

def in_game(game,display_surface):
    choix_background(game,display_surface)
    # tableau_prop(display_surface)
    if game.player.legends_J1 == 'bigband':
        display_surface.blit(game.image['bigband_J1_1'], (0, 224))
    elif game.player.legends_J1 == 'gunnar':
        display_surface.blit(game.image['gunnar_J1_1'], (0, 224))
    elif game.player.legends_J1 == 'harry':
        display_surface.blit(game.image['harry_J1_1'], (0, 224))
    elif game.player.legends_J1 == 'isis':
        display_surface.blit(game.image['isis_J1_1'], (0, 224))
    elif game.player.legends_J1 == 'kitt':
        display_surface.blit(game.image['kitt_J1_1'], (0, 224))
    elif game.player.legends_J1 == 'lucie':
        display_surface.blit(game.image['lucie_J1_1'], (0, 224))

    if game.player.legends_J2 == 'bigband':
        display_surface.blit(game.image['bigband_J2_1'], (924.02, 224))
    elif game.player.legends_J2 == 'gunnar':
        display_surface.blit(game.image['gunnar_J2_1'], (728.76, 224))
    elif game.player.legends_J2 == 'harry':
        display_surface.blit(game.image['harry_J2_1'], (777.14, 224))
    elif game.player.legends_J2 == 'isis':
        display_surface.blit(game.image['isis_J2_1'], (824.62, 224))
    elif game.player.legends_J2 == 'kitt':
        display_surface.blit(game.image['kitt_J2_1'], (728.76, 224))
    else:
        display_surface.blit(game.image['lucie_J2_1'], (836.91, 224))

    barre_de_vie(game,display_surface)
   

    # Effet fond noir transparent
    if game.alpha != 0:
        fond_noir_surface = pygame.Surface((1440, 1024))
        fond_noir_surface.set_alpha(game.alpha)
        fond_noir_surface.fill((0, 0, 0))
        display_surface.blit(fond_noir_surface, (0, 0))
        game.alpha = game.alpha - 10
        pygame.time.delay(30)
    print(game.player.faiblesse_J1,game.player.faiblesse_J2)


