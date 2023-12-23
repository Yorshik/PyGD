import pygame
from objects.GDPlayer import GDPlayer
from objects.constants import LEFTBUTTON, FPS, AY, HEIGHT


#TODO comments
class Cube(GDPlayer):
    def __init__(self, *group, y):
        super().__init__(*group)
        from objects.functions import load_image
        self.image = load_image('player_icons/cube1.png').convert_alpha()
        self.orig = self.image
        self.rect = self.image.get_rect(center=(32, 32))
        self.on_block = False
        self.rect.x = 320
        self.rect.y = y
        self.ay = AY
        self.vy = 0
        self.on_ground = True
        self.gravity = 1
        self.angle = 0
        self.block_y = None

    def rotate(self):
        direction = pygame.math.Vector2(self.rect.x + self.rect.w//2, self.rect.y + self.rect.y//2)
        angle = direction.as_polar()[1]
        self.image = pygame.transform.rotate(self.orig, -angle + 90 - self.angle)

    def set_on_block(self, boolean):
        self.on_block = boolean

    def update(self, *args, **kwargs):
        mouse = pygame.mouse.get_pressed()
        keys = pygame.key.get_pressed()
        if mouse[LEFTBUTTON - 1] or keys[pygame.K_SPACE] or keys[pygame.K_UP]:
            if self.on_ground or self.on_block:
                self.vy = 870 * self.gravity
        if self.block_y:
            y = min([self.rect.y - self.vy / FPS, max([int(HEIGHT - 100 - self.rect.h), int(self.block_y)])])
        else:
            y = min([self.rect.y - self.vy / FPS, int(HEIGHT - 100 - self.rect.h)])
        self.rect.y = y
        if self.rect.y != int(HEIGHT - 100 - self.rect.h):
            self.vy = max([self.vy - self.ay * self.gravity, -1000 * self.gravity])
            self.on_ground = False
        else:
            self.vy = 0
            self.on_ground = True
        if not self.on_ground and not self.on_block:
            self.angle += 5
            self.rotate()
        else:
            if self.angle < 45 or self.angle > 315:
                self.image = self.orig
            elif 45 < self.angle <= 135:
                self.image = pygame.transform.rotate(self.orig, -90)
            elif 135 < self.angle <= 225:
                self.image = pygame.transform.rotate(self.orig, -180)
            elif 225 < self.angle <= 315:
                self.image = pygame.transform.rotate(self.orig, -270)
            self.angle = 0
