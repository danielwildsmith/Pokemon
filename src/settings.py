import pygame
from csv import reader
from os import walk


def import_csv_layout(path):
    terrain_map = []
    with open(path) as level_map:
        layout = reader(level_map, delimiter = ',')
        for row in layout:
            terrain_map.append(list(row))
        return terrain_map


def import_folder(path):
    surface_list = []
    for _, __, image_files in walk(path):
        for image in image_files:
            full_path = path + '/' + image
            image_surf = pygame.image.load(full_path).convert_alpha()
            surface_list.append(image_surf)
    return surface_list


WIDTH = 1280
HEIGHT = 720
FPS = 60
TILESIZE = 12 * 4
FONT = '../graphics/font/joystix.ttf'
FONT_SIZE = 18

pokemon_data = {
    'pikachu': {'health': 20, 'damage': 5, 'moveset': ['Tackle', 'Shock'], 'image': '../graphics/pokemon/pikachu.png'},
    'eevee': {'health': 10, 'damage': 4, 'moveset': ['Tackle', 'Gust'], 'image': '../graphics/pokemon/eevee.png'}
}

BATTLE_UI_BG_COLOR = pygame.color.Color(186, 188, 191)
BATTLE_UI_BORDER_TEXT_COLOR = pygame.color.Color(75, 75, 75)

GRASS_BG_COLOR = pygame.color.Color(180, 217, 190)
