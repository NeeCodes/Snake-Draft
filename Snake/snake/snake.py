import pygame
import random
from collections import deque
from .constants import *
from .game import Game


class Snake:
    def __init__(self, win):
        #self.game = game
        self.win = win

        #self.speed = self.game.level
        self.speed = 1
        self.colour = snek_colour
        self.direction = 'right'
        self.food_eaten = 0

        self.head_x = random.randint(2, cols-3)
        self.head_y = random.randint(3, rows-3)

        self.body = deque()
        self.body.appendleft((self.head_x, self.head_y))

        self.gen_food()

    def init_food(self):
        self._draw_food()
        #self.food_pos = random.choice(list([(x,y) for x in cols for y in rows]))

    def _draw_food(self):
        pygame.draw.rect(self.win, food_colour, ((self.food_x * sq_size), (self.food_y * sq_size), sq_size, sq_size))
        #pygame.draw.rect(win, food_colour, (self.food_pos, sq_size, sq_size))

    def _erase_food(self):
        pygame.draw.rect(self.win, bg_colour, ((self.food_x * sq_size), (self.food_y * sq_size), sq_size, sq_size))

    def gen_food(self):
        #self._erase_food(win)

        self.food_x = random.randint(2, cols-3)
        self.food_y = random.randint(2, rows-3)
        self.food = (self.food_x, self.food_y)

        if (self.food_x, self.food_y) in self.body:
            self.gen_food(self.win)

        self._draw_food()

    def set_direction(self, dir):
        if dir == 'left' and self.direction != 'right':
            self.direction = dir

        if dir == 'right' and self.direction != 'left':
            self.direction = dir

        if dir == 'up' and self.direction != 'down':
            self.direction = dir

        if dir == 'down' and self.direction != 'up':
            self.direction = dir

    def move(self):
        #set the new head position
        if self.direction == 'left':
            self.head_x -= self.speed

        if self.direction == 'right':
            self.head_x += self.speed

        if self.direction == 'up':
            self.head_y -= self.speed

        if self.direction == 'down':
            self.head_y += self.speed

        #the snake hits an edge
        if self._hits_edge():
            pass
            #self.game.game_over = True

        #the snake eats itself
        elif (self.head_x, self.head_y) in self.body:
            pass
            #self.game.game_over = True

        #the snake eats the food
        elif (self.head_x, self.head_y) == (self.food_x, self.food_y):
            self._eat_food()
            self.body.appendleft((self.head_x, self.head_y))

        else:
            self.body.appendleft((self.head_x, self.head_y))
            self.remove_end()
            self.body.pop()

    def _hits_edge(self):
        if self.direction == 'left' and self.head_x == 0:
            return True

        elif self.direction == 'right' and self.head_x == cols - 1:
            return True

        elif self.direction == 'up' and self.head_y == 0:
            return True

        elif self.direction == 'down' and self.head_y == rows - 1:
            return True

        else:
            return False

    def _eat_food(self):
        self.food_eaten += 1
        self.gen_food()

    
    def remove_end(self):
        x = self.body[-1][0]
        y = self.body[-1][1]
        pygame.draw.rect(self.win, bg_colour, (x*sq_size, y*sq_size, sq_size, sq_size))
        #print(self.body[-1])
        # for x, y in *self.body[-1]:
        #     pygame.draw.rect(win, bg_colour, (x*sq_size, y*sq_size, sq_size, sq_size))

    def draw_snake(self):
        for (x,y) in self.body:
            pygame.draw.rect(self.win, snek_colour, (x*sq_size, y*sq_size, sq_size, sq_size))