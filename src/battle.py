import pygame
from settings import *


class Battle:
    def __init__(self):
        self.display_surface = pygame.display.get_surface()

    def display(self):
        self.display_surface.fill('gold')
