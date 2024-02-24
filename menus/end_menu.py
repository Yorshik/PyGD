import pygame.surface

import objects.constants
from objects.buttons import Button
from objects.label import Label

objects.constants.init_variables()


class EndMenu(pygame.surface.Surface):
    def __init__(self):
        super().__init__((800, 600))
        self.coins = []
        self.coin = pygame.sprite.Sprite()
        self.coin.image = pygame.image.load('data/resource/blocks/coin.png')
        self.coin.rect = self.coin.image.get_rect()
        self.not_collected_coin = pygame.sprite.Sprite()
        self.not_collected_coin.image = pygame.image.load('data/resource/blocks/not_collected_coin.png')
        self.not_collected_coin.rect = self.not_collected_coin.image.get_rect()
        self.music = r"data/resource/musics/menu.mp3"
        self.background = pygame.transform.scale(pygame.image.load("data/resource/backgrounds/end.jpg"), (800, 600))
        self.image = pygame.surface.Surface((800, 600))
        self.rect = self.image.get_rect()
        self.main_label = Label('Level Completed', (400, 150), font_size=120, font_color=(0, 255, 0))
        self.orbs_label = Label('100 orbs', (400, 220), font_size=100, font_color=(0, 0, 255))
        self.stars_label = Label('10 stars', (400, 290), font_size=100, font_color=(255, 255, 0))
        self.attempts_label = Label('', (400, 360), font_size=100, font_color=(255, 255, 255))
        self.all_sprites = pygame.sprite.Group()
        self.exit_button = Button('data/resource/images/exit.png', (950, 500), self.exit, (100, 100))
        self.reload_button = Button('data/resource/images/reload.png', (450, 500), self.reload, (100, 100))
        self.buttons = [self.exit_button, self.reload_button]
        self.labels = [self.main_label, self.orbs_label, self.stars_label, self.attempts_label]
        for button in self.buttons:
            self.all_sprites.add(button)
        for button in self.labels:
            self.all_sprites.add(button)

    def update(self, attempts, coins):
        self.attempts_label.text = f'attempts: {attempts}'
        self.attempts_label.image = self.attempts_label.font.render(
            self.attempts_label.text, True, self.attempts_label.font_color
            )
        self.attempts_label.rect = self.image.get_rect(topleft=(400, 360))
        for i in range(coins):
            self.all_sprites.remove(self.coins[i])
            x, y = self.coins[i].rect.x, self.coins[i].rect.y
            self.coins[i] = self.coin
            self.coins[i].rect.x = x
            self.coins[i].rect.y = y
            self.all_sprites.add(self.coins[i])

    def set_coins(self, amount):
        for i in range(amount):
            self.coins.append(self.not_collected_coin)
            self.coins[-1].rect.x = 700 + 100 * i
            self.coins[-1].rect.y = 500
            self.all_sprites.add(self.coins[-1])
        print(self.coins)

    def exit(self, dct):
        objects.constants.STATUS = 'MAIN'
        pygame.mixer.music.load(self.music)
        pygame.mixer.music.set_volume(0.1)  # Устанавливаем начальную громкость
        pygame.mixer.music.play(-1)
        dct['coingroup'] = pygame.sprite.Group()
        dct['spikegroup'] = pygame.sprite.Group()
        dct['blockgroup'] = pygame.sprite.Group()
        dct['inclinedplanegroup'] = pygame.sprite.Group()
        dct['portalgroup'] = pygame.sprite.Group()
        dct['orbgroup'] = pygame.sprite.Group()
        dct['jumppudgroup'] = pygame.sprite.Group()
        dct['endgroup'] = pygame.sprite.Group()

    def reload(self, dct):
        objects.constants.STATUS = 'GAME'
        dct['resetter']()

    def handle_event(self, event, dct):
        for button in self.buttons:
            if button.is_clicked(event):
                button.action(dct)

    def draw(self, surface=None):
        if surface is None:
            surface = pygame.display.get_surface()
        surface.blit(self.background, (350, 110))
        self.fill((255, 0, 255))
        self.image.fill((255, 255, 255))
        self.all_sprites.draw(surface)
