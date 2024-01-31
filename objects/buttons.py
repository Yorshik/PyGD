import pygame

from objects.constants import LEFTBUTTON


class Button(pygame.sprite.Sprite):
    def __init__(self, image_path, position, action, size=(50, 50)):
        super().__init__()
        self.original_image = pygame.image.load(image_path)
        self.image = pygame.transform.smoothscale(self.original_image, size)
        self.rect = self.image.get_rect(topleft=position)
        self.action = action

    def is_clicked(self, event):
        return event.type == pygame.MOUSEBUTTONUP and event.button == LEFTBUTTON and self.rect.collidepoint(event.pos)

    def scale(self, factor):
        self.image = pygame.transform.smoothscale(
            self.original_image, (int(self.rect.width * factor), int(self.rect.height * factor))
        )
        self.rect = self.image.get_rect(topleft=self.rect.topleft)
