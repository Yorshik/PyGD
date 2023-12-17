import pygame
from objects.constants import HEIGHT, FPS, SPEED


class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[None] * width for _ in range(height)]
        self.left = 0
        self.top = 0
        self.cell_size = 64
        self.clicked_cell = None

    def set_view(self):
        self.top = HEIGHT - 100 - self.cell_size * len(self.board[0])

    def render(self, scr):
        for i, row in enumerate(self.board):
            for j, el in enumerate(row):
                pygame.draw.rect(scr, (255, 255, 255),
                                 [self.left + i * self.cell_size, self.top + j * self.cell_size, self.cell_size,
                                  self.cell_size], width=1
                                 )
                if el:
                    el.rect.x -= SPEED / FPS

    def get_cell(self, pos):
        if self.left <= pos[0] <= len(self.board) * self.cell_size + self.left and self.top <= pos[1] <= len(
                self.board[0]
        ) * self.cell_size + self.top:
            return (pos[1] - self.top) // self.cell_size, (pos[0] - self.left) // self.cell_size
        return None
