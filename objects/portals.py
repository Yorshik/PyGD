import pygame

from objects.functions import load_image


class Portal(pygame.sprite.Sprite):
    def __init__(self, *group, t=None, x=0, y=0):
        super().__init__(*group)
        self.type = t
        self.activated = False
        self.image = self.load_image()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def load_image(self):
        match self.type:
            case 'to_cube':
                return load_image('blocks/portal_to_cube.png')
            case 'to_ship':
                return load_image('blocks/portal_to_ship.png')
            case 'to_wave':
                return load_image('blocks/portal_to_wave.png')
            # case 'to_ball':
            #     return load_image('blocks/portal_to_ball.png')
            # case 'to_ufo':
            #     return load_image('blocks/portal_to_ufo.png')
            # case 'to_spider':
            #     return load_image('blocks/portal_to_spider.png')
            case 'to_opposite_gravity':
                return load_image('blocks/portal_to_opposite_gravity.png')
            case 'to_normal_gravity':
                return load_image('blocks/portal_to_normal_gravity.png')

    def action(self, dct):
        if not self.activated:
            match self.type:
                case 'to_cube':
                    dct['player'].mode = dct['player'].change_mode('cube')
                case 'to_ship':
                    dct['player'].mode = dct['player'].change_mode('ship')
                case 'to_wave':
                    dct['player'].mode = dct['player'].change_mode('wave')
                # case 'to_ball':
                #     dct['player'].mode = dct['player'].change_mode('ball')
                # case 'to_ufo':
                #     dct['player'].mode = dct['player'].change_mode('ufo')
                # case 'to_spider':
                #     dct['player'].mode = dct['player'].change_mode('spider')
                case 'to_opposite_gravity':
                    dct['player'].mode.gravity = -1
                    dct['player'].mode.rect.y -= 1
                    dct['player'].mode.vy = 0
                case 'to_normal_gravity':
                    dct['player'].mode.gravity = 1
                    dct['player'].mode.vy = 0
            self.activated = True
