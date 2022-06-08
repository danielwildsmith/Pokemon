from csv import reader


def import_csv_layout(path):
    terrain_map = []
    with open(path) as level_map:
        layout = reader(level_map, delimiter = ',')
        for row in layout:
            terrain_map.append(list(row))
        return terrain_map


WIDTH = 1280
HEIGHT = 720
FPS = 60
TILESIZE = 12 * 4
