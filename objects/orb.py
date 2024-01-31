import time

import pygame

from objects.functions import load_image


class Orb(pygame.sprite.Sprite):
    def __init__(self, *group, x, y, t):
        super().__init__(*group)
        self.image = self.load_image(t)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.orb = t
        self.activated = False
        self.name = 'orb'
        self.time_of_activation = None

    def load_image(self, orb):
        match orb:
            case 'yellow':
                return load_image('blocks/yellow_orb.png')
            case 'purple':
                return load_image('blocks/purple_orb.png')
            case 'black':
                return load_image('blocks/black_orb.png')
            case 'red':
                return load_image('blocks/red_orb.png')
            case 'blue':
                return load_image('blocks/blue_orb.png')
            case 'green':
                return load_image('blocks/green_orb.png')

    def action(self, dct):
        if not self.activated:
            match self.orb, dct['player'].mode.name:
                case 'yellow', 'Cube' | 'Ship':
                    dct['player'].mode.vy = 15 * dct['player'].mode.gravity
                case 'purple', 'Cube' | 'Ship':
                    dct['player'].mode.vy = 15 * 0.5 * dct['player'].mode.gravity
                case 'black', 'Cube' | 'Ship':
                    dct['player'].mode.vy = -16 * dct['player'].mode.gravity
                case 'red', 'Cube' | 'Ship':
                    dct['player'].mode.vy = 15 * 1.5 * dct['player'].mode.gravity
                case 'green', _:
                    dct['player'].mode.gravity = -dct['player'].mode.gravity
                case 'blue', _:
                    dct['player'].mode.gravity = -dct['player'].mode.gravity
                    if dct['player'].mode.name == 'Ship':
                        dct['player'].mode.top_block_y, dct['player'].mode.bottom_block_y = dct[
                            'player'].mode.bottom_block_y, dct['player'].mode.top_block_y
                    dct['player'].mode.vy = 0
            self.activated = True
            self.time_of_activation = time.time()
        else:
            if time.time() - self.time_of_activation > 1:
                self.time_of_activation = None
                self.activated = False
