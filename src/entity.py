from settings import *
from random import choice

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

    def attack(self, given_attack_index=-1):
        if given_attack_index != -1:
            attack = self.moveset[given_attack_index]
        else:
            attack = choice(self.moveset)
        return f'{self.name} used {attack}!'
