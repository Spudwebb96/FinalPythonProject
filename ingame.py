import pygame
import class_game
from fonctions import *
from class_game import *
pygame.init()

p1 = player("P1")
P2 = player("P2")

self.sujetsref = [ 1, 2, 3, 4 ,5 ,6 ,7 ,8 ,9]
self.sujets = [ 1, 2, 3, 4 ,5 ,6 ,7 ,8 ,9]
self.verbesref = [ "a", "b", "c", "d" ,"e" ,"f" ,"g" ,"h" ,"i"]
self.verbes = [ "a", "b", "c", "d" ,"e" ,"f" ,"g" ,"h" ,"i"]
self.complementref = [ 10, 11, 12, 13 ,14 ,15 ,16 ,17 ,18]
self.complement = [ 10, 11, 12, 13 ,14 ,15 ,16 ,17 ,18]

x = randint(0,8)

self.prop.append(self.sujets[x])
self.prop.pop[x]

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





    
        