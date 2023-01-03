import pygame
from .constants import *

class Window:
    def __init__(self):
        pygame.init()

        #win = pygame.display.set_mode((screen_width, screen_height), pygame.SCALED) #scale up the window for any other screen size
        self.screen = pygame.display.set_mode((screen_width, screen_height))
        pygame.display.set_caption("Snek :>")

        self.clock = pygame.time.Clock()

        self.screen.fill(bg_colour)