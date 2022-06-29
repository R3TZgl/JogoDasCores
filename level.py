import pygame
from sys import exit
from pygame.locals import *
from time import sleep
from random import randint
from retangulos import retangulo              


class Partes():
    def __init__(self, nome, tela, status):
        self.nome = nome
        self.tela = tela
        self.status = status
    


    def fase(self, rect, retangulos, etapas, acertos, time):
        tentativas = 0
        acerto = 0

        red = (255,0,0)
        blue = (0,0,255)
        green = (0,255,0)
        yellow = (255,255,0)
        cores = [red,blue,green,yellow]


        while tentativas < etapas:

            #Contagem
            for c in range(3, 0, -1):
                fonte = pygame.font.SysFont('arial', 60, True, False)
                texto = fonte.render(f"{c}", True, (255,255,255))
                texto_rect = texto.get_rect(center = (400,300))
                
                self.tela.fill((0,0,0))
                self.tela.blit((texto), texto_rect)
                pygame.display.update()
                sleep(0.7)

        
            num_rect = randint(0,3)
            tempo = 0
            fase = True

            while fase:
                for evento in pygame.event.get():
                    if evento.type == pygame.QUIT:
                        pygame.quit()
                        exit()
                

                self.tela.fill((0,0,0))
                mouse_pos = pygame.mouse.get_pos()
                

                #Escolha de retangulos na tela
                if num_rect == 0:
                    retangulo(self.tela, cores[0], rect[0])
                elif num_rect == 1:
                    retangulo(self.tela, cores[1], rect[1])
                elif num_rect == 2:
                    retangulo(self.tela, cores[2], rect[2])
                elif num_rect == 3:
                    retangulo(self.tela, cores[3], rect[3])

                if tempo == time*500:
                    tentativas += 1
                    fase = False

                #Clique e colisão
                for evento in pygame.event.get():
                    if evento.type == pygame.MOUSEBUTTONDOWN:
                        if retangulos[num_rect].collidepoint(mouse_pos):
                            print("clicou")
                            acerto += 1
                            tentativas += 1
                            fase = False
                        
                tempo += 1
                
                pygame.display.update()
        

        if acerto < acertos:
            print("perdeu")

        self.status[self.nome] = [acerto, acertos, etapas]

        return self.status
            
        
