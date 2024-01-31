import pygame

from objects.constants import STARTPOSITION

pygame.init()


class Player(pygame.sprite.Sprite):
    def __init__(self, *group, mode):
        super().__init__(*group)
        from objects.cube import Cube
        from objects.ship import Ship
        from objects.wave import Wave
        self.name = 'Player'
        self.wave = Wave(y=STARTPOSITION, parent=self)
        self.ship = Ship(y=STARTPOSITION, parent=self)
        self.cube = Cube(y=STARTPOSITION, parent=self)
        self.mode = self.change_mode(mode, new=True)
        self.image = self.mode.image
        self.rect = self.mode.rect

    def update_image_and_rect(self, image, rect):
        self.image = image
        self.rect = rect

    def change_mode(self, to, new=False):
        match to:
            case 'ship':
                if new:
                    return self.ship
                ship = self.ship
                if self.mode.__class__ != self.wave.__class__:
                    ship.vy = self.mode.vy
                ship.rect.y = self.mode.rect.y
                ship.gravity = self.mode.gravity
                ship.collide_block = self.mode.collide_block
                ship.on_ground = self.mode.on_ground
                return ship
            case 'cube':
                if new:
                    return self.cube
                cube = self.cube
                if self.mode.__class__ != self.wave.__class__:
                    cube.vy = self.mode.vy
                cube.rect.y = self.mode.rect.y
                cube.gravity = self.mode.gravity
                cube.collide_block = self.mode.collide_block
                cube.on_ground = self.mode.on_ground
                return cube
            case 'wave':
                if new:
                    return self.wave
                wave = self.wave
                wave.rect.y = self.mode.rect.y
                wave.gravity = self.mode.gravity
                wave.collide_block = self.mode.collide_block
                wave.on_ground = self.mode.on_ground
                return wave

    def update(self, *args, **kwargs):
        self.mode.update(*args, **kwargs)
