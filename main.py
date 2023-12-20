import pygame

from objects.constants import FPS
from menus.main_menu import MainMenu


if __name__ == '__main__':
    pygame.init()
    main_menu = MainMenu()
    screen = pygame.display.set_mode((800, 600), pygame.SCALED, vsync=1)
    clock = pygame.time.Clock()
    while True:
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                main_menu.handle_event(event)
            main_menu.draw(screen)
            pygame.display.flip()
            clock.tick(FPS)
