import pygame.display


class Level:
    def __init__(self):
        self.display_surface = pygame.display.get_surface() \
            # TODO: import only ground layer. Then use a create_map function with groups to draw the rest.
        self.map_image = pygame.image.load('../graphics/Pokemon Town.png')
        self.map_rect = self.map_image.get_rect()

    def run(self):
        self.display_surface.blit(self.map_image, self.map_rect)
