import pygame

from objects.functions import load_image


class Jumppud(pygame.sprite.Sprite):
    def __init__(self, *group, var, x, y):
        super().__init__(*group)
        self.image = self.load_image(var)
        self.activated = False
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.variant = var
        self.name = 'jumppud'

    def load_image(self, variant):
        match variant:
            case 'yellow':
                return load_image('blocks/yellow_jumppud.png')
            case 'purple':
                return load_image('blocks/purple_jumppud.png')
            case 'red':
                return load_image('blocks/red_jumppud.png')
            case 'blue':
                return load_image('blocks/blue_jumppud.png')

    def action(self, dct):
        if not self.activated:
            self.activated = True
            match self.variant:
                case 'yellow':
                    dct['player'].mode.vy = 15 * 1.5 * dct['player'].mode.gravity
                case 'red':
                    dct['player'].mode.vy = 15 * 2 * dct['player'].mode.gravity
                case 'purple':
                    dct['player'].mode.vy = 15 * dct['player'].mode.gravity
                case 'blue':
                    dct['player'].mode.gravity = -dct['player'].mode.gravity
                    dct['player'].mode.vy = 0
