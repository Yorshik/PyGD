import pygame
from objects.GDObject import GDObject


class End(GDObject):
    def __init__(self, *group):
        super().__init__(*group, type_of_object='ending')