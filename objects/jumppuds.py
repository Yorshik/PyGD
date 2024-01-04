import pygame

from objects.functions import load_image


class Jumppud(pygame.sprite.Sprite):
    def __init__(self, *group, var, x, y):
        super().__init__(*group)
        self.load_info(var)
        self.activated = False
        self.rect.x = x
        self.rect.y = y
        self.variant = var

    def load_info(self, variant):
        match variant:
            case 'yellow':
                self.image = load_image('blocks/yellow_jumppud.png')
                self.dy = 870 * 1.5
            case 'purple':
                self.image = load_image('blocks/purple_jumppud.png')
                self.dy = 870
            case 'red':
                self.image = load_image('blocks/red_jumppud.png')
                self.dy = 870 * 2
        self.rect = self.image.get_rect()

    def action(self, dct):
        if not self.activated:
            self.activated = True
            dct['player'].mode.vy = self.dy * dct['player'].mode.gravity
