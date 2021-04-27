import pygame
import class_game
from fonctions import *
from class_game import *
pygame.init()

p1 = player("P1")
P2 = player("P2")

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

            





    
        