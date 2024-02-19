import pygame as pg
import sys
from objects.food import Food
from objects.snake import Snake
import numpy as np

#Define constants
UP,DOWN,LEFT,RIGHT = (pg.Vector2(0,1),pg.Vector2(0,-1),pg.Vector2(-1,0),pg.Vector2(1,0))
map_keys = {
    pg.K_UP: (0,-1),
    pg.K_DOWN: (0,1),
    pg.K_LEFT: (-1,0),
    pg.K_RIGHT:(1,0)
}

def draw_screen(screen: pg.Surface,food: pg.Vector2, size=16):
    screen.fill((0,0,0))
    pg.draw.rect(screen,(255,0,0),pg.Rect(food.x,food.y,size,size))

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
            if key is not None:
                key = pg.Vector2(*key)
            break
    return game,key

def check_food_collision(snake: Snake,food: Food):
    return pg.Rect(snake.head.x, snake.head.y, snake.size, snake.size).colliderect(pg.Rect(food.position.x,food.position.y,food.size,food.size))

def check_out_bounds(snake: Snake, screen: pg.Surface):
    pass


def check_loose_collisions(snake: Snake, screen: pg.Surface):
    return check_out_bounds(snake,screen) or snake.collide_itself()

def main_loop():
    size = 32
    screen = pg.display.set_mode((800,600))
    
    snake = Snake(pg.Vector2(*[i/2-size/2 for i in screen.get_size()]),LEFT,size)
    
    clock = pg.time.Clock()
    game = True
    direction = RIGHT
    food = Food(screen.get_size(),size//2)
    while game is True:
        draw_screen(screen,food.position)
        game,key = get_key()
        
        direction = key if key is not None and key.dot(direction)!= -1 else direction
        if game is True:
            snake.move_to(direction)
            draw_snake(screen,snake,size)
            #Check collisions
            #If collide with itself or it's out of screen
            if check_loose_collisions(snake,screen):
                game = False
                print("Game Over")
            #If collide with food
            elif check_food_collision(snake,food):
                food.feed(snake)
                food.update_position()
            pg.display.flip()
        clock.tick(5)#FPS

if __name__ == "__main__":
    
    pg.init()
    main_loop()
    pg.quit()