import pygame

class Label(pygame.sprite.Sprite):
    def __init__(self, text, position, font_size=20, font_color=(0, 0, 0)):
        super().__init__()

        self.font = pygame.font.Font(None, font_size)
        self.text = text
        self.font_color = font_color

        self.image = self.font.render(self.text, True, self.font_color)
        self.rect = self.image.get_rect(topleft=position)