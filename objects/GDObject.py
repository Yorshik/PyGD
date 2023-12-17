import pygame

from objects.functions import load_image


#TODO comments
class GDObject(pygame.sprite.Sprite):
    def __init__(self, *group, type_of_object=None):
        super().__init__(*group)
        self.image = load_image('blocks/standard.png')
        self.rect = self.image.get_rect()
        self.rect.x = 100
        self.rect.y = 0
        self.type = type_of_object
        self.die_from_collision = (False, False, False)
        self.dx = 0
        self.dy = 0
        self.hitbox = pygame.rect.Rect(0, 0, 10, 10)
