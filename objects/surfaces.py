import pygame

from objects.constants import WIDTH, SHIP_WAVE_CEIL


class Ground(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.surface.Surface((WIDTH, 100))
        self.rect = pygame.draw.rect(self.image, (0, 100, 255), [0, 0, WIDTH, 100])


class Ceil(pygame.Surface):
    def __init__(self):
        super().__init__((WIDTH, SHIP_WAVE_CEIL))
        pygame.draw.rect(self, (0, 100, 255), [0, 0, WIDTH + 1, SHIP_WAVE_CEIL])
