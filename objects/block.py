import pygame

from objects.functions import load_image


class Block(pygame.sprite.Sprite):
    def __init__(self, *group, x=100, y=100):
        super().__init__(*group)
        self.image = load_image('blocks/block.png')
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.die_from_collision = (True, True, False)
        self.name = 'block'
