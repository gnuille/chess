import pygame
from pygame.locals import *

class Horse(pygame.sprite.Sprite):
    def __init__(self, dimm, posX, posY):
        super().__init__()
        self.surface =  pygame.transform.scale(pygame.image.load("img/white_horse.png").convert_alpha(), (int(dimm[0]/8), int(dimm[1]/8)))
        self.posX = posX
        self.posY = posY
        self.dimm = dimm
    def move(self, i, j):
        self.posX = i*(self.dimm[0]/8)
        self.posY = j*(self.dimm[1]/8)
