import random
import pygame as pg
class Food:
    def __init__(self,bounds:tuple[int,int],pixel_size=16) -> None:
        self._position = pg.Vector2(0,0)
        self._pixel_size = pixel_size
        self.update_position(bounds)
    
    def update_position(self,bounds:tuple[int,int]):
        x = random.randrange(self._pixel_size,bounds[0]-self._pixel_size)
        y = random.randrange(self._pixel_size,bounds[1]-self._pixel_size)
        self._position = pg.Vector2(x,y)
    
    @property
    def position(self):
        return self._position