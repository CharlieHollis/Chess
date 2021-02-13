import pygame
import os

import boardSection as bs 

pygame.init()

height, width = 864,1000

display = pygame.display.set_mode((width,height))
darkSquare = (118,150,86)
white = (255,255,255)
selected = (186,202,43)

board = []

for i in range(8):
    board.append([])
    for j in range(8):
        if ((i+1)+(j+1)) % 2 == 0:
            board[i].append(bs.board(white, 100+i*100, 46+j*100, i+j))
        else: board[i].append(bs.board(darkSquare, 100+i*100, 46+j*100, i+j))


wood = pygame.image.load(os.path.join("imgs","wood.jpg"))
rook = (pygame.image.load(os.path.join("imgs","WhiteRook.png")),pygame.image.load(os.path.join("imgs","BlackRook.png")))


clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEMOTION:
            # print(pygame.mouse.get_pos())
            pass

    display.blit(wood, (0,0))
    display.blit(wood, (894,0))

    # for i in range(8):
    #     for j in range(8):
    #         if ((i+1)+(j+1)) % 2 == 0:
    #             pygame.draw.rect(display, white, (100+i*100,46+j*100,100,100))
    #         else: pygame.draw.rect(display, darkSquare, (100+i*100,46+j*100,100,100))

    for i in range(len(board)):
        for j in range(len(board[i])):
            pygame.draw.rect(display, board[i][j].colour, (board[i][j].posx,board[i][j].posy,board[i][j].sizex,board[i][j].sizey))

    # display.blit(rook[0],(100,46))
    # display.blit(rook[1],(100,746))

    pygame.display.update()
    clock.tick(60)


pygame.quit()


