import os

import objects.constants
import pygame
from menus.main_menu import MainMenu
from objects.constants import FPS
from objects.functions import draw, handle_collision, reset
from objects.surfaces import Ground, Ceil
from objects.player import Player
from menus.end_menu import EndMenu

if __name__ == '__main__':
    objects.constants.init_variables()
    running = True
    screen = pygame.display.set_mode((1500, 1500 / 16 * 9), pygame.SCALED, vsync=1)
    clock = pygame.time.Clock()
    pygame.init()
    main_menu = MainMenu()
    end_menu = EndMenu()
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
    speed_group = pygame.sprite.Group()
    spike_group = pygame.sprite.Group()
    portal_group = pygame.sprite.Group()
    player = Player(player_group, mode='cube')
    os.getcwd()
    groundgroup.add(ground)
    DICT = {
        'main_menu': main_menu, 'player': player, 'player_group': player_group, 'spikegroup': spike_group,
        'groundgroup': groundgroup, 'ceil': ceil, 'blockgroup': block_group, 'speedgroup': speed_group,
        'jumppudgroup': jumppud_group, 'orbgroup': orb_group, 'coingroup': coin_group, 'portalgroup': portal_group,
        'endgroup': end_group, 'inclinedplanegroup': inclinedplanegroup, 'level_bg': bg, 'board': None,
        'resetter': lambda: reset(DICT), 'event': None, 'end_menu': end_menu
    }

    while running:
        event_list = pygame.event.get()
        for event in event_list:
            if event.type == pygame.QUIT:
                running = False
            if objects.constants.STATUS == 'MAIN':
                main_menu.handle_event(event, DICT)
            elif objects.constants.STATUS == 'END':
                end_menu.handle_event(event)
        if objects.constants.STATUS == 'GAME':
            handle_collision(
                player, dct=DICT
            )
        draw(screen, DICT)
        DICT['event'] = event_list
        pygame.display.flip()
        clock.tick(FPS)
    pygame.quit()
