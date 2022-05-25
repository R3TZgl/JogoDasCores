import pygame
from random import randint

pygame.init()


largura = 800
altura = 600
b = 380
h = 280

janela = pygame.display.set_mode((largura, altura))

while True:
    vermelho = pygame.draw.rect(janela, (255,0,0), (10, 10, b, h ))
    azul = pygame.draw.rect(janela, (0,0,255), (10 ,310, b, h))
    verde = pygame.draw.rect(janela, (0,255,0), (410 ,10, b, h))
    amarelo = pygame.draw.rect(janela, (255,255,0), (410, 310, b, h))
    mouse_pos = pygame.mouse.get_pos()
    
    
    

    retangulos = [vermelho, azul, verde, amarelo]
    num_rect = randint(0,4)

    for evento in pygame.event.get():
                    if evento.type == pygame.MOUSEBUTTONDOWN and vermelho.collidepoint(mouse_pos):
                        print(f'Pressionou o vermelho ')
                        break
                    
    pygame.display.update()







#    else:    
#        while fase == 1:
#            
#            if num_rect == 0:
#                vermelho = retangulo(janela, red, (10, 10, b, h ))
#            elif num_rect == 1:
#                azul = retangulo(janela, blue, (10 ,310, b, h))
#            elif num_rect == 2:
#                verde = retangulo(janela, green, (410 ,10, b, h))
#            elif num_rect == 3:
#                amarelo = retangulo(janela, yellow, (410, 310, b, h))
#            print(retangulos[num_rect])
#            for evento in pygame.event.get():
#                if evento.type == pygame.MOUSEBUTTONDOWN and retangulos[num_rect].collidepoint(mouse_pos):
#                    print(f'Pressionou o {retangulos[num_rect]} ')    
#                    fase += 1
#            pygame.display.update()