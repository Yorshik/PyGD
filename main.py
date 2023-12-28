import time

import objects.constants


def handle_collision(
        p, blockgroup, spikegroup, orbgroup, endgroup, jumppudgroup, DHgroup, portalgroup, coingroup,
        speedgroup, ):
    if lst := pygame.sprite.spritecollide(p, blockgroup, False):
        if p.__class__ == Cube:
            for el in lst:
                if p.rect.y + p.rect.h - 10 > el.rect.y:
                    if objects.constants.STATUS != "DIED":
                        objects.constants.STATUS = 'DIED'
                        return 'DIED'
                else:
                    p.vy = 0
                    p.set_on_block(True)
                    p.block_y = el.rect.y
        elif p.__class__ == Ship:
            for el in lst:
                if p.rect.y < el.rect.y and p.rect.y + p.rect.h + p.vy - 25 < el.rect.y:
                    p.bottom_block_y = el.rect.y
                    p.vy = 0
                    p.collide_block = True
                elif (p.rect.y - p.vy) - (el.rect.y + el.rect.h) < 5 and p.rect.y + p.rect.h > el.rect.y + el.rect.h:
                    p.top_block_y = el.rect.y + el.rect.h
                    p.vy = 0
                    p.collide_block = True
                else:
                    objects.constants.STATUS = 'DIED'
    else:
        p.bottom_block_y = None
        p.top_block_y = None
        p.collide_block = False
    if pygame.sprite.spritecollide(p, spikegroup, False):
        objects.constants.STATUS = "DIED"
    if pygame.sprite.spritecollide(p, orbgroup, False):
        pass
    if pygame.sprite.spritecollide(p, endgroup, False):
        objects.constants.STATUS = 'WIN'
        print('win')
    if pygame.sprite.spritecollide(p, jumppudgroup, False):
        pass
    if pygame.sprite.spritecollide(p, DHgroup, False):
        pass
    if pygame.sprite.spritecollide(p, portalgroup, False):
        pass
    if pygame.sprite.spritecollide(p, coingroup, False):
        pass
    if pygame.sprite.spritecollide(p, speedgroup, False):
        pass


def reset(dct):
    dct['player'].rect.y = 1500 / 16 * 9 - 200
    dct['board'].left = 0
    dct['board'].reset()
    pygame.mixer.music.play(-1)
    objects.constants.STATUS = 'GAME'


if __name__ == '__main__':
    from menus.main_menu import MainMenu
    from objects.constants import FPS
    from objects.cube import Cube
    from objects.ship import Ship
    from objects.functions import draw
    from objects.ground import Ground
    from objects.groups import *

    objects.constants.init_status()
    running = True
    screen = pygame.display.set_mode((1500, 1500 / 16 * 9), pygame.SCALED, vsync=1)
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
    player = Ship(player_group, y=1500 / 16 * 9 - 150)

    DICT = {
        'main_menu': main_menu,
        'player': player,
        'player_group': player_group,
        'spikegroup': spike_group,
        'ground': ground,
        'blockgroup': block_group,
        'speedgroup': speed_group,
        'jumppudgroup': jumppud_group,
        'orbgroup': orb_group,
        'coingroup': coin_group,
        'portalgroup': portal_group,
        'endgroup': end_group,
        'DHgroup': DH_group,
        'level_bg': bg,
        'board': None,
        'time': time.time(),
        'resetter': lambda: reset(DICT),
        'status': 'MAIN'
    }
    while running:
        # if objects.constants.STATUS != 'DIED':
        #     DICT['time'] = time.time()
        handle_collision(
            player, blockgroup=block_group, spikegroup=spike_group, speedgroup=speed_group, jumppudgroup=jumppud_group,
            coingroup=coin_group, portalgroup=portal_group, endgroup=end_group, DHgroup=DH_group, orbgroup=orb_group
        )
        draw(screen, DICT)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            main_menu.handle_event(event, DICT)
        pygame.display.flip()
        clock.tick(FPS)
    pygame.quit()
