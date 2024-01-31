import pygame

from objects.constants import WIDTH, SHIP_WAVE_CEIL
from objects.label import Label


class Ground(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.surface.Surface((WIDTH, 100))
        self.rect = pygame.draw.rect(self.image, (0, 100, 255), [0, 0, WIDTH, 100])
        self.name = 'ground'


class Ceil(pygame.Surface):
    def __init__(self):
        super().__init__((WIDTH, SHIP_WAVE_CEIL))
        pygame.draw.rect(self, (0, 100, 255), [0, 0, WIDTH + 1, SHIP_WAVE_CEIL])


class NewBest(pygame.Surface):
    def __init__(self):
        super().__init__((1141, 400))
        self.set_colorkey(self.get_at((0, 0)))
        self.label = Label('%', (300, 300), font_size=100, font_color=(1, 1, 1))
        self.image = pygame.image.load('data/resource/images/new_best.png')

    def update(self, percent):
        self.fill((0, 0, 0))
        self.label.text = str(percent) + '%'
        self.label.image = self.label.font.render(self.label.text, True, self.label.font_color)
        self.label.rect = self.label.image.get_rect(topleft=(450, 200))
        self.blit(self.label.image, (self.label.rect.x, self.label.rect.y))
        self.blit(self.image, (0, 0))
