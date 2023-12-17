import pygame
from objects.constants import WIDTH, HEIGHT, FPS
from objects.cube import Cube
from objects.functions import load_level
from objects.groups import (
    PlayerGroup, DHGroup, BlockGroup,
    JumppudGroup, CoinGroup, EndGroup,
    OrbGroup, SpeedGroup, SpikeGroup, PortalGroup
)
from surfaces.ground import Ground


def run_game(running):
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
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
    clock = pygame.time.Clock()

    while running:
        screen.blit(bg, (0, 0))
        screen.blit(ground, [0, HEIGHT - 100])
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        board.render(screen)
        player_group.update()
        player_group.draw(screen)
        clock.tick(FPS)
        pygame.display.update()

    pygame.quit()
