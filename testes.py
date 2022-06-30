import pygame
from sys import exit
from pygame.locals import *
from time import sleep
from random import randint
from retangulos import retangulo
from level import Partes


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

#Definições para funções
fonte = pygame.font.SysFont('arial', 60, True, False)
mensagem = 'INICIAR'
texto = fonte.render(mensagem, True, (255,255,255))
texto_rect = texto.get_rect(center = (400,300))
musica = pygame.mixer.music.load("audio/axelay.mp3")
pygame.mixer.music.play(-1)

fps = pygame.time.Clock()
botao_iniciar = True

pontos = 0
tempo = 0
num_rect = randint(0,3)
anterior = num_rect
pausa = 0
iniciar = True

status = {}
fase = 1

#Jogo
while True:
    janela.fill((0,0,0))
    mouse_pos = pygame.mouse.get_pos()
        
    
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            exit()

        #Botão iniciar
        if evento.type == pygame.MOUSEBUTTONDOWN: 
            if texto_rect.collidepoint(mouse_pos):
                print('Iniciar')
                botao_iniciar = False    

    
    #Tela inicial                
    if botao_iniciar:
        retangulo(janela, red, red_rect)
        retangulo(janela, blue, blue_rect)
        retangulo(janela, green, green_rect)
        retangulo(janela, yellow, yellow_rect)
        
        janela.blit((texto), texto_rect)

    else:   
        num_rect = randint(0,3) 
        
        #Fases
        level1 = Partes("fase1", janela, status)
        level2 = Partes("fase2", janela, status)
        level3 = Partes("fase3", janela, status)
        level4 = Partes("fase4", janela, status)
        level5 = Partes("fase5", janela, status)

        if fase == 1:
            status = level1.fase(rects, retangulos, 5, 0, 1, False)
        
        elif fase == 2:
            status = level2.fase(rects, retangulos, 5, 0, 1, False)

        elif fase == 3:
            status = level3.fase(rects, retangulos, 5, 0, 1, False)

        elif fase == 4:
            status = level4.fase(rects, retangulos, 5, 0, 1, True)

        elif fase == 5:
            status = level5.fase(rects, retangulos, 5, 0, 1, True)

        if fase > 5:
            mensagem = "FIM"
            texto = fonte.render(mensagem, True, (255,255,255))
            texto_rect = texto.get_rect(center = (400,300))

        if fase <= 5:
            if status[level1.nome][0] < status[level1.nome][1]:
                print("\nPerdeu")
            else:
                print("\nvenceu")
                fase += 1
            
            
        
        janela.fill((0,0,0))
        janela.blit((texto), texto_rect)


    
    
    pygame.display.update()
    fps.tick(60)
