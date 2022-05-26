import pygame
from sys import exit
from pygame.locals import *
from time import sleep
from random import randint
from retangulos import retangulo


pygame.init()


largura = 800
altura = 600

janela = pygame.display.set_mode((largura, altura))
nome = pygame.display.set_caption('Jogo Sério')

b = 380
h = 280

fase = 0
level = 0

# Retângulos de fundo
red_rect = (10, 10, b, h )
blue_rect = (10 ,310, b, h)
green_rect = (410 ,10, b, h)
yellow_rect = (410, 310, b, h)

#cores
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
yellow = (255,255,0)


fonte = pygame.font.SysFont('arial', 60, True, False)
mensagem = 'INICIAR'
texto = fonte.render(mensagem, True, (255,255,255))
texto_rect = texto.get_rect(center = (400,300))

fps = pygame.time.Clock()
botao_iniciar = True


#Jogo
while True:
    janela.fill((0,0,0))
    mouse_pos = pygame.mouse.get_pos()
    num_rect = randint(0,4)    
    retangulos = [vermelho, azul, verde, amarelo]
    
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            exit()
        if evento.type == pygame.MOUSEBUTTONDOWN: 
            if texto_rect.collidepoint(mouse_pos):
                if fase == 0:
                    print('Iniciar')
                botao_iniciar = False    
                level += 1
                    
    if botao_iniciar:
        vermelho = retangulo(janela, red, red_rect)
        azul = retangulo(janela, blue, blue_rect)
        verde = retangulo(janela, green, green_rect)
        amarelo = retangulo(janela, yellow, yellow_rect)
        
        janela.blit((texto), texto_rect)
    else:    
        while fase == 1:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    exit()
            
            if num_rect == 0:
                vermelho = retangulo(janela, red, red_rect)
            elif num_rect == 1:
                azul = retangulo(janela, blue, blue_rect)
            elif num_rect == 2:
                verde = retangulo(janela, green, green_rect)
            elif num_rect == 3:
                amarelo = retangulo(janela, yellow, yellow_rect)

            print(retangulos[num_rect])


            pygame.display.update()


    

                

            
   
        
        
        
 
    if botao_iniciar == False:
        fase = 1
    
    pygame.display.update()
    fps.tick(60)