from settings import *


class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, group, sprite_type, grass_or_water=None, surface=pygame.Surface((TILESIZE, TILESIZE))):
        super().__init__(group)
        self.sprite_type = sprite_type
        self.wild_area_type = grass_or_water
        self.image = surface
        self.rect = self.image.get_rect(topleft=pos)
