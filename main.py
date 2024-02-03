import os

import pygame

import objects.constants
from menus.end_menu import EndMenu
from menus.main_menu import MainMenu
from menus.pause_menu import PauseMenu
from objects.constants import FPS
from objects.functions import draw, handle_collision, reset
from objects.label import Label
from objects.player import Player
from objects.surfaces import Ground, Ceil, NewBest

if __name__ == '__main__':
    objects.constants.init_variables()
    running = True
    screen = pygame.display.set_mode((1500, 1500 / 16 * 9), pygame.SCALED, vsync=1)
    clock = pygame.time.Clock()
    pygame.init()
    main_menu = MainMenu()
    end_menu = EndMenu()
    pause_menu = PauseMenu()
    bg = pygame.image.load(os.getcwd() + '/data/resource/backgrounds/bg1.png')
    ground = Ground()
    ceil = Ceil()
    player_group = pygame.sprite.Group()
    groundgroup = pygame.sprite.Group()
    inclinedplanegroup = pygame.sprite.Group()
    block_group = pygame.sprite.Group()
    jumppud_group = pygame.sprite.Group()
    coin_group = pygame.sprite.Group()
    end_group = pygame.sprite.Group()
    orb_group = pygame.sprite.Group()
    spike_group = pygame.sprite.Group()
    portal_group = pygame.sprite.Group()
    player = Player(player_group, mode='cube')
    groundgroup.add(ground)
    new_best = NewBest()
    DICT = {
        'main_menu': main_menu, 'player': player, 'player_group': player_group, 'spikegroup': spike_group,
        'groundgroup': groundgroup, 'ceil': ceil, 'blockgroup': block_group,
        'jumppudgroup': jumppud_group, 'orbgroup': orb_group, 'coingroup': coin_group, 'portalgroup': portal_group,
        'endgroup': end_group, 'inclinedplanegroup': inclinedplanegroup, 'level_bg': bg, 'board': None,
        'resetter': lambda: reset(DICT), 'event': None, 'end_menu': end_menu, 'pause_menu': pause_menu,
        'new_best': new_best, 'coins_coordinates': [],
        'counter': 50, 'percent': 0, 'attempts': 1,
        'attempt_label': Label('Attempt 1', (400, 300), font_size=150, font_color=(255, 255, 255)),
        'blackout': pygame.image.load('data/resource/backgrounds/blackout.png'), 'collected_coins': 0, 'max_coins': 0
    }

    while running:
        event_list = pygame.event.get()
        for event in event_list:
            if objects.constants.STATUS == 'MAIN':
                main_menu.handle_event(event, DICT)
            elif objects.constants.STATUS == 'WIN':
                end_menu.handle_event(event, DICT)
            elif objects.constants.STATUS == 'PAUSE':
                pause_menu.handle_event(event, DICT)
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    objects.constants.STATUS = 'PAUSE'
                    pygame.mixer.music.pause()
        if objects.constants.STATUS == 'GAME':
            handle_collision(
                player, dct=DICT
            )
        draw(screen, DICT)
        DICT['event'] = event_list
        pygame.display.flip()
        clock.tick(FPS)
    pygame.quit()
