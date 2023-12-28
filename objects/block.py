import pygame
from objects.functions import load_image


class Block(pygame.sprite.Sprite):
    def __init__(self, *group, x=100, y=100):
        super().__init__(*group)
        self.image = load_image('blocks/block.png')
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.hitbox = pygame.rect.Rect(self.rect.x, self.rect.y, self.rect.w, self.rect.h)
        self.die_from_collision = (True, True, False)
