import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame


import boardSection as bs 
import pieces as pc

pygame.init()
font = pygame.font.Font("CascadiaCode_VTT.ttf", 75)

height, width = 1000,1000
display = pygame.display.set_mode((width,height))

darkSquare = (118,150,86)
white = (255,255,255)
selected = (186,202,43)

boardBg = []
boardPc = []
circleImgArray = []

for i in range(8):                      # Creates the board pieces object array
    boardPc.append([])
    for j in range(8):
        if i == 0 :
            if j == 0 or j == 7:
                boardPc[i].append(pc.pieces(os.path.join("imgs","BlackRook.png"), 100+j*100, 100+i*100, "BlackRook", 1, "BlackRook"))
            elif j == 1 or j == 6:
                boardPc[i].append(pc.pieces(os.path.join("imgs","BlackKnight.png"), 100+j*100, 100+i*100, "BlackKnight", 1, "BlackKnight"))
            elif j == 2 or j == 5:
                boardPc[i].append(pc.pieces(os.path.join("imgs","BlackBishop.png"), 100+j*100, 100+i*100, "BlackBishop", 1, "BlackBishop"))
            elif j == 3:
                boardPc[i].append(pc.pieces(os.path.join("imgs","BlackQueen.png"), 100+j*100, 100+i*100, "BlackQueen", 1, "BlackQueen"))
            elif j == 4:
                boardPc[i].append(pc.pieces(os.path.join("imgs","BlackKing.png"), 100+j*100, 100+i*100, "BlackKing", 1, "BlackKing"))
        elif i == 1:
            boardPc[i].append(pc.pieces(os.path.join("imgs","BlackPawn.png"), 100+j*100, 100+i*100, "BlackPawn", 1, "BlackPawn"))
        
        elif i == 7 :
            if j == 0 or j == 7:
                boardPc[i].append(pc.pieces(os.path.join("imgs","WhiteRook.png"), 100+j*100, 100+i*100, "WhiteRook", 0, "WhiteRook"))
            elif j == 1 or j == 6:
                boardPc[i].append(pc.pieces(os.path.join("imgs","WhiteKnight.png"), 100+j*100, 100+i*100, "WhiteKnight", 0, "WhiteKnight"))
            elif j == 2 or j == 5:
                boardPc[i].append(pc.pieces(os.path.join("imgs","WhiteBishop.png"), 100+j*100, 100+i*100, "WhiteBishop", 0, "WhiteBishop"))
            elif j == 3:
                boardPc[i].append(pc.pieces(os.path.join("imgs","WhiteQueen.png"), 100+j*100, 100+i*100, "BlacWhiteQueenkQueen", 0, "WhiteQueen"))
            elif j == 4:
                boardPc[i].append(pc.pieces(os.path.join("imgs","WhiteKing.png"), 100+j*100, 100+i*100, "WhiteKing", 0, "WhiteKing"))
        elif i == 6:
            boardPc[i].append(pc.pieces(os.path.join("imgs","WhitePawn.png"), 100+j*100, 100+i*100, "WhitePawn", 0, "WhitePawn"))
        else:
             boardPc[i].append(pc.pieces(os.path.join("imgs","blank.png"), 100+j*100, 100+i*100, "blank", -1, "blank"))           

for i in range(8):                      # Creates the board sections object array
    boardBg.append([])
    for j in range(8):
        if ((i+1)+(j+1)) % 2 == 0:
            boardBg[i].append(bs.board(os.path.join("imgs","lightSquare.png"), 100+j*100, 100+i*100, i+j))
        else: boardBg[i].append(bs.board(os.path.join("imgs","darkSquare.png"), 100+j*100, 100+i*100, i+j))

wood = pygame.image.load(os.path.join("imgs","wood.jpg"))           # Bg img
selectedPath = os.path.join("imgs", "selected.png")                 # Selected img path



for i in range(8):
    circleImgArray.append([])
    for j in range(8):
        circleImgArray[i].append(bs.board(os.path.join("imgs", "circle.png"), 100+j*100, 100+i*100, i+j))

for i in range(8):
    for j in range(8):
        circleImgArray[i][j].colour.set_alpha(0)


clock = pygame.time.Clock()                             # Creates a clock variable to lock the fps

clicked = False
finding = True
turn = 0
findingPos = (0,0)
running = True

while running:                                              # Main Game Loop
    for event in pygame.event.get():                        # Loop that checks for events
        if event.type == pygame.QUIT:                       # Checks if the quit button has been pressed
            running = False


        if event.type == pygame.KEYDOWN:                    # Gets all key down events
            if event.key == pygame.K_ESCAPE and not finding:
                for i in range(len(boardPc)):
                    for j in range(len(boardPc[i])):
                        if boardPc[i][j].name == "blank":
                            boardPc[i][j].returnAlpha(os.path.join("imgs","blank.png"))
                for i in range(len(circleImgArray)):
                                for j in range(len(circleImgArray[i])):
                                    circleImgArray[i][j].colour.set_alpha(0)
                finding = True                


        if event.type == pygame.MOUSEBUTTONDOWN:            # Gets all mouse button down events
            mousePressedPos = pygame.mouse.get_pos()
            if mousePressedPos[0] > 99 and mousePressedPos[0] < 901 and not clicked:
                if  mousePressedPos[1] > 99 and mousePressedPos[1] < 901:
                    pressx = mousePressedPos[0]; pressy = mousePressedPos[1]
                    posx = (pressx - 100) / 100; posy = (pressy - 100) / 100
                    if finding:
                        if boardPc[int(posy)][int(posx)].name != "blank" and turn % 2 == 0 and boardPc[int(posy)][int(posx)].value == 0:
                            findingName = boardPc[int(posy)][int(posx)].name
                            MoveablePlaces = boardPc[int(posy)][int(posx)].moveablePlaces(boardPc)
                            for i in range(len(MoveablePlaces)):
                                movPosx = MoveablePlaces[i][0]
                                movPosy = MoveablePlaces[i][1]
                                if movPosx >= 8 or movPosy >= 8:
                                    pass
                                elif movPosx <= -1 or movPosy <= -1:
                                    pass
                                else:
                                    if boardPc[movPosy][movPosx].name == "blank":
                                        boardPc[movPosy][movPosx].setAlpha(selectedPath)  
                            for i in MoveablePlaces:
                                if i[0] >= 8 or i[1] >= 8:
                                    pass
                                elif i[0] <= -1 or i[1] <= -1:
                                    pass
                                elif boardPc[i[1]][i[0]].value == 1:
                                    circleImgArray[i[1]][i[0]].colour.set_alpha(192)
                                
                            findingPos = (int(posx),int(posy))
                            finding = False
                        
                        if boardPc[int(posy)][int(posx)].name != "blank" and turn % 2 == 1 and boardPc[int(posy)][int(posx)].value == 1:
                            findingName = boardPc[int(posy)][int(posx)].name
                            MoveablePlaces = boardPc[int(posy)][int(posx)].moveablePlaces(boardPc)
                            for i in range(len(MoveablePlaces)):
                                movPosx = MoveablePlaces[i][0]
                                movPosy = MoveablePlaces[i][1]
                                if movPosx >= 8 or movPosy >= 8:
                                    pass
                                elif movPosx <= -1 or movPosy <= -1:
                                    pass
                                else:
                                    if boardPc[movPosy][movPosx].name == "blank":
                                        boardPc[movPosy][movPosx].setAlpha(selectedPath)  
                            for i in MoveablePlaces: 
                                if i[0] >= 8 or i[1] >= 8:
                                    pass
                                elif i[0] <= -1 or i[1] <= -1:
                                    pass
                                elif boardPc[i[1]][i[0]].value == 0:
                                    circleImgArray[i[1]][i[0]].colour.set_alpha(192)
                                
                            findingPos = (int(posx),int(posy))
                            finding = False

                        
                        

                    elif not finding:
                        if boardPc[int(posy)][int(posx)].value != boardPc[findingPos[1]][findingPos[0]].value and (int(posx),int(posy)) in MoveablePlaces:
                            # Moving Piece to Blank 
                            boardPc[int(posy)][int(posx)].returnAlpha(os.path.join("imgs","{}.png".format(boardPc[findingPos[1]][findingPos[0]].name)))
                            boardPc[int(posy)][int(posx)].name = boardPc[findingPos[1]][findingPos[0]].name 
                            boardPc[int(posy)][int(posx)].posx = (int(posx) * 100) + 100
                            boardPc[int(posy)][int(posx)].posy = (int(posy) * 100) + 100
                            boardPc[int(posy)][int(posx)].value = boardPc[findingPos[1]][findingPos[0]].value

                            # Moving Blank to Piece
                            boardPc[findingPos[1]][findingPos[0]].returnAlpha(os.path.join("imgs", "blank.png"))
                            boardPc[findingPos[1]][findingPos[0]].name = "blank" 
                            boardPc[findingPos[1]][findingPos[0]].posx = (int(findingPos[0]) * 100) + 100
                            boardPc[findingPos[1]][findingPos[0]].posy = (int(findingPos[1]) * 100) + 100
                            boardPc[findingPos[1]][findingPos[0]].value = -1
                            finding = True
                            for i in range(len(boardPc)):
                                for j in range(len(boardPc[i])):
                                    if boardPc[i][j].name == "blank":
                                        boardPc[i][j].returnAlpha(os.path.join("imgs","blank.png"))
                            for i in range(len(circleImgArray)):
                                for j in range(len(circleImgArray[i])):
                                    circleImgArray[i][j].colour.set_alpha(0)
                            turn += 1
        
    if turn % 2 == 0:
        text = font.render("Turn: Player 1", True, white)
    else: text = font.render("Turn: Player 2", True, white)

    check = False
    checkedArray = []
    kingPlaces = []

    display.blit(wood, (0,0)); display.blit(wood, (894,0)); display.blit(wood, (0,894)); display.blit(wood, (894,894))      # Creates Background

    for i in range(len(boardBg)):             # Creates Board
        for j in range(len(boardBg[i])):
            display.blit(boardBg[i][j].colour, (boardBg[i][j].posx, boardBg[i][j].posy))

    for i in range(len(boardPc)):             # Creates pieces on the board
        for j in range(len(boardPc[i])):
            display.blit(boardPc[i][j].img, (boardPc[i][j].posx, boardPc[i][j].posy))

    for i in range(len(circleImgArray)):
        for j in range(len(circleImgArray[i])):
            display.blit(circleImgArray[i][j].colour, (circleImgArray[i][j].posx, circleImgArray[i][j].posy))

    display.blit(text, (187,10))


    # TODO: Checkmate algorithm needs work done to it.

    # for i in range(len(boardPc)):
    #     for j in range(len(boardPc[i])):
    #         if boardPc[i][j].value == 0:
    #             for checkPlaces in boardPc[i][j].moveablePlaces(boardPc):
    #                 checkedArray.append(checkPlaces)
    #         if boardPc[i][j].name == "blackking":
    #             kingPlaces.append((boardPc[i][j].arrayPosx, boardPc[i][j].arrayPosy))
    #             for kingplaces in boardPc[i][j].moveablePlaces(boardPc):
    #                 kingPlaces.append(kingplaces)
    # emptyCheck = []
    # for kingplaces in kingPlaces:
    #     if kingplaces in checkedArray:
    #         emptyCheck.append(kingplaces)
    
    # if len(emptyCheck) == len(kingPlaces):
    #     wonText = font.render("Player 1 has won!!", True, white)
    #     display.blit(wonText, (100,488))
    

    # for i in range(len(boardPc)):
    #     for j in range(len(boardPc[i])):
    #         if boardPc[i][j].value == 1:
    #             for checkPlaces in boardPc[i][j].moveablePlaces(boardPc):
    #                 checkedArray.append(checkPlaces)
    #         if boardPc[i][j].name == "whiteking":
    #             kingPlaces.append((boardPc[i][j].arrayPosx, boardPc[i][j].arrayPosy))
    #             for kingplaces in boardPc[i][j].moveablePlaces(boardPc):
    #                 kingPlaces.append(kingplaces)
    # emptyCheck = []
    # for kingplaces in kingPlaces:
    #     if kingplaces in checkedArray:
    #         emptyCheck.append(kingplaces)
        
    # if len(emptyCheck) == len(kingPlaces):
    #     wonText = font.render("Player 2 has won!!", True, white)
    #     display.blit(wonText, (100,488))

    pygame.display.update()                   # Updates the creen (new frame)
    clock.tick(60)                            # Sets the fps to a locked 60 (change to 30 if you have integrated graphics)

pygame.quit()                                 # Closes the window and ends the program