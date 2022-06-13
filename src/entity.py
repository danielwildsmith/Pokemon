from settings import *


class Entity(pygame.sprite.Sprite):
    def __init__(self, entity_name, pos, group):
        super().__init__(group)
        self.image = pygame.image.load(entity_data[entity_name]['image']).convert_alpha()
        self.image = pygame.transform.scale(self.image, (125, 125))
        self.rect = self.image.get_rect(center=pos)

        self.name = entity_name
        self.health = entity_data[entity_name]['health']
        self.damage = entity_data[entity_name]['damage']
        self.moveset = entity_data[entity_name]['moveset']
