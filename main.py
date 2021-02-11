import pygame

pygame.init()

height, width = 864,1000

display = pygame.display.set_mode((width,height))
black = (0,0,0)
white = (255,255,255)
brown = (193,154,107)


wood = pygame.image.load("wood.jpg")


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

    for i in range(8):
        for j in range(8):
            if ((i+1)+(j+1)) % 2 == 0:
                pygame.draw.rect(display, white, (100+i*100,46+j*100,100,100))
            else: pygame.draw.rect(display, black, (100+i*100,46+j*100,100,100))
    pygame.display.update()
    clock.tick(60)


pygame.quit()


