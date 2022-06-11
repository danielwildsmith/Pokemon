from settings import *


class Pokemon(pygame.sprite.Sprite):
    def __init__(self, pokemon_name, pos, group):
        super().__init__(group)
        self.image = pygame.image.load(pokemon_data[pokemon_name]['image']).convert_alpha()
        self.image = pygame.transform.scale(self.image, (200, 200))
        self.rect = self.image.get_rect(center=pos)

        self.health = pokemon_data[pokemon_name]['health']
        self.damage = pokemon_data[pokemon_name]['damage']
        self.moveset = pokemon_data[pokemon_name]['moveset']


