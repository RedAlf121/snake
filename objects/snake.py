from collections import deque
import pygame as pg
class Snake:
    def __init__(self, position:pg.Vector2, direction:pg.Vector2,pixel_size:int=32):
        self._direction = direction
        self._body = deque() #Vector2 deque
        self._puntuation = 0
        self._pixel_size = pixel_size
        self._body.append(position)
        self._body.append(position+self._next_move())
    
    @property
    def size(self):
        return self._pixel_size
    
    @property
    def puntuation(self):
        return self._puntuation
    
    @property
    def direction(self):
        return self._direction
    
    @property
    def head(self):
        return self._body[0]
    
    def _next_move(self) -> pg.Vector2:
        return (self.direction*self._pixel_size)
    
    def _previous_move(self) -> pg.Vector2:
        return (self.direction*-1*self._pixel_size)
    
    def move(self):
        """
        Logic movement of the snake
        It doesn't visualize the body
        Only updates all positions
        Using direction attribute
        """
        self._body.appendleft(self._body[0]+self._next_move())
        self._body.pop()
    
    def move_to(self, direction: pg.Vector2):
        """
        Logic movement of the snake
        It doesn't visualize the body
        With a direction parameter
        """
        self._direction = direction
        self.move()
    
    def grow(self):
        self.add_points()
        self._body.append(self._body[-1]-self._previous_move())
    
    def add_points(self):
        self._puntuation+=1
    
    def collide_itself(self):
        collide = False
        
        for i in enumerate(self._body):
            if i[0]>0 and pg.Rect(self.head.x, self.head.y, self.size, self.size).colliderect(pg.Rect(i[1].x,i[1].y,self.size,self.size)):
                collide = True
                break
        
        return collide
    
    def drop_points(self):
        """
        This function generates the points of the snake to be drawed on the interface
        """
        for i in self._body:
            yield(i)