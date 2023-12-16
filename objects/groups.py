import pygame


class PlayerGroup(pygame.sprite.Group):
    def __init__(self):
        super().__init__()

    def update(self, *args, **kwargs):
        self.sprites()[0].update()


class DHGroup(pygame.sprite.Group):
    def __init__(self):
        super().__init__()

    def update(self, *args, **kwargs):
        for sprite in self.sprites():
            sprite.update()


class EndGroup(pygame.sprite.Group):
    def __init__(self):
        super().__init__()

    def update(self, *args, **kwargs):
        for sprite in self.sprites():
            sprite.update()


class BlockGroup(pygame.sprite.Group):
    def __init__(self):
        super().__init__()

    def update(self, *args, **kwargs):
        for sprite in self.sprites():
            sprite.update()


class SpikeGroup(pygame.sprite.Group):
    def __init__(self):
        super().__init__()

    def update(self, *args, **kwargs):
        for sprite in self.sprites():
            sprite.update()


class OrbGroup(pygame.sprite.Group):
    def __init__(self):
        super().__init__()

    def update(self, *args, **kwargs):
        for sprite in self.sprites():
            sprite.update()


class JumppudGroup(pygame.sprite.Group):
    def __init__(self):
        super().__init__()

    def update(self, *args, **kwargs):
        for sprite in self.sprites():
            sprite.update()


class PortalGroup(pygame.sprite.Group):
    def __init__(self):
        super().__init__()

    def update(self, *args, **kwargs):
        for sprite in self.sprites():
            sprite.update()


class SpeedGroup(pygame.sprite.Group):
    def __init__(self):
        super().__init__()

    def update(self, *args, **kwargs):
        for sprite in self.sprites():
            sprite.update()


class CoinGroup(pygame.sprite.Group):
    def __init__(self):
        super().__init__()

    def update(self, *args, **kwargs):
        for sprite in self.sprites():
            sprite.update()
