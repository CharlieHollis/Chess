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

    def moveablePlaces(self, piecesArray):
        if self.name == "blank":
            return []
        
        self.moveable = []
        self.oppPos = 0

        if self.value == 0:
            if self.name == "whitepawn":
                self.possiblePlaces = [(int((self.posx - 100) / 100), int((self.posy - 200) / 100)),
                                      (int((self.posx - 100) / 100), int((self.posy - 300) / 100))]
                
                for i in self.possiblePlaces:
                    if piecesArray[i[1]][i[0]].value == self.value or self.oppPos == 1:
                        break
                    elif int(piecesArray[i[1]][i[0]].value) == 1 and self.oppPos == 0:
                        self.oppPos = 1
                        self.moveable.append(i)
                    else:
                        self.moveable.append(i)
                return self.moveable
            
            if self.name == "whiteknight":
                return [(int((self.posx - 200) / 100), int((self.posy - 300) / 100)),
                        (int((self.posx + 0  ) / 100), int((self.posy - 300) / 100)),
                        (int((self.posx + 100) / 100), int((self.posy - 200) / 100)),
                        (int((self.posx + 100) / 100), int((self.posy + 0  ) / 100)),
                        (int((self.posx + 0  ) / 100), int((self.posy + 100) / 100)),
                        (int((self.posx - 200) / 100), int((self.posy + 100) / 100)),
                        (int((self.posx - 300) / 100), int((self.posy + 0  ) / 100)),
                        (int((self.posx - 300) / 100), int((self.posy - 200) / 100))]
            
            if self.name == "whiterook":
                self.possiblePlaces = [[(int((self.posx - 200) / 100), int((self.posy - 100) / 100)),
                                        (int((self.posx - 300) / 100), int((self.posy - 100) / 100)),
                                        (int((self.posx - 400) / 100), int((self.posy - 100) / 100)),
                                        (int((self.posx - 500) / 100), int((self.posy - 100) / 100)),
                                        (int((self.posx - 600) / 100), int((self.posy - 100) / 100)),
                                        (int((self.posx - 700) / 100), int((self.posy - 100) / 100)),
                                        (int((self.posx - 800) / 100), int((self.posy - 100) / 100))],

                                        [(int((self.posx + 0  ) / 100), int((self.posy - 100) / 100)),
                                        (int((self.posx + 100) / 100), int((self.posy - 100) / 100)),
                                        (int((self.posx + 200) / 100), int((self.posy - 100) / 100)),
                                        (int((self.posx + 300) / 100), int((self.posy - 100) / 100)),
                                        (int((self.posx + 400) / 100), int((self.posy - 100) / 100)),
                                        (int((self.posx + 500) / 100), int((self.posy - 100) / 100)),
                                        (int((self.posx + 600) / 100), int((self.posy - 100) / 100))],
                                        
                                        [(int((self.posx - 100) / 100), int((self.posy - 200) / 100)),
                                        (int((self.posx - 100) / 100), int((self.posy - 300) / 100)),
                                        (int((self.posx - 100) / 100), int((self.posy - 400) / 100)),
                                        (int((self.posx - 100) / 100), int((self.posy - 500) / 100)),
                                        (int((self.posx - 100) / 100), int((self.posy - 600) / 100)),
                                        (int((self.posx - 100) / 100), int((self.posy - 700) / 100)),
                                        (int((self.posx - 100) / 100), int((self.posy - 800) / 100))],
                                        
                                        [(int((self.posx - 100) / 100), int((self.posy + 0  ) / 100)),
                                        (int((self.posx - 100) / 100), int((self.posy + 100) / 100)),
                                        (int((self.posx - 100) / 100), int((self.posy + 200) / 100)),
                                        (int((self.posx - 100) / 100), int((self.posy + 300) / 100)),
                                        (int((self.posx - 100) / 100), int((self.posy + 400) / 100)),
                                        (int((self.posx - 100) / 100), int((self.posy + 500) / 100)),
                                        (int((self.posx - 100) / 100), int((self.posy + 600) / 100))]]

                for i in range(len(self.possiblePlaces)):
                    for j in self.possiblePlaces[i]:
                        if j[0] >= 8 or j[1] >= 8:
                            break
                        elif j[0] <= -1 or j[1] <= -1:
                            break
                        if piecesArray[j[1]][j[0]].value == self.value or self.oppPos ==1:
                            break
                        elif int(piecesArray[j[1]][j[0]].value) == 1 and self.oppPos == 0:
                            self.oppPos = 1
                            self.moveable.append(j)
                        else:
                            self.moveable.append(j)
                    self.oppPos = 0
                
                return self.moveable

            if self.name == "whitebishop":
                self.possiblePlaces = [[(int((self.posx - 200) / 100), int((self.posy - 200) / 100)),
                                        (int((self.posx - 300) / 100), int((self.posy - 300) / 100)),
                                        (int((self.posx - 400) / 100), int((self.posy - 400) / 100)),
                                        (int((self.posx - 500) / 100), int((self.posy - 500) / 100)),
                                        (int((self.posx - 600) / 100), int((self.posy - 600) / 100)),
                                        (int((self.posx - 700) / 100), int((self.posy - 700) / 100)),
                                        (int((self.posx - 800) / 100), int((self.posy - 800) / 100))],

                                        [(int((self.posx + 0  ) / 100), int((self.posy - 200) / 100)),
                                        (int((self.posx + 100) / 100), int((self.posy - 300) / 100)),
                                        (int((self.posx + 200) / 100), int((self.posy - 400) / 100)),
                                        (int((self.posx + 300) / 100), int((self.posy - 500) / 100)),
                                        (int((self.posx + 400) / 100), int((self.posy - 600) / 100)),
                                        (int((self.posx + 500) / 100), int((self.posy - 700) / 100)),
                                        (int((self.posx + 600) / 100), int((self.posy - 800) / 100))],
                                        
                                        [(int((self.posx + 0  ) / 100), int((self.posy + 0  ) / 100)),
                                        (int((self.posx + 100) / 100), int((self.posy + 100) / 100)),
                                        (int((self.posx + 200) / 100), int((self.posy + 200) / 100)),
                                        (int((self.posx + 300) / 100), int((self.posy + 300) / 100)),
                                        (int((self.posx + 400) / 100), int((self.posy + 400) / 100)),
                                        (int((self.posx + 500) / 100), int((self.posy + 500) / 100)),
                                        (int((self.posx + 600) / 100), int((self.posy + 600) / 100))],
                                        
                                        [(int((self.posx - 200) / 100), int((self.posy + 0  ) / 100)),
                                        (int((self.posx - 300) / 100), int((self.posy + 100) / 100)),
                                        (int((self.posx - 400) / 100), int((self.posy + 200) / 100)),
                                        (int((self.posx - 500) / 100), int((self.posy + 300) / 100)),
                                        (int((self.posx - 600) / 100), int((self.posy + 400) / 100)),
                                        (int((self.posx - 700) / 100), int((self.posy + 500) / 100)),
                                        (int((self.posx - 800) / 100), int((self.posy + 600) / 100))]]


                for i in range(len(self.possiblePlaces)):
                    for j in self.possiblePlaces[i]:
                        if j[0] >= 8 or j[1] >= 8:
                            break
                        elif j[0] <= -1 or j[1] <= -1:
                            break
                        elif piecesArray[j[1]][j[0]].value == self.value or self.oppPos ==1:
                            break
                        elif int(piecesArray[j[1]][j[0]].value) == 1 and self.oppPos == 0:
                            self.oppPos = 1
                            self.moveable.append(j)
                        else:
                            self.moveable.append(j)
                    self.oppPos = 0
                

                return self.moveable

            if self.name == "whitequeen":
                self.possiblePlaces = [[(int((self.posx - 200) / 100), int((self.posy - 200) / 100)),
                                        (int((self.posx - 300) / 100), int((self.posy - 300) / 100)),
                                        (int((self.posx - 400) / 100), int((self.posy - 400) / 100)),
                                        (int((self.posx - 500) / 100), int((self.posy - 500) / 100)),
                                        (int((self.posx - 600) / 100), int((self.posy - 600) / 100)),
                                        (int((self.posx - 700) / 100), int((self.posy - 700) / 100)),
                                        (int((self.posx - 800) / 100), int((self.posy - 800) / 100))],

                                        [(int((self.posx + 0  ) / 100), int((self.posy - 200) / 100)),
                                        (int((self.posx + 100) / 100), int((self.posy - 300) / 100)),
                                        (int((self.posx + 200) / 100), int((self.posy - 400) / 100)),
                                        (int((self.posx + 300) / 100), int((self.posy - 500) / 100)),
                                        (int((self.posx + 400) / 100), int((self.posy - 600) / 100)),
                                        (int((self.posx + 500) / 100), int((self.posy - 700) / 100)),
                                        (int((self.posx + 600) / 100), int((self.posy - 800) / 100))],
                                        
                                        [(int((self.posx + 0  ) / 100), int((self.posy + 0  ) / 100)),
                                        (int((self.posx + 100) / 100), int((self.posy + 100) / 100)),
                                        (int((self.posx + 200) / 100), int((self.posy + 200) / 100)),
                                        (int((self.posx + 300) / 100), int((self.posy + 300) / 100)),
                                        (int((self.posx + 400) / 100), int((self.posy + 400) / 100)),
                                        (int((self.posx + 500) / 100), int((self.posy + 500) / 100)),
                                        (int((self.posx + 600) / 100), int((self.posy + 600) / 100))],
                                        
                                        [(int((self.posx - 200) / 100), int((self.posy + 0  ) / 100)),
                                        (int((self.posx - 300) / 100), int((self.posy + 100) / 100)),
                                        (int((self.posx - 400) / 100), int((self.posy + 200) / 100)),
                                        (int((self.posx - 500) / 100), int((self.posy + 300) / 100)),
                                        (int((self.posx - 600) / 100), int((self.posy + 400) / 100)),
                                        (int((self.posx - 700) / 100), int((self.posy + 500) / 100)),
                                        (int((self.posx - 800) / 100), int((self.posy + 600) / 100))],
                                        
                                        [(int((self.posx - 200) / 100), int((self.posy - 100) / 100)),
                                        (int((self.posx - 300) / 100), int((self.posy - 100) / 100)),
                                        (int((self.posx - 400) / 100), int((self.posy - 100) / 100)),
                                        (int((self.posx - 500) / 100), int((self.posy - 100) / 100)),
                                        (int((self.posx - 600) / 100), int((self.posy - 100) / 100)),
                                        (int((self.posx - 700) / 100), int((self.posy - 100) / 100)),
                                        (int((self.posx - 800) / 100), int((self.posy - 100) / 100))],

                                        [(int((self.posx + 0  ) / 100), int((self.posy - 100) / 100)),
                                        (int((self.posx + 100) / 100), int((self.posy - 100) / 100)),
                                        (int((self.posx + 200) / 100), int((self.posy - 100) / 100)),
                                        (int((self.posx + 300) / 100), int((self.posy - 100) / 100)),
                                        (int((self.posx + 400) / 100), int((self.posy - 100) / 100)),
                                        (int((self.posx + 500) / 100), int((self.posy - 100) / 100)),
                                        (int((self.posx + 600) / 100), int((self.posy - 100) / 100))],
                                        
                                        [(int((self.posx - 100) / 100), int((self.posy - 200) / 100)),
                                        (int((self.posx - 100) / 100), int((self.posy - 300) / 100)),
                                        (int((self.posx - 100) / 100), int((self.posy - 400) / 100)),
                                        (int((self.posx - 100) / 100), int((self.posy - 500) / 100)),
                                        (int((self.posx - 100) / 100), int((self.posy - 600) / 100)),
                                        (int((self.posx - 100) / 100), int((self.posy - 700) / 100)),
                                        (int((self.posx - 100) / 100), int((self.posy - 800) / 100))],
                                        
                                        [(int((self.posx - 100) / 100), int((self.posy + 0  ) / 100)),
                                        (int((self.posx - 100) / 100), int((self.posy + 100) / 100)),
                                        (int((self.posx - 100) / 100), int((self.posy + 200) / 100)),
                                        (int((self.posx - 100) / 100), int((self.posy + 300) / 100)),
                                        (int((self.posx - 100) / 100), int((self.posy + 400) / 100)),
                                        (int((self.posx - 100) / 100), int((self.posy + 500) / 100)),
                                        (int((self.posx - 100) / 100), int((self.posy + 600) / 100))]]
 
                for i in range(len(self.possiblePlaces)):
                    for j in self.possiblePlaces[i]:
                        if j[0] >= 8 or j[1] >= 8:
                            break
                        elif j[0] <= -1 or j[1] <= -1:
                            break
                        if piecesArray[j[1]][j[0]].value == self.value or self.oppPos ==1:
                            break
                        elif int(piecesArray[j[1]][j[0]].value) == 1 and self.oppPos == 0:
                            self.oppPos = 1
                            self.moveable.append(j)
                        else:
                            self.moveable.append(j)
                    self.oppPos = 0
                
                return self.moveable