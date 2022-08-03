import pygame
from sys import exit
from pygame.locals import *

#TESTE DE ERRO DE CLIQUE

pygame.init()


#configurações de tela
largura = 800
altura = 600

janela = pygame.display.set_mode((largura, altura))
nome = pygame.display.set_caption('Jogo Sério')

b = 380
h = 280

#Retângulos de fundo
red_rect = (10, 10, b, h )
blue_rect = (10 ,310, b, h)
green_rect = (410 ,10, b, h)
yellow_rect = (410, 310, b, h)
rects = [red_rect,blue_rect,green_rect,yellow_rect]

#cores
red = (255,0,0)
blue = (0,0,255)
green = (0,255,0)
yellow = (255,255,0)
cores = [red,blue,green,yellow]

#print na tela
vermelho = pygame.draw.rect(janela, red, red_rect)
azul = pygame.draw.rect(janela, blue, blue_rect)
verde = pygame.draw.rect(janela, green, green_rect)
amarelo = pygame.draw.rect(janela, yellow, yellow_rect)
retangulos = [vermelho, azul, verde, amarelo]

while True:
    mouse_pos = pygame.mouse.get_pos()
    janela.fill((0,0,0))
          
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    janela.fill((0,0,0))
    pygame.draw.rect(janela, blue, blue_rect)
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            print("clicou")
        if retangulos[1].collidepoint(mouse_pos):
            print("passou")
   
    pygame.display.update()