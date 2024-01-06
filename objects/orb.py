import pygame

from objects.functions import load_image
from objects.wave import Wave


class Orb(pygame.sprite.Sprite):
    def __init__(self, *group, x, y, t):
        super().__init__(*group)
        self.image = self.load_image(t)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.orb = t
        self.activated = False

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

    def action(self, DICT):
        if DICT['player'].mode.__class__ != Wave:
            if not self.activated:
                match self.orb:
                    case 'yellow':
                        DICT['player'].mode.vy = 15 * DICT['player'].mode.gravity
                    case 'purple':
                        DICT['player'].mode.vy = 15 * 0.5 * DICT['player'].mode.gravity
                    case 'black':
                        DICT['player'].mode.vy = -16 * DICT['player'].mode.gravity
                    case 'red':
                        DICT['player'].mode.vy = 15 * 1.5 * DICT['player'].mode.gravity
                self.activated = True
