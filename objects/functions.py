import csv
import os
import sys
import time

import pygame
from PIL import Image

import objects.constants
from objects.board import Board
from objects.constants import LEFTBUTTON, WIDTH

objects.constants.init_variables()


def load_image(name, colorkey=None):
    print(os.getcwd())
    image = pygame.image.load(os.getcwd() + '\\data\\resource\\' + name)
    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image


def load_level(
        filename, blockgroup, spikegroup, orbgroup, endgroup, jumppudgroup, portalgroup, inclinedplanegroup
):
    from objects.block import Block
    from objects.end import End
    from objects.portals import Portal
    from objects.jumppuds import Jumppud
    from objects.orb import Orb
    from objects.spike import Spike
    from objects.inclined_plane import InclinedPlane
    with open(os.getcwd() + '/' + filename) as csvfile:
        reader = list(csv.reader(csvfile, delimiter=';'))
    music = reader.pop(0)
    gamemode = reader.pop(0)[0]
    pygame.mixer.music.load(os.getcwd() + '/data/resource/musics/' + music[0])
    pygame.mixer.music.play(-1)
    board = Board(0, 0)
    board.start = gamemode
    board.left = 320
    board.board = [[0 for _ in range(len(reader))] for _ in range(len(reader[0]))]
    board.set_view()
    for i, col in enumerate(reader):
        for j, el in enumerate(col):
            match el:
                case '  ':
                    board.board[j][i] = 0
                case 'vb':
                    board.board[j][i] = Block(blockgroup, x=j * 64 + 320, y=i * 64 + int(board.top) - 1)
                case 'e ':
                    board.board[j][i] = End(endgroup, x=j * 64 + 320, y=i * 64 + int(board.top) - 1)
                case 'vp':
                    board.board[j][i] = Portal(portalgroup, t='to_ship', x=j * 64 + 320, y=i * 64 - 32 + int(board.top) - 1)
                case 'cp':
                    board.board[j][i] = Portal(portalgroup, t='to_cube', x=j * 64 + 320, y=i * 64 - 32 + int(board.top) - 1)
                case 'wp':
                    board.board[j][i] = Portal(portalgroup, t='to_wave', x=j * 64 + 320, y=i * 64 - 32 + int(board.top) - 1)
                # case 'bp':
                #     board.board[j][i] = Portal(portalgroup, t='to_ball', x=j * 64, y=i * 64 - 32 + int(board.top) - 1)
                # case 'sp':
                #     board.board[j][i] = Portal(portalgroup, t='to_spider', x=j * 64, y=i * 64 - 32 + int(board.top) - 1)
                # case 'up':
                #     board.board[j][i] = Portal(portalgroup, t='to_ufo', x=j * 64, y=i * 64 - 32 + int(board.top) - 1)
                case 'op':
                    board.board[j][i] = Portal(portalgroup, t='to_opposite_gravity', x=j * 64 + 320, y=i * 64 - 32 + int(board.top) - 1)
                case 'np':
                    board.board[j][i] = Portal(portalgroup, t='to_normal_gravity', x=j * 64 + 320, y=i * 64 - 32 + int(board.top) - 1)
                case 'pj':
                    board.board[j][i] = Jumppud(
                        jumppudgroup, var='purple', x=j * 64 + 320, y=i * 64 + (64 - 12) + int(board.top) - 1
                        )
                case 'rj':
                    board.board[j][i] = Jumppud(
                        jumppudgroup, var='red', x=j * 64 + 320, y=i * 64 + (64 - 15) + int(board.top) - 1
                        )
                case 'yj':
                    board.board[j][i] = Jumppud(
                        jumppudgroup, var='yellow', x=j * 64 + 320, y=i * 64 + (64 - 10) + int(board.top) - 1
                        )
                case 'bj':
                    board.board[j][i] = Jumppud(jumppudgroup, var='blue', x=j * 64,
                                                y=i * 64 + 320 + (64 - 14) + int(board.top) - 1)
                case 'yo':
                    board.board[j][i] = Orb(orbgroup, x=j * 64 + 320, y=i * 64 + int(board.top) - 1, t='yellow')
                case 'ro':
                    board.board[j][i] = Orb(orbgroup, x=j * 64 + 320, y=i * 64 + int(board.top) - 1, t='red')
                case 'bo':
                    board.board[j][i] = Orb(orbgroup, x=j * 64 + 320, y=i * 64 + int(board.top) - 1, t='black')
                case 'po':
                    board.board[j][i] = Orb(orbgroup, x=j * 64 + 320, y=i * 64 + int(board.top) - 1, t='purple')
                case 'so':
                    board.board[j][i] = Orb(orbgroup, x=j * 64 + 320, y=i * 64 + int(board.top) - 1, t='blue')
                case 'go':
                    board.board[j][i] = Orb(orbgroup, x=j * 64 + 320, y=i * 64 + int(board.top) - 1, t='green')
                case 'sa':
                    board.board[j][i] = Spike(spikegroup, x=j * 64 + 320, y=i * 64 + int(board.top) - 1, a=0)
                case 'sb':
                    board.board[j][i] = Spike(spikegroup, x=j * 64 + 320, y=i * 64 + int(board.top) - 1, a=90)
                case 'sc':
                    board.board[j][i] = Spike(spikegroup, x=j * 64 + 320, y=i * 64 + int(board.top) - 1, a=180)
                case 'sd':
                    board.board[j][i] = Spike(spikegroup, x=j * 64 + 320, y=i * 64 + int(board.top) - 1, a=270)
                case 'ia':
                    board.board[j][i] = InclinedPlane(inclinedplanegroup, x=j*64 + 320, y=i*64 + int(board.top) - 1, a=0)
                case 'ib':
                    board.board[j][i] = InclinedPlane(inclinedplanegroup, x=j * 64 + 320, y=i * 64 + int(board.top) - 1, a=90)
                case 'ic':
                    board.board[j][i] = InclinedPlane(inclinedplanegroup, x=j*64 + 320, y=i*64 + int(board.top) - 1, a=180)
                case 'id':
                    board.board[j][i] = InclinedPlane(inclinedplanegroup, x=j*64 + 320, y=i*64 + int(board.top) - 1, a=270)
    return board


def handle_collision(p, dct):
    from objects.cube import Cube
    from objects.ship import Ship
    from objects.wave import Wave
    if pygame.sprite.spritecollide(p, dct['groundgroup'], False):
        if p.mode.gravity == -1:
            objects.constants.STATUS = 'DIED'
        else:
            p.mode.vy = 0
            p.mode.on_ground = True
            p.mode.rect.y = dct['groundgroup'].sprites()[0].rect.y - 63
    else:
        p.mode.on_ground = False
    if lst := pygame.sprite.spritecollide(p, dct['blockgroup'], False):
        if p.mode.__class__ == Cube:
            if p.mode.gravity == 1:
                for el in lst:
                    if p.mode.rect.y + p.mode.rect.h - 10 > el.rect.y:
                        objects.constants.STATUS = 'DIED'
                    else:
                        p.mode.vy = 0
                        p.mode.collide_block = True
                        p.mode.bottom_block_y = el.rect.y
            else:
                for el in lst:
                    if p.mode.rect.y + 10 < el.rect.y + el.rect.h:
                        objects.constants.STATUS = 'DIED'
                    else:
                        p.mode.vy = 0
                        p.mode.collide_block = True
                        p.mode.bottom_block_y = el.rect.y + el.rect.h
        elif p.mode.__class__ == Ship:
            if p.mode.gravity == 1:
                for el in lst:
                    if p.mode.on_ground:
                        objects.constants.STATUS = 'DIED'
                    elif p.mode.rect.y < el.rect.y and p.mode.rect.y + p.mode.rect.h - 10 < el.rect.y:
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
                for el in lst:
                    if el.rect.y + el.rect.h - 10 < p.mode.rect.y < el.rect.y + el.rect.h:
                        p.mode.bottom_block_y = el.rect.y + el.rect.h
                        p.mode.vy = 0
                        p.mode.collide_block = True
                    elif el.rect.y < p.mode.rect.y + p.mode.rect.h < el.rect.y + el.rect.h + 10:
                        p.mode.top_block_y = el.rect.y - 1
                        p.mode.vy = 0
                        p.mode.collide_block = True
                    else:
                        objects.constants.STATUS = 'DIED'
        elif p.mode.__class__ == Wave:
            objects.constants.STATUS = 'DIED'
    else:
        p.mode.bottom_block_y = None
        p.mode.top_block_y = None
        p.mode.collide_block = False
    if lst := pygame.sprite.spritecollide(p, dct['spikegroup'], False):
        for el in lst:
            if p.mode.rect.colliderect(pygame.rect.Rect(el.rect.x + 20, el.rect.y + 23, 24, 39)):
                objects.constants.STATUS = "DIED"
                break
    if lst := pygame.sprite.spritecollide(p, dct['orbgroup'], False):
        mouse = pygame.mouse.get_pressed()
        keys = pygame.key.get_pressed()
        if mouse[LEFTBUTTON - 1] or keys[pygame.K_SPACE] or keys[pygame.K_UP]:
            lst[0].action(dct)
        # for el in dct['event']:
        #     if el.type == pygame.MOUSEBUTTONDOWN:
        #         if el.button == LEFTBUTTON:
        #             lst[0].action(dct)
        #             break
        #     elif el.type == pygame.KEYDOWN:
        #         if el.key == pygame.K_SPACE or el.key == pygame.K_UP:
        #             lst[0].action(dct)
        #             break
    if pygame.sprite.spritecollide(p, dct['endgroup'], False):
        objects.constants.STATUS = 'WIN'
        print('win')
    if lst := pygame.sprite.spritecollide(p, dct['jumppudgroup'], False):
        for el in lst:
            el.action(dct)
    if lst := pygame.sprite.spritecollide(p, dct['inclinedplanegroup'], False):
        # added only for good wave passages
        for el in lst:
            if pygame.sprite.collide_mask(p, el):
                objects.constants.STATUS = 'DIED'
                break
    if lst := pygame.sprite.spritecollide(p, dct['portalgroup'], False):
        for el in lst:
            el.action(dct)
    if pygame.sprite.spritecollide(p, dct['coingroup'], False):
        pass
    if pygame.sprite.spritecollide(p, dct['speedgroup'], False):
        pass


def reset(dct):
    dct['player'].mode.rect.y = objects.constants.STARTPOSITION
    dct['player'].mode.vy = 0
    dct['player'].mode.gravity = 1
    dct['board'].left = 320
    dct['board'].reset()
    dct['player'].mode = dct['player'].change_mode(dct['board'].start)
    dct['player'].mode.image = dct['player'].cube.orig
    for sprite in dct['portalgroup'].sprites() + dct['jumppudgroup'].sprites():
        sprite.activated = False
    pygame.mixer.music.play(-1)
    objects.constants.STATUS = 'GAME'


# Обрезка объектов
def crop_image(name, x, y, size):
    fullname = os.path.join(os.getcwd() + '\\resource/icons/', name)
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
            dct['board'].render(scr)
            dct['groundgroup'].sprites()[0].rect.y = dct['board'].top + len(dct['board'].board[0]) * 64
            dct['groundgroup'].draw(scr)
            match dct['player'].mode.name:
                case 'Ship' | 'Wave':
                    scr.blit(dct['ceil'], pygame.rect.Rect(0, 0, WIDTH, objects.constants.SHIP_WAVE_CEIL))
            dct['blockgroup'].draw(scr)
            dct['inclinedplanegroup'].draw(scr)
            dct['spikegroup'].draw(scr)
            dct['portalgroup'].draw(scr)
            dct['jumppudgroup'].draw(scr)
            dct['orbgroup'].draw(scr)
            dct['player_group'].update(dct)
            dct['player_group'].draw(scr)
        case 'DIED':
            pygame.mixer.music.stop()
            time.sleep(0.5)
            dct['resetter']()
        case 'WIN':
            scr.blit(dct['level_bg'], (0, 0))
            dct['board'].render(scr, changes=False)
            dct['groundgroup'].sprites()[0].rect.y = dct['board'].top + len(dct['board'].board[0]) * 64
            dct['groundgroup'].draw(scr)
            match dct['player'].mode.name:
                case 'Ship' | 'Wave':
                    scr.blit(dct['ceil'], pygame.rect.Rect(0, 0, WIDTH, objects.constants.SHIP_WAVE_CEIL))
            dct['blockgroup'].draw(scr)
            dct['player_group'].update()
            dct['player_group'].draw(scr)
            dct['end_menu'].draw(scr)
        case Err:
            raise Exception(Err + ' Something went wrong')
