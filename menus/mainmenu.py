import pygame
from objects.buttons import Button
import sys


class MainMenu(pygame.surface.Surface):
    def __init__(self):
        super().__init__((1500, int(1500 / 16 * 9)))  # super() для инициализации родительского класса
        self.buttons = [
            Button("Играть", 36, (100, 100), (200, 50), self.button1_action),
            Button("Выход", 36, (100, 200), (200, 50),  sys.exit),
        ]

    def button1_action(self):
        from objects.functions import run_game
        run_game()

    def handle_event(self, event):
        for button in self.buttons:
            if button.is_clicked(event):
                button.action()

    def draw(self, surface):
        self.fill((255, 255, 255))
        for button in self.buttons:
            button.draw(self)
        surface.blit(self, (0, 0))