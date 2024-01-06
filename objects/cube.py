from math import ceil

import pygame

from objects.constants import LEFTBUTTON, CUBEAY, HEIGHT


# TODO comments
class Cube(pygame.sprite.Sprite):
    def __init__(self, *group, y=0, parent):
        super().__init__(*group)
        from objects.functions import load_image
        self.image = load_image('player_icons/cube1.png').convert_alpha()
        self.orig = self.image
        self.rect = self.image.get_rect(center=(32, 32))
        self.collide_block = False
        self.rect.x = 320
        self.rect.y = y
        self.ay = CUBEAY
        self.vy = 0
        self.on_ground = True
        self.gravity = 1
        self.angle = 0
        self.bottom_block_y = None
        self.parent = parent

    def update(self, *args, **kwargs):
        mouse = pygame.mouse.get_pressed()
        keys = pygame.key.get_pressed()
        if mouse[LEFTBUTTON - 1] or keys[pygame.K_SPACE] or keys[pygame.K_UP]:
            if self.on_ground or self.collide_block:
                self.vy = 14.5 * self.gravity
        if self.bottom_block_y:
            self.rect.y = min(int(self.rect.y - self.vy), self.bottom_block_y - self.rect.h + 1)
        else:
            self.rect.y = min([int(self.rect.y - self.vy), ceil(HEIGHT - 100 - self.rect.h)])
        if self.rect.y != ceil(HEIGHT - 100 - self.rect.h):
            self.vy = max([self.vy - self.ay * self.gravity, -1000 * self.gravity])
            self.on_ground = False
        else:
            self.vy = 0
            self.on_ground = True
        if not self.collide_block and not self.on_ground:
            self.angle += 5
            self.image = pygame.transform.rotate(self.orig, -self.angle)
        else:
            if self.angle:
                if self.angle < 45 or self.angle >= 315:
                    self.image = self.orig
                    self.angle = 0
                elif 45 <= self.angle <= 135:
                    self.image = pygame.transform.rotate(self.orig, -90)
                    self.angle = 90
                elif 135 <= self.angle < 225:
                    self.image = pygame.transform.rotate(self.orig, -180)
                    self.angle = 180
                elif 225 <= self.angle < 315:
                    self.image = pygame.transform.rotate(self.orig, -270)
                    self.angle = 270
        self.parent.update_image_and_rect(self.image, self.rect)
