import csv
import os
import sys
import time

import pygame
from PIL import Image

import objects.constants
from objects.board import Board
from objects.constants import OFFSET, HEIGHT

objects.constants.init_status()


def load_image(name, colorkey=None):
    fullname = os.path.join('data/resource/', name)
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


def load_level(
        filename, blockgroup, spikegroup, orbgroup, endgroup, jumppudgroup, DHgroup, portalgroup, coingroup,
        speedgroup, ):
    from objects.block import Block
    from objects.end import End
    with open('./' + filename) as csvfile:
        reader = list(csv.reader(csvfile, delimiter=';'))
    music = reader.pop(0)
    pygame.mixer.music.load('data/resource\\musics\\' + music[0])
    pygame.mixer.music.play(-1)
    board = Board(0, 0)
    matrix = [[0 for _ in range(len(reader))] for _ in range(len(reader[0]))]
    board.board = matrix
    board.set_view()
    for i, row in enumerate(reader):
        for j, el in enumerate(row):
            match el:
                case '  ':
                    board.board[j][i] = 0
                case 'b ':
                    board.board[j][i] = Block(blockgroup, x=j * 64, y=i * 64 - OFFSET)
                case 'e ':
                    board.board[j][i] = End(endgroup, x=j * 64, y=i * 64 - OFFSET)
    return board


# Обрезка объектов
def crop_image(name, x, y, size):
    fullname = os.path.join('./resource/icons/', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = Image.open(fullname)
    texture = image.crop((x, y, x + size, y + size))
    return texture


# Конвертирование картинки из pil в pygame
def convert(pil_image):
    pil_image = pil_image.convert('RGBA')
    image_data = pil_image.tobytes('raw', 'RGBA')
    width, height = pil_image.size
    return pygame.image.fromstring(image_data, (width, height), 'RGBA')


def draw(scr: pygame.Surface, dct):
    match objects.constants.STATUS:
        case 'MAIN':
            dct['main_menu'].draw(scr)
        case 'GAME':
            scr.blit(dct['level_bg'], (0, 0))
            scr.blit(dct['ground'], [0, HEIGHT - 100])
            dct['board'].render(scr)
            dct['blockgroup'].draw(scr)
            dct['player_group'].update()
            dct['player_group'].draw(scr)
        case 'DIED':
            pygame.mixer.music.stop()
            time.sleep(1)
            dct['resetter']()
        case 'WIN':
            scr.blit(dct['level_bg'], (0, 0))
            scr.blit(dct['ground'], [0, HEIGHT - 100])
            dct['board'].render(scr, changes=False)
            dct['blockgroup'].draw(scr)
            dct['player_group'].update()
            dct['player_group'].draw(scr)
            # TODO add drawing end menu
        case Err:
            raise Exception(Err + ' Something went wrong')
