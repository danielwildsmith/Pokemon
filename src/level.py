import pygame
from settings import *
from player import Player
from tile import Tile


class Level:
    def __init__(self):
        self.display_surface = pygame.display.get_surface() \
            # TODO: import only ground layer. Then use a create_map function with groups to draw the rest.
        self.visible_sprites = YSortCameraGroup()
        self.obstacle_sprites = pygame.sprite.Group()

        self.player = Player((815, 840), [self.visible_sprites], self.obstacle_sprites)

        self.create_map()

    def create_map(self):
        layouts = {
            'boundary': import_csv_layout('../map/map_boundaries.csv')
        }
        for style, layout in layouts.items():
            for row_index, row in enumerate(layout):
                for col_index, col in enumerate(row):
                    if col != '-1':
                        x = col_index * TILESIZE
                        y = row_index * TILESIZE
                        if style == 'boundary':
                            Tile((x, y), [self.obstacle_sprites], 'invisible')

    def run(self):
        self.visible_sprites.custom_draw(self.player)
        self.visible_sprites.update()


class YSortCameraGroup(pygame.sprite.Group):
    def __init__(self):
        # general setup
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.half_width = self.display_surface.get_size()[0] // 2
        self.half_height = self.display_surface.get_size()[1] // 2
        self.offset = pygame.math.Vector2(100, 200)

        # creating the map
        self.map_image = pygame.image.load('../graphics/Pokemon Town.png')
        self.map_rect = self.map_image.get_rect()

    def custom_draw(self, player):
        # getting the offset
        self.offset.x = player.rect.centerx - self.half_width
        self.offset.y = player.rect.centery - self.half_height

        # drawing the floor
        floor_offset_pos = self.map_rect.topleft - self.offset
        self.display_surface.blit(self.map_image, floor_offset_pos)

        for sprite in sorted(self.sprites(), key=lambda sprite: sprite.rect.centery):
            offset_pos = sprite.rect.topleft - self.offset
            self.display_surface.blit(sprite.image, offset_pos)
