import pygame
from sys import exit
from pygame.locals import *
from time import sleep
from random import randint
from retangulos import retangulo              


class Partes():
    def __init__(self,fase):
        self.fase = fase


    def fase(self,):
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
                    pontos += 1
                    break
                    
            tempo += 1
            pygame.display.update()

        