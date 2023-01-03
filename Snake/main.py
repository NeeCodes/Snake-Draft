import pygame
import random
import math
from collections import deque
from sys import exit

from snake.snake import Snake
from snake.constants import *
from snake.window import Window
from snake.game import Game


window = Window()
win = window.screen

run = True
game_over = False

snake = Snake(win)

snake.init_food()

game = Game(snake)


while run:
    if game_over:
        pygame.display.update()
        continue

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
            exit()
            break

        if event.type == pygame.KEYDOWN: #any button pressed
            if event.key == pygame.K_LEFT:
                snake.set_direction('left')

            elif event.key == pygame.K_RIGHT:
                snake.set_direction('right')

            elif event.key == pygame.K_UP:
                snake.set_direction('up')

            elif event.key == pygame.K_DOWN:
                snake.set_direction('down')
 
                
    snake.move()

    snake.draw_snake()

    pygame.display.update()

    window.clock.tick(10)

