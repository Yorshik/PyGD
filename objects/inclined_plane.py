import pygame

from objects.functions import load_image


class InclinedPlane(pygame.sprite.Sprite):
    def __init__(self, *group, x, y, a):
        super().__init__(*group)
        self.image = pygame.transform.rotate(load_image('\\blocks\\inclined_plane.png'), a)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.mask = pygame.mask.from_surface(self.image)
        self.name = 'inclined_plane'
