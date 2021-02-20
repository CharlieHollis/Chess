import pygame

class pieces(object):

    def __init__(self, imagePath, posx, posy, colour, value, name):
        self.imagePath = imagePath
        self.img = pygame.image.load(imagePath)
        self.posx, self.posy = posx, posy
        self.colour = colour.lower()
        self.value = value
        self.name = name.lower()

        self.arrayPosx, self.arrayPosy = self.findArray()

        self.moveablePlaces


    
    def findArray(self):
        return int((self.posx-100)/100), int((self.posy-100)/100)

    def setAlpha(self, imgPath):
        self.img = pygame.image.load(imgPath).convert()
        self.img.set_alpha(128)

    def returnAlpha(self, imgPath):
        self.img = pygame.image.load(imgPath)

    def moveablePlaces(self):
        if self.name == "blank":
            return []
        
        # TODO:: Write the moveable places algorithm

        if self.value == 0:
            if self.name == "whitepawn":
                return [(int((self.posx - 100) / 100), int((self.posy - 200) / 100)),
                        (int((self.posx - 100) / 100), int((self.posy - 300) / 100))]

            if self.name == "whiteknight":
                return [(int((self.posx - 200) / 100), int((self.posy - 300) / 100)),
                        (int((self.posx + 0) / 100), int((self.posy - 300) / 100)),
                        (int((self.posx + 100) / 100), int((self.posy - 200) / 100)),
                        (int((self.posx + 100) / 100), int((self.posy + 0  ) / 100)),
                        (int((self.posx + 0  ) / 100), int((self.posy + 100) / 100)),
                        (int((self.posx - 200) / 100), int((self.posy + 100) / 100)),
                        (int((self.posx - 300) / 100), int((self.posy + 0  ) / 100)),
                        (int((self.posx - 300) / 100), int((self.posy - 200) / 100))]
                          
            if self.name == "whiterook":
                return [(int((self.posx - 200) / 100), int((self.posy - 100) / 100)),
                        (int((self.posx - 300) / 100), int((self.posy - 100) / 100)),
                        (int((self.posx - 400) / 100), int((self.posy - 100) / 100)),
                        (int((self.posx - 500) / 100), int((self.posy - 100) / 100)),
                        (int((self.posx - 600) / 100), int((self.posy - 100) / 100)),
                        (int((self.posx - 700) / 100), int((self.posy - 100) / 100)),
                        (int((self.posx - 800) / 100), int((self.posy - 100) / 100)),

                        (int((self.posx + 0  ) / 100), int((self.posy - 100) / 100)),
                        (int((self.posx + 100) / 100), int((self.posy - 100) / 100)),
                        (int((self.posx + 200) / 100), int((self.posy - 100) / 100)),
                        (int((self.posx + 300) / 100), int((self.posy - 100) / 100)),
                        (int((self.posx + 400) / 100), int((self.posy - 100) / 100)),
                        (int((self.posx + 500) / 100), int((self.posy - 100) / 100)),
                        (int((self.posx + 600) / 100), int((self.posy - 100) / 100)),

                        (int((self.posx - 100) / 100), int((self.posy - 200) / 100)),
                        (int((self.posx - 100) / 100), int((self.posy - 300) / 100)),
                        (int((self.posx - 100) / 100), int((self.posy - 400) / 100)),
                        (int((self.posx - 100) / 100), int((self.posy - 500) / 100)),
                        (int((self.posx - 100) / 100), int((self.posy - 600) / 100)),
                        (int((self.posx - 100) / 100), int((self.posy - 700) / 100)),
                        (int((self.posx - 100) / 100), int((self.posy - 800) / 100)),

                        (int((self.posx - 100) / 100), int((self.posy + 0  ) / 100)),
                        (int((self.posx - 100) / 100), int((self.posy + 100) / 100)),
                        (int((self.posx - 100) / 100), int((self.posy + 200) / 100)),
                        (int((self.posx - 100) / 100), int((self.posy + 300) / 100)),
                        (int((self.posx - 100) / 100), int((self.posy + 400) / 100)),
                        (int((self.posx - 100) / 100), int((self.posy + 500) / 100)),
                        (int((self.posx - 100) / 100), int((self.posy + 600) / 100))]


            if self.name == "whitebishop":
                return [(int((self.posx - 200) / 100), int((self.posy - 200) / 100)),
                        (int((self.posx - 300) / 100), int((self.posy - 300) / 100)),
                        (int((self.posx - 400) / 100), int((self.posy - 400) / 100)),
                        (int((self.posx - 500) / 100), int((self.posy - 500) / 100)),
                        (int((self.posx - 600) / 100), int((self.posy - 600) / 100)),
                        (int((self.posx - 700) / 100), int((self.posy - 700) / 100)),
                        (int((self.posx - 800) / 100), int((self.posy - 800) / 100)),
                        
                        (int((self.posx + 0  ) / 100), int((self.posy - 200) / 100)),
                        (int((self.posx + 100) / 100), int((self.posy - 300) / 100)),
                        (int((self.posx + 200) / 100), int((self.posy - 400) / 100)),
                        (int((self.posx + 300) / 100), int((self.posy - 500) / 100)),
                        (int((self.posx + 400) / 100), int((self.posy - 600) / 100)),
                        (int((self.posx + 500) / 100), int((self.posy - 700) / 100)),
                        (int((self.posx + 600) / 100), int((self.posy - 800) / 100)),
                        
                        (int((self.posx + 0  ) / 100), int((self.posy + 0  ) / 100)),
                        (int((self.posx + 100) / 100), int((self.posy + 100) / 100)),
                        (int((self.posx + 200) / 100), int((self.posy + 200) / 100)),
                        (int((self.posx + 300) / 100), int((self.posy + 300) / 100)),
                        (int((self.posx + 400) / 100), int((self.posy + 400) / 100)),
                        (int((self.posx + 500) / 100), int((self.posy + 500) / 100)),
                        (int((self.posx + 600) / 100), int((self.posy + 600) / 100)),
                        
                        (int((self.posx - 200) / 100), int((self.posy + 0  ) / 100)),
                        (int((self.posx - 300) / 100), int((self.posy + 100) / 100)),
                        (int((self.posx - 400) / 100), int((self.posy + 200) / 100)),
                        (int((self.posx - 500) / 100), int((self.posy + 300) / 100)),
                        (int((self.posx - 600) / 100), int((self.posy + 400) / 100)),
                        (int((self.posx - 700) / 100), int((self.posy + 500) / 100)),
                        (int((self.posx - 800) / 100), int((self.posy + 600) / 100))]
