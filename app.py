import pygame
from pygame.locals import *
from grid import Map
import shutil
class App:
    def __init__(self):
        self._running = True
        self._display_surf = None
        self.size = self.width, self.height = 400, 400

    def on_init(self):
        pygame.init()
        self._display_surf = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        self._running = True
        self._clock = pygame.time.Clock()
        self._dt = self._clock.tick(200)
        self._grid = Map(self.size)
    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False
        elif event.type == pygame.MOUSEBUTTONUP:
            self._grid.mark(int((pygame.mouse.get_pos()[0]/self.width)*8),int((pygame.mouse.get_pos()[1]/self.height)*8))

    def on_loop(self):
        pass

    def on_render(self):
        for i,l in enumerate(self._grid.grid):
            for j, elem in enumerate(l):
                self._display_surf.blit(elem[0], (i*int(self.width/8), j*int(self.height/8)))
                self._display_surf.blit(self._grid.pieceSurfaces[elem[1].value], (i*int(self.width/8), j*int(self.height/8)))
                if elem[2]== 1:
                    self._display_surf.blit(self._grid.frameSurface, (i*int(self.width/8), j*int(self.height/8)))
                elif elem[2]==2:
                    self._display_surf.blit(self._grid.circleSurface, (i*int(self.width/8) + (self.width/8)/2 - (self.width/8)/8, j*int(self.height/8) + int(self.height/8)/2 - int(self.height/8)/8))

        pygame.display.flip()

    def on_cleanup(self):
        shutil.rmtree("__pycache__")
        pygame.quit()
    def on_execute(self):
        if self.on_init() == False:
            self._running = False
        while (self._running):
            self._dt = self._clock.tick(200)
            for event in pygame.event.get():
                self.on_event(event)
            self.on_loop()
            self.on_render()
        self.on_cleanup()
