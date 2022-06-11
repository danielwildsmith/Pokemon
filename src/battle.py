import pygame
from settings import *
from pokemon import Pokemon


class Battle:
    def __init__(self):
        self.display_surface = pygame.display.get_surface()
        self.font = pygame.font.Font(FONT, FONT_SIZE)
        self.battle_background_surf = pygame.image.load('../graphics/background/battle_background.png').convert()
        self.battle_background_surf = pygame.transform.scale(self.battle_background_surf, (WIDTH, HEIGHT - 200))
        self.battle_background_rect = self.battle_background_surf.get_rect(midtop=(WIDTH / 2, 0))

        self.pokemon_sprites = pygame.sprite.Group()
        pikachu = Pokemon('pikachu', (350, 575), self.pokemon_sprites)
        eevee = Pokemon('eevee', (950, 350), self.pokemon_sprites)

        self.pikachu_UI = PokemonUI(700, 575, 200, 100, self.font)

    def display(self):
        self.display_surface.blit(self.battle_background_surf, self.battle_background_rect)
        self.pokemon_sprites.draw(self.display_surface)
        self.pikachu_UI.display(self.display_surface, 'pikachu')


class PokemonUI:
    def __init__(self, left, top, width, height, font):
        self.rect = pygame.Rect(left, top, width, height)
        self.font = font

    def display_info(self, surface, name):
        pokemon_name_surf = self.font.render(name, False, BATTLE_UI_BORDER_TEXT_COLOR)
        pokemon_name_rect = pokemon_name_surf.get_rect(topleft=self.rect.topleft + pygame.math.Vector2(30, 30))
        surface.blit(pokemon_name_surf, pokemon_name_rect)

    def display(self, surface, name):
        pygame.draw.rect(surface, BATTLE_UI_BG_COLOR, self.rect)
        pygame.draw.rect(surface, BATTLE_UI_BORDER_TEXT_COLOR, self.rect, 4)
        self.display_info(surface, name)
