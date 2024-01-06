import objects.constants

if __name__ == '__main__':
    from menus.main_menu import MainMenu
    from objects.constants import FPS
    from objects.functions import draw, handle_collision, reset
    from objects.ground import Ground
    from objects.groups import *

    objects.constants.init_variables()
    running = True
    screen = pygame.display.set_mode((1500, 1500 / 16 * 9), pygame.SCALED, vsync=1)
    from objects.player import Player

    clock = pygame.time.Clock()
    pygame.init()
    main_menu = MainMenu()
    bg = pygame.image.load('data/resource/backgrounds/bg1.png')
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
    player = Player(player_group, mode='wave')

    DICT = {
        'main_menu': main_menu, 'player': player, 'player_group': player_group, 'spikegroup': spike_group,
        'ground': ground, 'blockgroup': block_group, 'speedgroup': speed_group, 'jumppudgroup': jumppud_group,
        'orbgroup': orb_group, 'coingroup': coin_group, 'portalgroup': portal_group, 'endgroup': end_group,
        'DHgroup': DH_group, 'level_bg': bg, 'board': None, 'resetter': lambda: reset(DICT), 'status': 'MAIN'
    }
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            main_menu.handle_event(event, DICT)
        handle_collision(
            player, DICT=DICT
        )
        draw(screen, DICT)
        pygame.display.flip()
        clock.tick(FPS)
    pygame.quit()
