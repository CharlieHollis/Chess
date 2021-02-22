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
                
                self.pawntakes = [(int((self.posx - 200) / 100), int((self.posy - 200) / 100)),                             
                                  (int((self.posx - 0  ) / 100), int((self.posy - 200) / 100))]

                for i in self.possiblePlaces:
                    if i[1] <= -1 or int(piecesArray[i[1]][i[0]].value) == 1:                       # TODO:: Values
                        break
                    else:
                        self.moveable.append(i)
                
                
                for i in self.pawntakes:
                    if i[1] <= -1:                                                              
                        pass
                    elif i[0] >= 8 or i[0] <= -1:                                                                 
                        pass    
                    elif int(piecesArray[i[1]][i[0]].value) != 1:                               
                        pass
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
            
            if self.name == "whiteking":                                            
                self.possiblePlaces = [(int((self.posx - 200) / 100), int((self.posy - 200) / 100)),
                                       (int((self.posx - 100) / 100), int((self.posy - 200) / 100)),
                                       (int((self.posx - 0  ) / 100), int((self.posy - 200) / 100)),
                                       (int((self.posx - 0  ) / 100), int((self.posy - 100) / 100)),
                                       (int((self.posx - 0  ) / 100), int((self.posy - 0  ) / 100)),
                                       (int((self.posx - 100) / 100), int((self.posy - 0  ) / 100)),
                                       (int((self.posx - 200) / 100), int((self.posy - 0  ) / 100)),
                                       (int((self.posx - 200) / 100), int((self.posy - 100) / 100))]

                for i in self.possiblePlaces:
                    if (i[0] >= 8 or i[1] >= 8) or (i[0] <= -1 or i[1] <= -1):
                        pass
                    elif piecesArray[i[1]][i[0]].value == self.value:
                        pass
                    else:
                        self.moveable.append(i)
                return self.moveable



        if self.value == 1:
            if self.name == "blackpawn":                                            
                self.possiblePlaces = [(int((self.posx - 100) / 100), int((self.posy + 0  ) / 100)),                        
                                       (int((self.posx - 100) / 100), int((self.posy + 100) / 100))]
                
                self.pawntakes = [(int((self.posx - 200) / 100), int((self.posy - 0  ) / 100)),                             
                                  (int((self.posx - 0  ) / 100), int((self.posy - 0  ) / 100))]

                for i in self.possiblePlaces:
                    if i[1] <= -1 or int(piecesArray[i[1]][i[0]].value) == 0:                       
                        break
                    else:
                        self.moveable.append(i)
                
                for i in self.pawntakes:
                    if i[1] >= 8:                                                              
                        pass
                    elif i[0] >= 8 or i[0] <= -1:                                                                 
                        pass    
                    elif int(piecesArray[i[1]][i[0]].value) != 0:                               
                        pass
                    else:
                        self.moveable.append(i)

                return self.moveable
            


            if self.name == "blackknight":                                                  
                return [(int((self.posx - 200) / 100), int((self.posy - 300) / 100)),
                        (int((self.posx + 0  ) / 100), int((self.posy - 300) / 100)),
                        (int((self.posx + 100) / 100), int((self.posy - 200) / 100)),
                        (int((self.posx + 100) / 100), int((self.posy + 0  ) / 100)),
                        (int((self.posx + 0  ) / 100), int((self.posy + 100) / 100)),
                        (int((self.posx - 200) / 100), int((self.posy + 100) / 100)),
                        (int((self.posx - 300) / 100), int((self.posy + 0  ) / 100)),
                        (int((self.posx - 300) / 100), int((self.posy - 200) / 100))]
            
            if self.name == "blackrook":                                                    
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
                        elif int(piecesArray[j[1]][j[0]].value) == 0 and self.oppPos == 0:
                            self.oppPos = 1
                            self.moveable.append(j)
                        else:
                            self.moveable.append(j)
                    self.oppPos = 0
                
                return self.moveable

            if self.name == "blackbishop":                                              
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
                        elif int(piecesArray[j[1]][j[0]].value) == 0 and self.oppPos == 0:
                            self.oppPos = 1
                            self.moveable.append(j)
                        else:
                            self.moveable.append(j)
                    self.oppPos = 0
                

                return self.moveable

            if self.name == "blackqueen":                                           
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
                        elif int(piecesArray[j[1]][j[0]].value) == 0 and self.oppPos == 0:
                            self.oppPos = 1
                            self.moveable.append(j)
                        else:
                            self.moveable.append(j)
                    self.oppPos = 0
                
                return self.moveable
            
            if self.name == "blackking":                                            
                self.possiblePlaces = [(int((self.posx - 200) / 100), int((self.posy - 200) / 100)),
                                       (int((self.posx - 100) / 100), int((self.posy - 200) / 100)),
                                       (int((self.posx - 0  ) / 100), int((self.posy - 200) / 100)),
                                       (int((self.posx - 0  ) / 100), int((self.posy - 100) / 100)),
                                       (int((self.posx - 0  ) / 100), int((self.posy - 0  ) / 100)),
                                       (int((self.posx - 100) / 100), int((self.posy - 0  ) / 100)),
                                       (int((self.posx - 200) / 100), int((self.posy - 0  ) / 100)),
                                       (int((self.posx - 200) / 100), int((self.posy - 100) / 100))]

                for i in self.possiblePlaces:
                    if (i[0] >= 8 or i[1] >= 8) or (i[0] <= -1 or i[1] <= -1):
                        pass
                    elif piecesArray[i[1]][i[0]].value == self.value:
                        pass
                    else:
                        self.moveable.append(i)
                return self.moveable


        