from collections import deque
import pygame as pg
class Snake:
    def __init__(self, position:pg.Vector2, direction:pg.Vector2,pixel_size:int=32):
        self._body = deque()
        self._pixel_size = pixel_size
        self._body.append(position)
        self._body.append(position+self._next_move(direction))

    def _next_move(self, direction:pg.Vector2) -> pg.Vector2:
        return (direction*self._pixel_size)
    
    def move(self,direction:pg.Vector2):
        """
        Logic movement of the snake
        It doesn't visualize the body
        Only updates all positions
        """
        self._body.appendleft(self._body[0]+self._next_move(direction))
        self._body.pop()
    
    @property
    def size(self):
        return self._pixel_size
    
    def drop_points(self):
        """
        This function generates the points of the snake to be drawed on the interface
        """
        for i in self._body:
            yield(i)