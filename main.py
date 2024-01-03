import time

import objects.constants


def handle_collision(
        p, blockgroup, spikegroup, orbgroup, endgroup, jumppudgroup, DHgroup, portalgroup, coingroup,
        speedgroup, DICT):
    if lst := pygame.sprite.spritecollide(p, blockgroup, False):
        if p.mode.__class__ == Cube:
            for el in lst:
                if p.mode.rect.y + p.mode.rect.h - 10 > el.rect.y:
                    if objects.constants.STATUS != "DIED":
                        objects.constants.STATUS = 'DIED'
                        return 'DIED'
                else:
                    p.mode.vy = 0
                    p.mode.set_on_block(True)
                    p.mode.bottom_block_y = el.rect.y
        elif p.mode.__class__ == Ship:
            for el in lst:
                if p.mode.rect.y < el.rect.y and p.mode.rect.y + p.mode.rect.h + p.mode.vy - 25 < el.rect.y:
                    p.mode.bottom_block_y = el.rect.y
                    p.mode.vy = 0
                    p.mode.collide_block = True
                elif (p.mode.rect.y - p.mode.vy) - (el.rect.y + el.rect.h) < 5 and p.mode.rect.y + p.mode.rect.h > el.rect.y + el.rect.h:
                    p.mode.top_block_y = el.rect.y + el.rect.h
                    p.mode.vy = 0
                    p.mode.collide_block = True
                else:
                    objects.constants.STATUS = 'DIED'
    else:
        p.mode.bottom_block_y = None
        p.mode.top_block_y = None
        p.mode.collide_block = False
    if pygame.sprite.spritecollide(p, spikegroup, False):
        objects.constants.STATUS = "DIED"
    if pygame.sprite.spritecollide(p, orbgroup, False):
        pass
    if pygame.sprite.spritecollide(p, endgroup, False):
        objects.constants.STATUS = 'WIN'
        print('win')
    if lst := pygame.sprite.spritecollide(p, jumppudgroup, False):
        for el in lst:
            el.action(DICT)
    if pygame.sprite.spritecollide(p, DHgroup, False):
        pass
    if lst := pygame.sprite.spritecollide(p, portalgroup, False):
        for el in lst:
            el.action(DICT)
    if pygame.sprite.spritecollide(p, coingroup, False):
        pass
    if pygame.sprite.spritecollide(p, speedgroup, False):
        pass


def reset(dct):
    dct['player'].mode.rect.y = objects.constants.STARTPOSITION
    dct['board'].left = 0
    dct['board'].reset()
    for sprite in dct['portalgroup'].sprites():
        sprite.activated = False
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
    player = Player(player_group, mode='ship')

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
        if objects.constants.STATUS != 'DIED' and DICT['time'] - time.time() > 0.2:
            DICT['time'] = time.time()
        handle_collision(
            player, blockgroup=block_group, spikegroup=spike_group, speedgroup=speed_group, jumppudgroup=jumppud_group,
            coingroup=coin_group, portalgroup=portal_group, endgroup=end_group, DHgroup=DH_group, orbgroup=orb_group, DICT=DICT
        )
        draw(screen, DICT)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            main_menu.handle_event(event, DICT)
        pygame.display.flip()
        clock.tick(FPS)
    pygame.quit()
