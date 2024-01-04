import csv
import os
import sys
import time

import pygame
from PIL import Image

import objects.constants
from objects.board import Board
from objects.constants import OFFSET, HEIGHT, LEFTBUTTON

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
        speedgroup
):
    from objects.block import Block
    from objects.end import End
    from objects.portals import Portal
    from objects.jumppuds import Jumppud
    from objects.orb import Orb
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
                    board.board[j][i] = Block(blockgroup, x=j * 64, y=i * 64 - OFFSET + 1)
                case 'e ':
                    board.board[j][i] = End(endgroup, x=j * 64, y=i * 64 - OFFSET)
                case 'sp':
                    board.board[j][i] = Portal(portalgroup, t='to_ship', x=j * 64, y=i * 64 - OFFSET - 32)
                case 'cp':
                    board.board[j][i] = Portal(portalgroup, t='to_cube', x=j * 64, y=i * 64 - OFFSET - 32)
                case 'pj':
                    board.board[j][i] = Jumppud(jumppudgroup, var='purple', x=j * 64, y=i * 64 - OFFSET + (64 - 12))
                case 'rj':
                    board.board[j][i] = Jumppud(jumppudgroup, var='red', x=j * 64, y=i * 64 - OFFSET + (64 - 15))
                case 'yj':
                    board.board[j][i] = Jumppud(jumppudgroup, var='yellow', x=j * 64, y=i * 64 - OFFSET + (64 - 10))
                case 'yo':
                    board.board[j][i] = Orb(orbgroup, x=j * 64, y=i * 64 - OFFSET, t='yellow')
                case 'ro':
                    board.board[j][i] = Orb(orbgroup, x=j * 64, y=i * 64 - OFFSET, t='red')
                case 'bo':
                    board.board[j][i] = Orb(orbgroup, x=j * 64, y=i * 64 - OFFSET, t='black')
                case 'po':
                    board.board[j][i] = Orb(orbgroup, x=j * 64, y=i * 64 - OFFSET, t='purple')
    return board


def handle_collision(p, DICT):
    from objects.cube import Cube
    from objects.ship import Ship
    if lst := pygame.sprite.spritecollide(p, DICT['blockgroup'], False):
        if p.mode.__class__ == Cube:
            for el in lst:
                if p.mode.rect.y + p.mode.rect.h - 10 > el.rect.y:
                    objects.constants.STATUS = 'DIED'
                else:
                    p.mode.vy = 0
                    p.mode.collide_block = True
                    p.mode.bottom_block_y = el.rect.y
        elif p.mode.__class__ == Ship:
            for el in lst:
                if p.mode.rect.y < el.rect.y and p.mode.rect.y + p.mode.rect.h + p.mode.vy - 15 < el.rect.y:
                    p.mode.bottom_block_y = el.rect.y
                    p.mode.vy = 0
                    p.mode.collide_block = True
                elif (p.mode.rect.y - p.mode.vy) - (
                        el.rect.y + el.rect.h) < 5 and p.mode.rect.y + p.mode.rect.h > el.rect.y + el.rect.h:
                    p.mode.top_block_y = el.rect.y + el.rect.h
                    p.mode.vy = 0
                    p.mode.collide_block = True
                else:
                    objects.constants.STATUS = 'DIED'
    else:
        p.mode.bottom_block_y = None
        p.mode.top_block_y = None
        p.mode.collide_block = False
    if pygame.sprite.spritecollide(p, DICT['spikegroup'], False):
        objects.constants.STATUS = "DIED"
    if lst := pygame.sprite.spritecollide(p, DICT['orbgroup'], False):
        keys = pygame.key.get_pressed()
        mouse = pygame.mouse.get_pressed()
        for el in lst:
            if pygame.sprite.collide_rect(p, el):
                if mouse[LEFTBUTTON - 1] or keys[pygame.K_SPACE] or keys[pygame.K_UP]:
                    el.action(DICT)
    if pygame.sprite.spritecollide(p, DICT['endgroup'], False):
        objects.constants.STATUS = 'WIN'
        print('win')
    if lst := pygame.sprite.spritecollide(p, DICT['jumppudgroup'], False):
        for el in lst:
            el.action(DICT)
    if pygame.sprite.spritecollide(p, DICT['DHgroup'], False):
        pass
    if lst := pygame.sprite.spritecollide(p, DICT['portalgroup'], False):
        for el in lst:
            el.action(DICT)
    if pygame.sprite.spritecollide(p, DICT['coingroup'], False):
        pass
    if pygame.sprite.spritecollide(p, DICT['speedgroup'], False):
        pass


def reset(dct):
    dct['player'].mode.rect.y = objects.constants.STARTPOSITION
    dct['board'].left = 0
    dct['board'].reset()
    for sprite in dct['portalgroup'].sprites() + dct['orbgroup'].sprites() + dct['jumppudgroup'].sprites():
        sprite.activated = False
    pygame.mixer.music.play(-1)
    objects.constants.STATUS = 'GAME'


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
            dct['portalgroup'].draw(scr)
            dct['jumppudgroup'].draw(scr)
            dct['orbgroup'].draw(scr)
            dct['player_group'].update()
            dct['player_group'].draw(scr)
        case 'DIED':
            pygame.mixer.music.stop()
            time.sleep(0.5)
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
