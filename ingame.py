from random import randint
import pygame
import class_game
import time
from fonctions import *
from class_game import *
pygame.init()


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
    bar_border = (0, 0, 0)
    bar_losehp = (255, 211, 121)
    bar_position_J1 = [20, 20, game.player.max_Hp_J1, 50]
    ecart = game.player.max_Hp_J1 - game.player.Hp_J1

    #j1
    if game.player.max_Hp_J1 != game.player.Hp_J1:
        if game.player.max_Hp_J1 == 380:
            game.player.bar_vie_J1 = (232, 170, 14)
        elif game.player.max_Hp_J1 == 240:
            game.player.bar_vie_J1 = (205, 0, 0)
        pygame.draw.rect(display_surface, bar_losehp, [20, 20, 500, 50], 0, 25)
        pygame.draw.rect(display_surface, game.player.bar_vie_J1, bar_position_J1, 0, 25)
        pygame.draw.rect(display_surface, bar_border, [20, 20, 500, 50], 3, 25)
        game.player.max_Hp_J1 = game.player.max_Hp_J1 - 2

    else:
        pygame.draw.rect(display_surface, bar_losehp, [20, 20, 500, 50], 0, 25)
        pygame.draw.rect(display_surface, game.player.bar_vie_J1, bar_position_J1, 0, 25)
        pygame.draw.rect(display_surface, bar_border, [20, 20, 500, 50], 3, 25)

    #j2
    if game.player.max_Hp_J2 != game.player.Hp_J2:
        if game.player.max_Hp_J2 == 380:
            game.player.bar_vie_J2 = (232, 170, 14)
        elif game.player.max_Hp_J2 == 240:
            game.player.bar_vie_J2 = (205, 0, 0)
        pygame.draw.rect(display_surface, bar_losehp, [920, 20, 500, 50], 0, 25)
        pygame.draw.rect(display_surface, game.player.bar_vie_J2, game.player.bar_position_J2, 0, 25)
        pygame.draw.rect(display_surface, bar_border, [920, 20, 500, 50], 3, 25)
        game.player.max_Hp_J2 = game.player.max_Hp_J2 - 2
        game.player.bar_position_J2[0] = game.player.bar_position_J2[0] + 2
        game.player.bar_position_J2[2] = game.player.max_Hp_J2
        print(game.player.max_Hp_J2)
    else:
        pygame.draw.rect(display_surface, bar_losehp, [920, 20, 500, 50], 0, 25)
        pygame.draw.rect(display_surface, game.player.bar_vie_J2, game.player.bar_position_J2, 0, 25)
        pygame.draw.rect(display_surface, bar_border, [920, 20, 500, 50], 3, 25)

def choix_background_local(game,display_surface):
    if game.stage_select == 1:
        display_surface.blit(game.image['isis_back'], (0, 0))
    if game.stage_select == 2:
        display_surface.blit(game.image['gunnar_back'], (0, 0))
    if game.stage_select == 3:
        display_surface.blit(game.image['bigband_back'], (0, 0))    
    if game.stage_select == 4:
        display_surface.blit(game.image['kitt_back'], (0, 0))
    if game.stage_select == 5:
        display_surface.blit(game.image['harry_back'], (0, 0))
    if game.stage_select == 6:
        display_surface.blit(game.image['lucie_back'], (0, 0))

def remplir_tableau(game, display_surface):
    RED = (125, 0, 0)
    BLUE = (0, 48, 170)
    GREEN = (0, 116, 19)
    YELLOW = (255, 135, 0) 
    sysfont = pygame.font.get_default_font()
    #print('system font :', sysfont)

    t0 = time.time()
    font = pygame.font.SysFont("palatinolinotype", 48, bold=True, italic=False)
    #print('time needed for Font creation :', time.time() - t0)

    font1 = pygame.font.SysFont('palatinolinotype', 35)

    if len(game.prop) != 12:
        v = randint(0,len(game.sujets) - 1)
        w = randint(0,len(game.verbes) - 1)
        game.prop.append(game.sujets[v])
        game.sujets.pop(v)
        game.prop.append(game.verbes[w])
        game.verbes.pop(w)
        if len(game.prop) != 12 :
            x = randint(0, len(game.complement) - 1)
            y = randint(0, len(game.liaison) - 1)
            z = randint(0, len(game.final) - 1)
            game.prop.append(game.complement[x])
            game.complement.pop(x)
            game.prop.append(game.liaison[y])
            game.liaison.pop(y)
            game.prop.append(game.final[z])
            game.final.pop(z)

    img1 = font1.render(game.prop[0], True, RED)
    img2 = font1.render(game.prop[1], True, BLUE)
    img3 = font1.render(game.prop[2], True, GREEN)
    img4 = font1.render(game.prop[3], True, YELLOW)
    img5 = font1.render(game.prop[4], True, GREEN)

    display_surface.blit(img1, (555, 330))
    display_surface.blit(img2, (555, 380))
    display_surface.blit(img3, (555, 430))
    display_surface.blit(img4, (555, 480))
    display_surface.blit(img5, (555, 530))
    if len(game.prop) > 5 :
        img6 = font1.render(game.prop[5], True, RED)
        img7 = font1.render(game.prop[6], True, BLUE)
        img8 = font1.render(game.prop[7], True, GREEN)
        img9 = font1.render(game.prop[8], True, YELLOW)
        img10 = font1.render(game.prop[9], True, GREEN)
        display_surface.blit(img6, (555, 580))
        display_surface.blit(img7, (555, 630))
        display_surface.blit(img8, (555, 680))
        display_surface.blit(img9, (555, 730))
        display_surface.blit(img10, (555, 780))
    if len(game.prop) > 10 :
        img11 = font1.render(game.prop[10], True, RED)
        img12 = font1.render(game.prop[11], True, BLUE)
        display_surface.blit(img11, (555, 830))
        display_surface.blit(img12, (555, 880))

def tableau_prop(game, display_surface):
    tableau_prop = (212,212,212)
    tableau_position = [545, 324, 350, 650]
    pygame.draw.rect(display_surface, tableau_prop, tableau_position)
    pygame.draw.rect(display_surface, (0,0,0), tableau_position, 3)

    line_couleur = (0,0,0)
    line_position_start = [545, 374]
    line_position_end = [895, 374]
    line_position_start_vert = [720, 973]
    line_position_end_vert = [720, 923]
    pygame.draw.line(display_surface,line_couleur,line_position_start_vert,line_position_end_vert,3)

    for i in range(1,13):
        pygame.draw.line(display_surface,line_couleur,line_position_start,line_position_end,3)
        line_position_start[1] += 50
        line_position_end[1] += 50
    remplir_tableau(game, display_surface)

def in_game(game,display_surface):
    choix_background_local(game,display_surface)
    tableau_prop(game, display_surface)
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

    display_surface.blit(game.image['nuage_J1'], (20,87))
    display_surface.blit(game.image['nuage_J2'], (767,87))   

    barre_de_vie(game,display_surface)
   

    # Effet fond noir transparent
    if game.alpha != 0:
        fond_noir_surface = pygame.Surface((1440, 1024))
        fond_noir_surface.set_alpha(game.alpha)
        fond_noir_surface.fill((0, 0, 0))
        display_surface.blit(fond_noir_surface, (0, 0))
        game.alpha = game.alpha - 5



