import pygame
from objects.constants import WIDTH


class Ground(pygame.Surface):
    def __init__(self):
        super().__init__((WIDTH, 100))
        pygame.draw.rect(self, (255, 0, 255), [0, 0, WIDTH, 100])

