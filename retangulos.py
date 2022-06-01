import pygame

def retangulo(a,b,c):
    pygame.draw.rect(a, b, c)
    pygame.draw.rect(a, (0,0,0), c, 5)
