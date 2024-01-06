import sys
import time

import pygame

import objects.constants
from objects.buttons import Button
from objects.functions import load_level, reset
from objects.label import Label

objects.constants.init_variables()


class MainMenu(pygame.surface.Surface):
    def __init__(self):
        super().__init__((1500, int(1500 / 16 * 9)))

        background = pygame.image.load("data/resource/backgrounds/bg1.png")
        self.background = pygame.transform.scale(background, (1500, int(1500 / 16 * 9)))
        self.image = pygame.surface.Surface((1500, int(1500 / 16 * 9)))
        self.rect = self.image.get_rect()

        self.all_sprites = pygame.sprite.Group()

        self.music_image = Button("data/resource/images/GJ_music_on.png", (20, 510), self.toggle_music, (80, 80))
        self.settings_button = Button("data/resource/images/GJ_settings.png", (700, 10), self.settings, (80, 80))

        self.buttons = [
            Button("data/resource/images/GJ_play_btn.png", (220, 280), self.start_game, (150, 150)),
            Button("data/resource/images/GJ_profile.png", (410, 280), self.profile, (150, 150)),
            Button("data/resource/images/GJ_exit.png", (20, 10), sys.exit, (80, 80)),
            self.settings_button,
            self.music_image
        ]

        self.button_clicked = False
        self.name_label = Label("PyDG ", (300, 150), font_size=100)

        for button in self.buttons:
            self.all_sprites.add(button)

        self.all_sprites.add(self.name_label)

        self.music = r"data/resource/musics/menu.mp3"
        pygame.mixer.init()
        pygame.mixer.music.load(self.music)
        pygame.mixer.music.set_volume(0.1)  # Устанавливаем начальную громкость
        pygame.mixer.music.play(-1)

    def start_game(self, dct):
        dct['board'] = load_level(
            'data\\levels\\test.csv',
            dct['blockgroup'],
            dct['spikegroup'],
            dct['orbgroup'],
            dct['endgroup'],
            dct['jumppudgroup'],
            dct['DHgroup'],
            dct['portalgroup'],
            dct['coingroup'],
            dct['speedgroup']
        )
        reset(dct)
        time.sleep(0.3)

    def profile(self):
        pass

    def toggle_music(self):
        if pygame.mixer.music.get_volume() == 0.0:
            self.all_sprites.remove(self.music_image)
            self.music_image = Button(r"resource\images\GJ_music_on.png", (20, 510), self.toggle_music, (80, 80))
            self.all_sprites.add(self.music_image)
            pygame.mixer.music.set_volume(0.1)  # Восстанавливаем начальную громкость
        else:
            self.all_sprites.remove(self.music_image)
            self.music_image = Button(r"resource\images\GJ_music_off.png", (20, 510), self.toggle_music, (80, 80))
            self.all_sprites.add(self.music_image)
            pygame.mixer.music.set_volume(0.0)  # Устанавливаем громкость на 0 (выключаем звук)
        self.draw()

    def settings(self):
        pass

    def handle_event(self, event, dct):
        for button in self.buttons:
            if button.is_clicked(event):
                button.action(dct)

    def draw(self, surface=None):
        if surface is None:
            surface = pygame.display.get_surface()
        self.fill((255, 255, 255))
        self.image.fill((255, 255, 255))
        self.all_sprites.draw(self.image)
        surface.blit(self.background, (0, 0))
        surface.blit(self.image, (0, 0))
