import pygame
from objects.GDPlayer import GDPlayer
from objects.constants import LEFTBUTTON, FPS, AY, HEIGHT


#TODO comments
class Cube(GDPlayer):
    def __init__(self, *group, y):
        super().__init__(*group)
        from objects.functions import load_image
        self.image = load_image('icons/cube1.png')
        self.rect = self.image.get_rect()
        self.rect.x = 320
        self.rect.y = y
        self.ay = AY
        self.vy = 0
        self.on_ground = True
        self.gravity = 1

    def update(self, *args, **kwargs):
        mouse = pygame.mouse.get_pressed()
        keys = pygame.key.get_pressed()
        if mouse[LEFTBUTTON - 1] or keys[pygame.K_SPACE] or keys[pygame.K_UP]:
            if self.on_ground:
                self.vy = 750 * self.gravity
        self.rect.y = min([self.rect.y - self.vy / FPS, int(HEIGHT - 100 - self.rect.h)])
        if self.rect.y != int(HEIGHT - 100 - self.rect.h):
            self.vy = max([self.vy - self.ay * self.gravity, -1000 * self.gravity])
            self.on_ground = False
        else:
            self.vy = 0
            self.on_ground = True
