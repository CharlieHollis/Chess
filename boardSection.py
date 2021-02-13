import pygame

class board(object):

    def __init__(self, imagePath, posx, posy, value):

        self.colour = pygame.image.load(imagePath)
        self.posx = posx
        self.posy = posy
        self.value = value
        self.sizex, self.sizey = 100, 100

        self.arrayPosx, self.arrayPosy = self.findArray()
        

    def findArray(self):
        return int((self.posx-100)/100), int((self.posy-46)/100)

