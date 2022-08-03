import pygame
from sys import exit, float_repr_style
from pygame.locals import *
from time import sleep
from random import randint
from retangulos import retangulo              


class Partes():
    def __init__(self, nome, tela, status):
        self.nome = nome
        self.tela = tela
        self.status = status
    


    def fase(self, rect, retangulos, etapas, acertos, time, simultaneo):
        tentativas, acerto = 0, 0

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
            segundo = randint(0,3)
            escolha = randint(0,1)
            apertos, tempo = 0, 0
            fase, rect_1, rect_2 = True, True, True
            
            while segundo == num_rect:
                segundo = randint(0,3)

            
            #fase
            while fase:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
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

                #adição de mais um retângulo
                if simultaneo and escolha == 1:
                    if segundo == 0:
                        retangulo(self.tela, cores[0], rect[0])
                    elif segundo == 1:
                        retangulo(self.tela, cores[1], rect[1])
                    elif segundo == 2:
                        retangulo(self.tela, cores[2], rect[2])
                    elif segundo == 3:
                        retangulo(self.tela, cores[3], rect[3])


                if tempo == time * 500:
                    tentativas += 1
                    fase = False

                #clique e colisão
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        exit()
                        
                    #para dois retângulos
                    if simultaneo and escolha == 1:
                        if event.type == pygame.MOUSEBUTTONDOWN and rect_1:
                            if retangulos[num_rect].collidepoint(mouse_pos) :
                                print("clicou no primeiro")
                                apertos += 1
                                rect_1 = False
                        elif event.type == pygame.MOUSEBUTTONDOWN and rect_2:
                            if retangulos[segundo].collidepoint(mouse_pos) :
                                print("clicou no segundo")
                                apertos += 1
                                rect_2 = False                               

                        if apertos == 2:
                            acerto += 1
                            tentativas += 1
                            fase = False
                            print("clicou nos dois")

                    else:
                        #para um retângulo
                        if event.type == pygame.MOUSEBUTTONDOWN:
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
        print(self.status)
        return self.status
        
        
