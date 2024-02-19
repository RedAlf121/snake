import pygame as pg
import sys
from snake import Snake
import numpy as np

#Define constants
UP,DOWN,LEFT,RIGHT = (pg.Vector2(0,1),pg.Vector2(0,-1),pg.Vector2(-1,0),pg.Vector2(1,0))
map_keys = {
    pg.K_UP: (0,-1),
    pg.K_DOWN: (0,1),
    pg.K_LEFT: (-1,0),
    pg.K_RIGHT:(1,0)
}
def draw_food():
    """
    """
    pass

def draw_screen(screen: pg.Surface):
    screen.fill((0,0,0))

def draw_snake(screen,snake: Snake,size=32):
    for pixel in snake.drop_points():
        pg.draw.rect(screen,(255,255,255),pg.Rect(pixel.x,pixel.y,size,size))
        

def get_key():
    game = True
    key = None
    for event in pg.event.get():
        if event.type == pg.QUIT:
            game = False
            break
        if event.type == pg.KEYDOWN:
            key = map_keys.get(event.key,None)
            break
    return game,key

def main_loop():
    screen = pg.display.set_mode((800,600))
    snake = Snake(pg.Vector2(23,23),LEFT)
    clock = pg.time.Clock()
    game = True
    direction = RIGHT
    while game is True:
        draw_screen(screen)
        game,key = get_key()
        direction = key if key is not None else direction
        if game is True:
            snake.move(pg.Vector2(*direction))
            draw_snake(screen,snake)
            #Check collisions
            #If collide with food
            #If collide with itself or it's out of screen
            pg.display.flip()
        clock.tick(5)#FPS

if __name__ == "__main__":
    
    pg.init()
    main_loop()
    pg.quit()