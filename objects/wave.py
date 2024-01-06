from math import ceil

import pygame

from objects.constants import LEFTBUTTON, HEIGHT
from objects.functions import load_image


class Wave(pygame.sprite.Sprite):
    def __init__(self, *group, y, parent):
        super().__init__(*group)
        self.parent = parent
        self.image = load_image('player_icons/wave1.png')
        self.orig = self.image
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = 320
        self.gravity = 1
        self.vy = 0
        self.bottom_block_y = None
        self.top_block_y = None
        self.collide_block = False
        self.on_ground = False

    def update(self):
        keys = pygame.key.get_pressed()
        mouse = pygame.mouse.get_pressed()
        if mouse[LEFTBUTTON - 1] or keys[pygame.K_SPACE] or keys[pygame.K_UP]:
            if not self.top_block_y:
                self.vy = 5
        self.rect.y -= self.vy
        if self.bottom_block_y:
            self.rect.y = min(int(self.rect.y - self.vy), self.bottom_block_y - self.rect.h + 1)
        elif self.top_block_y:
            self.rect.y = self.top_block_y - self.vy
        else:
            self.rect.y = min([int(self.rect.y - self.vy), ceil(HEIGHT - 100 - self.rect.h)])
        if self.collide_block or self.on_ground:
            self.image = self.orig
        elif self.vy > 0:
            self.image = pygame.transform.rotate(self.orig, 45)
        else:
            self.image = pygame.transform.rotate(self.orig, -45)
        if self.rect.y == ceil(HEIGHT - 100 - self.rect.h):
            self.vy = 0
            self.on_ground = True
        else:
            self.vy = -5
            self.on_ground = False
        print(self.vy)
        self.parent.update_image_and_rect(self.image, self.rect)
