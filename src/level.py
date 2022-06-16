from settings import *
from player import Player
from tile import Tile
from battle import Battle
from random import randint


class Level:
    def __init__(self):
        self.display_surface = pygame.display.get_surface()
        self.visible_sprites = YSortCameraGroup()
        self.invisible_sprites = pygame.sprite.Group()

        self.player = Player((815, 860), [self.visible_sprites], self.invisible_sprites)

        self.create_map()

        self.battle = Battle(self.player)
        self.battle_sequence = False

    def create_map(self):
        layouts = {
            'boundary': import_csv_layout('../map/map_boundaries.csv'),
            'wild_areas': import_csv_layout('../map/map_wild_areas.csv')
        }
        for style, layout in layouts.items():
            for row_index, row in enumerate(layout):
                for col_index, col in enumerate(row):
                    if col != '-1':
                        x = col_index * TILESIZE
                        y = row_index * TILESIZE
                        if style == 'boundary':
                            Tile((x, y), [self.invisible_sprites], 'boundary')
                        if style == 'wild_areas':
                            Tile((x, y), [self.invisible_sprites], 'wild_area')

    def battle_spawn(self):
        if self.player.in_wild_area():
            if randint(1, 150) == 8:
                self.battle_sequence = True

    def run(self):
        if self.battle_sequence:
            self.battle.update()
            if not self.battle.update():
                self.battle_sequence = False
                self.battle = Battle(self.player)
        else:
            self.visible_sprites.custom_draw(self.player)
            self.visible_sprites.update()
            self.battle_spawn()


class YSortCameraGroup(pygame.sprite.Group):
    def __init__(self):
        # general setup
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.half_width = self.display_surface.get_size()[0] // 2
        self.half_height = self.display_surface.get_size()[1] // 2
        self.offset = pygame.math.Vector2(100, 200)

        # creating the map
        self.map_image = pygame.image.load('../graphics/background/Pokemon Town.png')
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
