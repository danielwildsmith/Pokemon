import pygame.sprite

from settings import *
from entity import Entity


class Battle:
    # TODO: implement a function for displaying the entity's information
    def __init__(self, player):
        self.display_surface = pygame.display.get_surface()
        self.font = pygame.font.Font(FONT, FONT_SIZE)

        self.entity_group = pygame.sprite.Group()
        self.player_entity = Entity(player.entities[0], (275, HEIGHT - 250), self.entity_group)
        self.enemy_entity = Entity('snake', (WIDTH - 325, 190), self.entity_group)

        self.items = self.create_items(f'A wild {self.enemy_entity.name} appeared!')

    def create_items(self, text):
        items = {
            'dialogue': BattleUI(0, HEIGHT - 150, WIDTH / 2, 150, self.font, DIALOGUE_BG_COLOR, DIALOGUE_BORDER_COLOR,
                                 text_color=DIALOGUE_TEXT_COLOR, text=text, type='dialogue'),
            'player_entity': BattleUI(WIDTH / 2 + 45, HEIGHT - 350, 550, 135, self.font, ENTITY_UI_BG_COLOR),
            'enemy_entity': BattleUI(65, 75, 525, 135, self.font, ENTITY_UI_BG_COLOR),
            'attack_1': BattleUI(WIDTH / 2 + 15, HEIGHT - 150, WIDTH / 4 - 30, 65, self.font, MOVESET_BG_COLOR,
                                 text=self.player_entity.moveset[0], text_color=MOVESET_TEXT_COLOR),
            'attack_2': BattleUI(WIDTH * 0.75 + 15, HEIGHT - 150, WIDTH / 4 - 30, 65, self.font, MOVESET_BG_COLOR,
                                 text=self.player_entity.moveset[1], text_color=MOVESET_TEXT_COLOR),
            'attack_3': BattleUI(WIDTH / 2 + 15, HEIGHT - 75, WIDTH / 4 - 30, 65, self.font, MOVESET_BG_COLOR,
                                 text=self.player_entity.moveset[2], text_color=MOVESET_TEXT_COLOR),
            'run_4': BattleUI(WIDTH * 0.75 + 15, HEIGHT - 75, WIDTH / 4 - 30, 65, self.font, MOVESET_BG_COLOR,
                              text='Run', text_color=MOVESET_TEXT_COLOR)
            # TODO: display enemy UI
        }

        return items

    def create_scene(self):
        # TODO: add platforms, maybe try your hand at pixel art
        self.display_surface.fill(GRASS_BG_COLOR)
        platform_one = pygame.Rect(-100, HEIGHT - 250, 700, 200)
        pygame.draw.ellipse(self.display_surface, GRASS_PLATFORM_COLOR, platform_one)
        pygame.draw.ellipse(self.display_surface, GRASS_PLATFORM_BORDER_COLOR, platform_one, 8)

        platform_two = pygame.Rect(WIDTH / 2 + 50, 150, 550, 165)
        pygame.draw.ellipse(self.display_surface, GRASS_PLATFORM_COLOR, platform_two)
        pygame.draw.ellipse(self.display_surface, GRASS_PLATFORM_BORDER_COLOR, platform_two, 8)

    def display(self):
        self.create_scene()
        for item in self.items.values():
            item.display_rect(self.display_surface)
        self.entity_group.draw(self.display_surface)


class BattleUI:
    # TODO: Implement a method for a health bar
    def __init__(self, left, top, width, height, font, color, border_color=None, text=None, text_color=None, type=None):
        self.rect = pygame.Rect(left, top, width, height)
        self.font = font
        self.text = text if text else None
        self.text_color = text_color if text_color else None
        self.color = color
        self.border_color = border_color if border_color else None
        self.type = type if type else None

    def display_rect(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)
        if self.border_color:
            pygame.draw.rect(surface, self.border_color, self.rect, 4)
        else:
            pygame.draw.rect(surface, DEFAULT_BORDER_COLOR, self.rect, 4)

        if self.text:
            text_surf = self.font.render(self.text, False, self.text_color)
            if self.type == 'dialogue':
                text_rect = text_surf.get_rect(topleft=self.rect.topleft + pygame.math.Vector2(15, 15))
            else:
                text_rect = text_surf.get_rect(center=self.rect.center)
            surface.blit(text_surf, text_rect)
