import pygame


def fase(a):
    
    while fase == a:
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
                if retangulos[num_rect].collidepoint(mouse_pos):
                    print(f'Pressionou o {retangulos[num_rect]} ')
    return                
    