import pygame
import os

import boardSection as bs 

pygame.init()

height, width = 1000,1000

display = pygame.display.set_mode((width,height))
darkSquare = (118,150,86)
white = (255,255,255)
selected = (186,202,43)

boardBg = []

for i in range(8):
    boardBg.append([])
    for j in range(8):
        if ((i+1)+(j+1)) % 2 == 0:
            boardBg[i].append(bs.board(os.path.join("imgs","lightSquare.png"), 100+i*100, 100+j*100, i+j))
        else: boardBg[i].append(bs.board(os.path.join("imgs","darkSquare.png"), 100+i*100, 100+j*100, i+j))


wood = pygame.image.load(os.path.join("imgs","wood.jpg"))
rook = (pygame.image.load(os.path.join("imgs","WhiteRook.png")),pygame.image.load(os.path.join("imgs","BlackRook.png")))


clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            
            # print(pygame.mouse.get_pos())
            pass

    display.blit(wood, (0,0)); display.blit(wood, (894,0)); display.blit(wood, (0,894)); display.blit(wood, (894,894))      # Creates Background

    for i in range(len(boardBg)):             # Creates Board
        for j in range(len(boardBg[i])):
            display.blit(boardBg[i][j].colour, (boardBg[i][j].posx, boardBg[i][j].posy))


    display.blit(rook[0],(100,46))
    display.blit(rook[1],(100,746))

    pygame.display.update()
    clock.tick(60)


pygame.quit()


