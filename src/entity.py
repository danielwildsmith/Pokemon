import pygame.time

from settings import *
from random import randint
from math import sin


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

        self.vulnerable = True
        self.attacked_time = None
        self.flicker_time_length = 400

    def attack(self, target_entity, given_attack_index=-1):
        if given_attack_index != -1:
            attack = self.moveset[given_attack_index]
            attack_type = ''
        else:
            attack_index = randint(0, 1)
            attack = list(self.moveset)[attack_index]
            attack_type = 'slash' if attack_index == 0 else 'stat_move'
        if 'stat_move' not in attack_type:
            target_entity.health -= self.damage
            target_entity.attacked_time = pygame.time.get_ticks()
            target_entity.vulnerable = False
            additional_info = ''
        else:
            self.damage += 3
            additional_info = 'Its stats increased!'
        return attack_type, f'{self.name} used {attack}! {additional_info}'

    def heal(self):
        self.health += self.damage
        return f'{self.name} healed itself!'

    def cooldowns(self):
        current_time = pygame.time.get_ticks()
        if not self.vulnerable:
            if current_time - self.attacked_time >= self.flicker_time_length:
                self.vulnerable = True

    def animate(self):
        # flicker effect
        if not self.vulnerable:
            value = sin(pygame.time.get_ticks())
            if value >= 0:
                value = 255
            else:
                value = 0
            self.image.set_alpha(value)
        else:
            self.image.set_alpha(255)

    def update(self):
        self.cooldowns()
        self.animate()
