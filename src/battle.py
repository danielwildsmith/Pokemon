from settings import *


class Battle:
    # TODO: implement a function for displaying the entity's information
    def __init__(self):
        self.display_surface = pygame.display.get_surface()
        self.font = pygame.font.Font(FONT, FONT_SIZE)

        self.items = self.create_items()

    def create_items(self):
        items = {
            'dialogue': BattleUI(0, HEIGHT - 150, WIDTH / 2, 150, self.font, BATTLE_UI_BG_COLOR),
            'entity': BattleUI(WIDTH - 400, HEIGHT - 300, 350, 100, self.font, BATTLE_UI_BG_COLOR),
            'option_1': BattleUI(WIDTH / 2 + 15, HEIGHT - 150, WIDTH / 4 - 30, 65, self.font, BATTLE_UI_BG_COLOR),
            'option_2': BattleUI(WIDTH * 0.75 + 15, HEIGHT - 150, WIDTH / 4 - 30, 65, self.font, BATTLE_UI_BG_COLOR),
            'option_3': BattleUI(WIDTH / 2 + 15, HEIGHT - 75, WIDTH / 4 - 30, 65, self.font, BATTLE_UI_BG_COLOR),
            'option_4': BattleUI(WIDTH * 0.75 + 15, HEIGHT - 75, WIDTH / 4 - 30, 65, self.font, BATTLE_UI_BG_COLOR)
            # TODO: display enemy UI
        }

        return items

    def create_scene(self):
        # TODO: add platforms, maybe try your hand at pixel art
        self.display_surface.fill(GRASS_BG_COLOR)

    def display(self):
        self.create_scene()
        for item in self.items.values():
            item.display_rect(self.display_surface)


class BattleUI:
    # TODO: Implement a method for a health bar
    def __init__(self, left, top, width, height, font, color, text=None):
        self.rect = pygame.Rect(left, top, width, height)
        self.font = font
        self.text = text if text else None
        self.color = color

    def display_rect(self, surface):
        if not self.text:
            pygame.draw.rect(surface, self.color, self.rect)
            pygame.draw.rect(surface, BATTLE_UI_BORDER_TEXT_COLOR, self.rect, 4)
        else:
            text_surf = self.font.render(self.text, False, BATTLE_UI_BORDER_TEXT_COLOR)
            text_rect = text_surf.get_rect(center=self.rect.center)
            surface.blit(text_surf, text_rect)
