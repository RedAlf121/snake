import random
import pygame as pg
from objects.snake import Snake
class Food:
    def __init__(self,bounds:tuple[int,int],pixel_size=16) -> None:
        self._position = pg.Vector2(0,0)
        self._pixel_size = pixel_size
        self._bounds = bounds
        self.update_position()
    
    def update_position(self):
        x = random.randrange(self._pixel_size,self._bounds[0]-self._pixel_size)
        y = random.randrange(self._pixel_size,self._bounds[1]-self._pixel_size)
        self._position = pg.Vector2(x,y)
    
    def feed(self, snake: Snake):
        snake.grow()
    
    @property
    def size(self):
        return self._pixel_size
    
    @property
    def position(self):
        return self._position