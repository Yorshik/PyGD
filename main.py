# from objects.constants import STATUS
import objects.constants

if __name__ == '__main__':
    from menus.main_menu import MainMenu
    from objects.constants import FPS
    from objects.cube import Cube
    from objects.functions import draw, load_level
    from objects.ground import Ground
    from objects.groups import *
    objects.constants.init_status()
    running = True
    screen = pygame.display.set_mode((1500, 1500/16*9), pygame.SCALED, vsync=1)
    clock = pygame.time.Clock()
    pygame.init()
    main_menu = MainMenu()
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
    player = Cube(player_group, y=1500/16*9-150)

    DICT = {
        'main_menu': main_menu,
        'player': player,
        'player_group': player_group,
        'spike_group': spike_group,
        'ground': ground,
        'block_group': block_group,
        'speedgroup': speed_group,
        'jumppudgroup': jumppud_group,
        'coingroup': coin_group,
        'portalgroup': portal_group,
        'endgroup': end_group,
        'DHgroup': DH_group,
        'level_bg': bg,
        'board': board
    }
    while running:
        draw(screen, DICT)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            main_menu.handle_event(event)
        # screen.blit(main_menu, (0,0))
        pygame.display.flip()
        clock.tick(FPS)
    pygame.quit()
