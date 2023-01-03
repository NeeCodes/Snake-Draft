import pygame

counter = 0
level = counter//5 + 1
score = counter * (10 * level)
game_over = False
run = True

class Game:
    def __init__(self, snake):
        self.counter = 0
        self.level = (self.counter)//5 + 1
        self.score = self.counter * (10 * self.level)
        self.game_over = False
        self.run = True

        self.snake = snake


    def main_loop(self):
        while run:
            if self.game_over:
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
                        self.snake.set_direction('left')

                    elif event.key == pygame.K_RIGHT:
                        self.snake.set_direction('right')

                    elif event.key == pygame.K_UP:
                        self.snake.set_direction('up')

                    elif event.key == pygame.K_DOWN:
                        self.snake.set_direction('down')
                               
                        
            self.snake.move()

            self.snake.draw_snake()

            pygame.display.update()
            self.window.clock.tick(60)