import sys
import os
import pygame
from objects.board import Board
import csv


def load_image(name, colorkey=None):
    fullname = os.path.join('./resource/', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image


def load_level(filename, blockgroup, spikegroup, orbgroup, endgroup, jumppudgroup, DHgroup, portalgroup, coingroup, speedgroup, ):
    from objects.block import Block
    from objects.end import End
    with open('./' + filename) as csvfile:
        reader = list(csv.reader(csvfile, delimiter=';'))
    board = Board(0, 0)
    board.set_view(0, 0, 64)
    matrix = [[[None] for _ in range(len(reader))] for _ in range(len(reader[0]))]
    for i, row in enumerate(reader):
        for j, el in enumerate(row):
            match el:
                case ' ':
                    matrix[j][i] = 0
                case 'b':
                    matrix[j][i] = Block(blockgroup, x=i*64, y=j*64)
                case 'e':
                    matrix[j][i] = End(endgroup)
    board.board = matrix
    return board
