import math
import pygame
from objects.constants import LEFTBUTTON, FPS, SHIPAY, HEIGHT, SPEED
from math import ceil


class Ship(pygame.sprite.Sprite):
    def __init__(self, *group, y, parent):
        super().__init__(*group)
        from objects.functions import load_image
        self.image = load_image('player_icons/ship1.png').convert_alpha()
        self.orig = self.image
        self.rect = self.image.get_rect(center=(32, 32))
        self.rect.x = 320
        self.rect.y = y
        self.ay = SHIPAY
        self.vy = 0
        self.on_ground = True
        self.gravity = 1
        self.angle = 0
        self.bottom_block_y = None
        self.top_block_y = None
        self.collide_block = False
        self.parent = parent

    def update(self, *args, **kwargs):
        mouse = pygame.mouse.get_pressed()
        keys = pygame.key.get_pressed()
        if mouse[LEFTBUTTON - 1] or keys[pygame.K_SPACE] or keys[pygame.K_UP]:
            if not self.top_block_y:
                self.vy = min([self.vy + 120 * self.gravity, 1000])
        if self.top_block_y:
            y = self.top_block_y - self.vy / FPS
        elif self.bottom_block_y:
            y = self.bottom_block_y - self.rect.h
        else:
            y = min([self.rect.y - self.vy / FPS, ceil(HEIGHT - 100 - self.rect.h)])
        self.rect.y = y
        if self.rect.y != ceil(HEIGHT - 100 - self.rect.h):
            self.vy = max([self.vy - 50 * self.gravity, -1000])
            self.on_ground = False
        else:
            self.vy = 0
            self.on_ground = True
        if not (self.on_ground or self.collide_block) and self.vy != 0:
            self.angle = math.degrees(math.atan(self.vy / SPEED))/1.7
            if abs(self.angle) > 45:
                self.angle = 45 * self.angle / abs(self.angle)
        else:
            self.angle = 0
        if self.angle:
            self.image = pygame.transform.rotate(self.orig, min(self.angle, 45))
        else:
            self.image = self.orig
        self.parent.update_image_and_rect(self.image, self.rect)
