import copy

import pygame

import objects.constants
from objects.constants import HEIGHT

objects.constants.init_variables()


class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = None
        self.left = 0
        self.top = 0
        self.cell_size = 64
        self.clicked_cell = None
        self.start = None

    def __copy__(self):
        board = Board(0, 0)
        board.board = copy.copy(self.board)
        board.set_view()
        return board

    def set_view(self):
        self.top = HEIGHT - 100 - self.cell_size * len(self.board[0])

    def reset(self):
        for i, row in enumerate(self.board):
            for j, el in enumerate(row):
                if el:
                    el.rect.x = i * 64
                    el.rect.y = (j + 1) * 64 - el.rect.h + self.top - 1

    def render(self, scr, changes=True, draw=True):
        if changes:
            dx = 8 * objects.constants.GAMESPEED
            self.left -= dx
        for i, row in enumerate(self.board):
            for j, el in enumerate(row):
                if draw:
                    pygame.draw.rect(
                        scr, (255, 255, 255),
                        [self.left + i * self.cell_size, self.top + j * self.cell_size, self.cell_size,
                         self.cell_size], width=1
                    )
                if el:
                    if changes:
                        el.rect.x -= dx

    def get_cell(self, pos):
        if self.left <= pos[0] <= len(self.board) * self.cell_size + self.left and self.top <= pos[1] <= len(
                self.board[0]
        ) * self.cell_size + self.top:
            return (pos[1] - self.top) // self.cell_size, (pos[0] - self.left) // self.cell_size
        return None
