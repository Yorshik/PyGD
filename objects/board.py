import pygame


class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[None] * width for _ in range(height)]
        self.left = 10
        self.top = 10
        self.cell_size = 30
        self.clicked_cell = None
        self.colors = ((255, 255, 255), (255, 0, 0), (0, 0, 255))

    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def render(self, scr):
        for i, row in enumerate(self.board):
            for j, el in enumerate(row):
                pygame.draw.rect(scr, (255, 255, 255),
                                 [self.left + i * self.cell_size, self.top + j * self.cell_size, self.cell_size,
                                  self.cell_size], width=1
                                 )


    # def click_cell(self, position):
    #     self.clicked_cell = self.get_cell(position)

    def get_cell(self, pos):
        if self.left <= pos[0] <= len(self.board) * self.cell_size + self.left and self.top <= pos[1] <= len(
                self.board[0]
        ) * self.cell_size + self.top:
            return (pos[1] - self.top) // self.cell_size, (pos[0] - self.left) // self.cell_size
        return None
