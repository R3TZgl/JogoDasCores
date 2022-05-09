from ast import Break
import pygame
fase = 1

def lvl(f):
    
    while True:
        if num_rect == 0:
            vermelho = retangulo(janela, red, (10, 10, b, h ))
        if num_rect == 1:
            azul = retangulo(janela, blue, (10 ,310, b, h))
        if num_rect == 2:
            verde = retangulo(janela, green, (410 ,10, b, h))
        if num_rect == 3:
            amarelo = retangulo(janela, yellow, (410, 310, b, h))
        for evento in pygame.event.get():
            if evento.type == pygame.MOUSEBUTTONDOWN:
                if vermelho.collidepoint(mouse_pos):
                    print(f'Pressionou o vermelho ')
                    f = True
                    fase += 1
                elif azul.collidepoint(mouse_pos):
                    print('Pressionou o azul')
                    f = True
                    fase += 1
                elif verde.collidepoint(mouse_pos):
                    print('Pressionou o verde')
                    f = True
                    fase += 1
                elif amarelo.collidepoint(mouse_pos):
                    print('Pressionou o amarelo')    
                    f = True
                    fase += 1
                else:
                    f = False
        if fase == 2:
            break
        pygame.display.update()
    return f                
    