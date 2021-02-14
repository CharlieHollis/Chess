import pygame
import os

import boardSection as bs 
import pieces as pc

pygame.init()

height, width = 1000,1000
display = pygame.display.set_mode((width,height))

darkSquare = (118,150,86)
white = (255,255,255)
selected = (186,202,43)

boardBg = []
boardPc = []

for i in range(8):
    boardPc.append([])
    for j in range(8):
        if i == 0 :
            if j == 0 or j == 7:
                boardPc[i].append(pc.pieces(os.path.join("imgs","BlackRook.png"), 100+j*100, 100+i*100, "BlackRook", i+j, "BlackRook"))
            elif j == 1 or j == 6:
                boardPc[i].append(pc.pieces(os.path.join("imgs","BlackKnight.png"), 100+j*100, 100+i*100, "BlackKnight", i+j, "BlackKnight"))
            elif j == 2 or j == 5:
                boardPc[i].append(pc.pieces(os.path.join("imgs","BlackBishop.png"), 100+j*100, 100+i*100, "BlackBishop", i+j, "BlackBishop"))
            elif j == 3:
                boardPc[i].append(pc.pieces(os.path.join("imgs","BlackQueen.png"), 100+j*100, 100+i*100, "BlackQueen", i+j, "BlackQueen"))
            elif j == 4:
                boardPc[i].append(pc.pieces(os.path.join("imgs","BlackKing.png"), 100+j*100, 100+i*100, "BlackKing", i+j, "BlackKing"))
        elif i == 1:
            boardPc[i].append(pc.pieces(os.path.join("imgs","BlackPawn.png"), 100+j*100, 100+i*100, "BlackPawn", i+j, "BlackPawn"))
        
        elif i == 7 :
            if j == 0 or j == 7:
                boardPc[i].append(pc.pieces(os.path.join("imgs","WhiteRook.png"), 100+j*100, 100+i*100, "WhiteRook", i+j, "WhiteRook"))
            elif j == 1 or j == 6:
                boardPc[i].append(pc.pieces(os.path.join("imgs","WhiteKnight.png"), 100+j*100, 100+i*100, "WhiteKnight", i+j, "WhiteKnight"))
            elif j == 2 or j == 5:
                boardPc[i].append(pc.pieces(os.path.join("imgs","WhiteBishop.png"), 100+j*100, 100+i*100, "WhiteBishop", i+j, "WhiteBishop"))
            elif j == 3:
                boardPc[i].append(pc.pieces(os.path.join("imgs","WhiteQueen.png"), 100+j*100, 100+i*100, "BlacWhiteQueenkQueen", i+j, "WhiteQueen"))
            elif j == 4:
                boardPc[i].append(pc.pieces(os.path.join("imgs","WhiteKing.png"), 100+j*100, 100+i*100, "WhiteKing", i+j, "WhiteKing"))
        elif i == 6:
            boardPc[i].append(pc.pieces(os.path.join("imgs","WhitePawn.png"), 100+j*100, 100+i*100, "WhitePawn", i+j, "WhitePawn"))
        else:
             boardPc[i].append(pc.pieces(os.path.join("imgs","blank.png"), 100+j*100, 100+i*100, "blank", i+j, "blank"))           

for i in range(8):
    boardBg.append([])
    for j in range(8):
        if ((i+1)+(j+1)) % 2 == 0:
            boardBg[i].append(bs.board(os.path.join("imgs","lightSquare.png"), 100+j*100, 100+i*100, i+j))
        else: boardBg[i].append(bs.board(os.path.join("imgs","darkSquare.png"), 100+j*100, 100+i*100, i+j))

wood = pygame.image.load(os.path.join("imgs","wood.jpg"))
selectedPath = os.path.join("imgs", "selected.png")


clock = pygame.time.Clock()

clicked = False
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mousePressedPos = pygame.mouse.get_pos()
            if mousePressedPos[0] > 99 and mousePressedPos[0] < 901 and not clicked:
                if  mousePressedPos[1] > 99 and mousePressedPos[1] < 901:
                    pressx = mousePressedPos[0]; pressy = mousePressedPos[1]
                    pressx = (pressx - 100) / 100; pressy = (pressy - 100) / 100
                    print(str(pressx)[0], str(pressy)[0])
                    clicked = True
            if clicked:
                for i in range(len(boardPc)):
                    for j in range(len(boardPc[i])):
                        if boardPc[i][j].name == "blank":
                            boardPc[i][j].changeColour(selectedPath)


    display.blit(wood, (0,0)); display.blit(wood, (894,0)); display.blit(wood, (0,894)); display.blit(wood, (894,894))      # Creates Background

    for i in range(len(boardBg)):             # Creates Board
        for j in range(len(boardBg[i])):
            display.blit(boardBg[i][j].colour, (boardBg[i][j].posx, boardBg[i][j].posy))

    for i in range(len(boardPc)):             # Creates pieces on the board
        for j in range(len(boardPc[i])):
            display.blit(boardPc[i][j].img, (boardPc[i][j].posx, boardPc[i][j].posy))

    # TODO:: Check where each piece can move, Display where each piece can move, Only display when a piece is pressed
    # TODO:: Check if someone has won the game yet

    pygame.display.update()
    clock.tick(60)


pygame.quit()


