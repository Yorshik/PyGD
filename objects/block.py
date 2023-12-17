import pygame
from objects.GDObject import GDObject
from objects.functions import load_image


class Block(GDObject):
    def __init__(self, *group, x=100, y=100):
        super().__init__(*group, type_of_object='block')
        self.image = load_image('blocks/block.png')
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.hitbox = pygame.rect.Rect(self.rect.x, self.rect.y, self.rect.w, self.rect.h)
        self.die_from_collision = (True, True, False)
