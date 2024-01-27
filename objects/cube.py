import pygame

from objects.constants import LEFTBUTTON, CUBEAY,  MAXSPEED


class Cube(pygame.sprite.Sprite):
    def __init__(self, *group, y=0, parent):
        super().__init__(*group)
        from objects.functions import load_image
        self.name = 'Cube'
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
        if self.gravity == 1:
            if mouse[LEFTBUTTON - 1] or keys[pygame.K_SPACE] or keys[pygame.K_UP]:
                if self.on_ground or self.collide_block:
                    self.vy = 14.5
            if self.bottom_block_y:
                self.rect.y = min(int(self.rect.y - self.vy), self.bottom_block_y - self.rect.h + 1)
            else:
                self.rect.y -= self.vy
            self.vy -= self.ay
        else:
            self.on_ground = False
            if mouse[LEFTBUTTON - 1] or keys[pygame.K_SPACE] or keys[pygame.K_UP]:
                if self.collide_block:
                    self.vy = -14.5
            if self.bottom_block_y:
                self.rect.y = max([int(self.rect.y - self.vy), self.bottom_block_y-1])
            else:
                self.rect.y -= self.vy
            self.vy = min([self.vy + self.ay, MAXSPEED])
        if not self.collide_block and not self.on_ground:
            self.angle += 5 * self.gravity
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
