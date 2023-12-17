import pygame
from buttons import Button
import buttons_actions


class MainMenu(pygame.surface.Surface):
    def __init__(self):
        super().__init__((1500, int(1500 / 16 * 9)))  # super() для инициализации родительского класса
        self.buttons = [
            Button("Играть", 36, (100, 100), (200, 50), buttons_actions.button1_action),
            Button("Выход", 36, (100, 200), (200, 50),  buttons_actions.button2_action),
        ]

    def handle_event(self, event):
        for button in self.buttons:
            if button.is_clicked(event):
                button.action()

    def draw(self, surface):
        self.fill((255, 255, 255))
        for button in self.buttons:
            button.draw(self)
        surface.blit(self, (0, 0))


pygame.init()
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Main Menu")

menu = MainMenu()

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
             pygame.quit()
        menu.handle_event(event)

    menu.draw(screen)

    pygame.display.flip()
    clock.tick(60)








