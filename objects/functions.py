import csv
import os
import sys

import pygame

from objects.board import Board
from objects.constants import OFFSET, FPS, WIDTH, HEIGHT, SPEED
from objects.cube import Cube
from objects.groups import (
    PortalGroup, SpeedGroup, SpikeGroup, OrbGroup, EndGroup, CoinGroup, BlockGroup, JumppudGroup,
    PlayerGroup, DHGroup
)
from surfaces.ground import Ground


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


def load_level(
        filename, blockgroup, spikegroup, orbgroup, endgroup, jumppudgroup, DHgroup, portalgroup, coingroup,
        speedgroup, ):
    from objects.block import Block
    from objects.end import End
    with open('./' + filename) as csvfile:
        reader = list(csv.reader(csvfile, delimiter=';'))
    board = Board(0, 0)
    matrix = [[[None] for _ in range(len(reader))] for _ in range(len(reader[0]))]
    board.board = matrix
    board.set_view()
    for i, row in enumerate(reader):
        for j, el in enumerate(row):
            match el:
                case ' ':
                    board.board[j][i] = 0
                case 'b':
                    board.board[j][i] = Block(blockgroup, x=j * 64, y=i * 64 - OFFSET)
                case 'e':
                    board.board[j][i] = End(endgroup)
    return board


def run_game():
    screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.SCALED, vsync=1)
    bg = pygame.image.load('./resource/backgrounds/bg1.png')
    ground = Ground()
    player_group = PlayerGroup()
    DH_group = DHGroup()
    block_group = BlockGroup()
    jumppud_group = JumppudGroup()
    coin_group = CoinGroup()
    end_group = EndGroup()
    orb_group = OrbGroup()
    speed_group = SpeedGroup()
    spike_group = SpikeGroup()
    portal_group = PortalGroup()
    board = load_level(
        'data/levels/test.csv',
        blockgroup=block_group,
        spikegroup=spike_group,
        speedgroup=speed_group,
        orbgroup=orb_group,
        jumppudgroup=jumppud_group,
        portalgroup=portal_group,
        coingroup=coin_group,
        endgroup=end_group,
        DHgroup=DH_group
    )
    player = Cube(player_group, y=200)
    running = True
    clock = pygame.time.Clock()

    while running:
        screen.blit(bg, (0, 0))
        screen.blit(ground, [0, HEIGHT - 100])
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        board.left -= SPEED / FPS
        board.render(screen)
        block_group.draw(screen)
        player_group.update()
        player_group.draw(screen)
        clock.tick(FPS)
        pygame.display.update()
    pygame.quit()
    sys.exit()
