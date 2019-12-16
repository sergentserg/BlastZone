import pygame as pg
from src.utility.map_loader import map_loader

class Level:
    def __init__(self, level_file, player):
        self.level_file = level_file
        # Needs an image
        self.image = map_loader.make_map(self.level_file)
        self.rect = self.image.get_rect()
        # Needs a list of sprites
        self.level_sprites = pg.sprite.LayeredUpdates()
        map_loader.init_sprites(self.level_sprites, player)
        # Needs game level music
        self.level_music = None

    def update(self, dt):
        self.level_sprites.update(dt)

    def draw(self, screen):
        screen.blit(self.image, self.rect)
        self.level_sprites.draw(screen)
