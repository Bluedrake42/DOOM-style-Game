import pygame as pg
import random
import json

_ = False

# Function to load a random level

def load_random_level():
    level_files = ['levels/level1.json', 'levels/level2.json', 'levels/level3.json']
    selected_file = random.choice(level_files)
    with open(selected_file, 'r') as file:
        mini_map = json.load(file)
    return mini_map

class Map:
    def __init__(self, game):
        self.game = game
        self.mini_map = load_random_level()
        self.world_map = {}
        self.rows = len(self.mini_map)
        self.cols = len(self.mini_map[0])
        self.get_map()

    def reload_map_on_death(self):
        self.mini_map = load_random_level()
        self.world_map.clear()
        self.get_map()

    def get_map(self):
        for j, row in enumerate(self.mini_map):
            for i, value in enumerate(row):
                if value:
                    self.world_map[(i, j)] = value

    def draw(self):
        [pg.draw.rect(self.game.screen, 'darkgray', (pos[0] * 100, pos[1] * 100, 100, 100), 2)
         for pos in self.world_map]