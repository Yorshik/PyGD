import pygame
from objects.functions import load_image


class GDPlayer(pygame.sprite.Sprite):
    def __init__(self, *group):
        super().__init__(*group)
        self.image = load_image('icons/standard.png')
        self.rect = self.image.get_rect()
        self.rect.x = 300
        self.ay = 0
        self.vy = 0
        self.on_ground = True
        self.gravity = 1

    def move(self):
        pass

    def update(self, *args, **kwargs):
        pass

