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

#Retângulos de fundo
red_rect = (10, 10, b, h )
blue_rect = (10 ,310, b, h)
green_rect = (410 ,10, b, h)
yellow_rect = (410, 310, b, h)

#cores
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
yellow = (255,255,0)

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
#musica = pygame.mixer.music.load("audio/axelay.mp3")
#pygame.mixer.music.play(-1)

fps = pygame.time.Clock()
botao_iniciar = True

pontos = 0
tempo = 0
num_rect = randint(0,3)
anterior = num_rect
pausa = 0
fase1 = True

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
                if fase == 0:
                    print('Iniciar')
                botao_iniciar = False    
                level += 1
    
    #Tela inicial                
    if botao_iniciar:
        retangulo(janela, red, red_rect)
        retangulo(janela, blue, blue_rect)
        retangulo(janela, green, green_rect)
        retangulo(janela, yellow, yellow_rect)
        
        janela.blit((texto), texto_rect)
    
    else:  
        #Fases  
        while fase == 1:
            anterior = num_rect
            num_rect = randint(0,3)
            
            if num_rect == anterior:
                while num_rect == anterior:
                    num_rect = randint(0,3)

            #Saída 
            while fase1:
                for evento in pygame.event.get():
                    if evento.type == pygame.QUIT:
                        pygame.quit()
                        exit()
                
                
                janela.fill((0,0,0))
                mouse_pos = pygame.mouse.get_pos()

                if num_rect == 0:
                    retangulo(janela, red, red_rect)
                elif num_rect == 1:
                    retangulo(janela, blue, blue_rect)
                elif num_rect == 2:
                    retangulo(janela, green, green_rect)
                elif num_rect == 3:
                    retangulo(janela, yellow, yellow_rect)

                #Funções do jogo
                if evento.type == pygame.MOUSEBUTTONDOWN:
                    if retangulos[num_rect].collidepoint(mouse_pos) or tempo == 5000:
                        print("clicou")  
                        tempo = 0
                        pausa = 0
                        pontos += 1
                        break
                      
                tempo += 1
                pygame.display.update()
            
            #Contadores
            pausa += 1
            if pausa == 1000:
                fase1 = True
            else:
                fase1 = False

            if pontos == 5:
                janela.blit((texto), texto_rect)
                break

            janela.fill((0,0,0))
            pygame.display.update()



    if botao_iniciar == False:
        fase = 1
    
    pygame.display.update()
    fps.tick(60)