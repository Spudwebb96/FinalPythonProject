import pygame
pygame.init()

class player:
    def __init__(self,role,name):
        self.hp = 3
        # Attribution de le personnage choisi par le joueur de self.image1 et
        self.image_one = False

        if role == "P1":
            self.phrase1 = []

            if name == "Bigband":
                weakness = "yomamajokes"
                #image ?
            
            if name == "Gunnar":
                weakness = "yomamajokes"

            if name == "Harry":
                weakness = "yodaddyjokes"

            if name == "K.I.T.T":
                weakness = "yomamajokes"

            if name == "Lucie":
                weakness = "yomamajokes"
        
            if name == "Isis":
                weakness = "yomamajokes"

        if role == "P2":
            self.phrase2 = []

            if name == "Bigband":
                weakness = "yomamajokes"
            
            if name == "Gunnar":
                weakness = "yomamajokes"

            if name == "Harry":
                weakness = "yodaddyjokes"

            if name == "K.I.T.T":
                weakness = "yomamajokes"

            if name == "Lucie":
                weakness = "yomamajokes"
        
            if name == "Isis":
                weakness = "yomamajokes"


        if self.image != False:
            self.image_one_load = pygame.image.load(self.image)

    
    # self.weakness = self.listweakness

