import pygame.surface
from objects.buttons import Button
import objects.constants
objects.constants.init_variables()


class EndMenu(pygame.surface.Surface):
    def __init__(self):
        super().__init__((800, 600))
        self.exit_button = Button('zatichka.png', (500, 500), self.exit, (50, 50))
        self.reload_button = Button('zatichka.png', (250, 500), self.reload, (50, 50))
        self.buttons = pygame.sprite.Group()
        self.buttons.add(self.exit_button, self.reload_button)

    def exit(self):
        objects.constants.STATUS = 'MAIN'

    def reload(self):
        objects.constants.STATUS = 'GAME'

    def handle_event(self, event):
        for button in self.buttons:
            if button.is_clicked(event):
                button.action()

    def draw(self, surface=None):
        if surface is None:
            surface = pygame.display.get_surface()
        self.fill((255, 0, 255))
        self.buttons.draw(surface)

