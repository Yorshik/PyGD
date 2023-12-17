import pygame


class Button:
    def __init__(self, text, font, position, size, action):
        self.rect = pygame.Rect(position, size)
        self.text = text
        self.action = action
        self.font = font

    def is_clicked(self, event):
        return event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and self.rect.collidepoint(event.pos)

    def draw(self, surface):
        pygame.draw.rect(surface, (200, 200, 200), self.rect)
        font = pygame.font.Font(None, self.font)
        text_render = font.render(self.text, True, (0, 0, 0))
        text_rect = text_render.get_rect(center=self.rect.center)
        surface.blit(text_render, text_rect.topleft)