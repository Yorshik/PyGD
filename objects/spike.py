import pygame

from objects.functions import load_image


class Spike(pygame.sprite.Sprite):
    def __init__(self, *group, x, y, a):
        super().__init__(*group)
        self.image = pygame.transform.rotate(load_image('blocks/spike.png'), a)
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.name = 'spike'
