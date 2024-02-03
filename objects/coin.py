import pygame

from objects.functions import load_image


class Coin(pygame.sprite.Sprite):
    def __init__(self, *groups, x, y):
        super().__init__(*groups)
        self.image = load_image('blocks/coin.png')
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.vy = 15
        self.status = 'static'

    def update(self, *args, **kwargs):
        if self.status != 'static':
            self.rect.y -= self.vy
            self.vy -= 0.8
            if self.rect.y > 1000:
                self.kill()
