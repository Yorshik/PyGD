import pygame


class End(pygame.sprite.Sprite):
    def __init__(self, *group, x=100, y=100):
        super().__init__(*group)
        self.rect = pygame.rect.Rect(x, y, 64, 64)
        self.name = 'end'
