import re
import pygame
from sys import exit
from pygame.locals import *
from time import sleep

pygame.init()


largura = 800
altura = 600

janela = pygame.display.set_mode((largura, altura))
nome = pygame.display.set_caption('Jogo Sério')

b = 380
h = 280

# Retângulos de fundo
red = pygame.draw.rect(janela, (255,0,0), (10, 10, b, h ))
blue = pygame.draw.rect(janela, (0,0,255), (10 ,310, b, h))
green = pygame.draw.rect(janela, (0,255,0), (410 ,10, b, h))
yellow = pygame.draw.rect(janela, (255,255,0), (410, 310, b, h))

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
            
            if texto_rect.collidepoint(mouse_pos):
                print('Iniciar')   
                fase += 1   
                
    mouse_pos = pygame.mouse.get_pos()
    retangulos = [red, blue, green, yellow]
     
     
     
    
    
    
           
    
    
    janela.fill((0,0,0))
    pygame.draw.rect(janela, (255,0,0), (10, 10, b, h ))
    pygame.draw.rect(janela, (0,0,255), (10 ,310, b, h))
    pygame.draw.rect(janela, (0,255,0), (410 ,10, b, h))
    pygame.draw.rect(janela, (255,255,0), (410, 310, b, h))
    
    if fase == 0:
        janela.blit((texto), texto_rect)
    pygame.display.update()