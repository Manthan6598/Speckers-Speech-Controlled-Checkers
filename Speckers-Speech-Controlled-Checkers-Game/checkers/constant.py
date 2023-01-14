# -*- coding: utf-8 -*-
"""
Created on Wed Nov 30 16:22:59 2022

@author: Admin
"""
import pygame 

#-------BOARD DIMENSIONS-------------#

WIDTH, HEIGHT = 600,600
ROWS, COLS = 8,8
SQUARE_SIZE = WIDTH//COLS


#--------RGB COLORS----------------#

RED = (255,0,0)
WHITE = (255,255,255)
BLACK = (139, 0, 0)
BLUE = (0,0,255)
GREY = (128,28,128)
SKIN = (75,83,32)

CROWN = pygame.transform.scale(pygame.image.load('assets/crown.png'),(30,20))