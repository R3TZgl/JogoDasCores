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
    


    def fase(self, cores, rect, num_rect, retangulos, etapas, acertos, time):
        tentativas = 0
        acerto = 0

        while tentativas < etapas:
            tempo = 0

            while True:
                for evento in pygame.event.get():
                    if evento.type == pygame.QUIT:
                        pygame.quit()
                        exit()
                

                self.tela.fill((0,0,0))
                mouse_pos = pygame.mouse.get_pos()

                if num_rect == 0:
                    retangulo(self.tela, cores[0], rect[0])
                elif num_rect == 1:
                    retangulo(self.tela, cores[1], rect[1])
                elif num_rect == 2:
                    retangulo(self.tela, cores[2], rect[2])
                elif num_rect == 3:
                    retangulo(self.tela, cores[3], rect[3])


                for evento in pygame.event.get():
                    if evento.type == pygame.MOUSEBUTTONDOWN:
                        if retangulos[num_rect].collidepoint(mouse_pos):
                            print("clicou")
                            acerto += 1
                            tentativas += 1
                            break
                        
                tempo += 1
                print(tempo)
                if tempo == time:
                    tentativas += 1
                    break
                pygame.display.update()
        
        if acerto < acertos:
            print("perdeu")

        self.status[self.nome] = [acerto,acertos]

        return self.status
            
        
