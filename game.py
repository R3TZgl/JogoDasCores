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

# Retângulos de fundo
vermelho = pygame.draw.rect(janela, (255,0,0), (10, 10, b, h ))
azul = pygame.draw.rect(janela, (0,0,255), (10 ,310, b, h))
verde = pygame.draw.rect(janela, (0,255,0), (410 ,10, b, h))
amarelo = pygame.draw.rect(janela, (255,255,0), (410, 310, b, h))

#cores
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
yellow = (255,255,0)


fonte = pygame.font.SysFont('arial', 60, True, False)
mensagem = 'INICIAR'
texto = fonte.render(mensagem, True, (255,255,255))
texto_rect = texto.get_rect(center = (400,300))

fase = 0


while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            exit()
        
        if evento.type == pygame.MOUSEBUTTONDOWN: 
            if retangulos[0].collidepoint(mouse_pos):
                print('Pressionou o vermelho') 
            elif retangulos[1].collidepoint(mouse_pos):
                print('Pressionou o azul')
            elif retangulos[2].collidepoint(mouse_pos):
                print('Pressionou o verde')
            elif retangulos[3].collidepoint(mouse_pos):
                print('Pressionou o amarelo')    
            
            
            if texto_rect.collidepoint(mouse_pos):
                print('Iniciar')   
                fase += 1  
             
    num_rect = randint(0,4)            
    mouse_pos = pygame.mouse.get_pos()

    retangulos = [vermelho, azul, verde, amarelo] 

     
    
    
    
           
    
    
    janela.fill((0,0,0))
    vermelho = retangulo(janela, red, (10, 10, b, h ))
    azul = retangulo(janela, blue, (10 ,310, b, h))
    verde = retangulo(janela, green, (410 ,10, b, h))
    amarelo = retangulo(janela, yellow, (410, 310, b, h))
    
    if fase == 0:
        janela.blit((texto), texto_rect)
    pygame.display.update()