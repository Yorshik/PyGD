import pygame

import objects.constants
from objects.buttons import Button
from objects.label import Label

objects.constants.init_variables()


class PauseMenu(pygame.surface.Surface):
    def __init__(self):
        super().__init__((objects.constants.WIDTH, int(objects.constants.HEIGHT)))
        self.music = r"data/resource/musics/menu.mp3"
        self.resume_button = Button('data/resource/images/play.png', (200, 600), self.resume, size=[100, 100])
        self.reload_button = Button('data/resource/images/reload.png', (750, 600), self.reload, size=[100, 100])
        self.exit_button = Button('data/resource/images/exit.png', (1300, 600), self.exit, size=[100, 100])
        self.main_label = Label('Project Level', (200, 150), font_size=150, font_color=[255, 255, 255])
        self.percent_label = Label('0%', (200, 300), font_size=150, font_color=[255, 255, 255])
        self.buttons = [self.resume_button, self.exit_button, self.reload_button]
        self.labels = [self.main_label, self.percent_label]
        self.all_sprites = pygame.sprite.Group()
        for button in self.buttons:
            self.all_sprites.add(button)
        for label in self.labels:
            self.all_sprites.add(label)

    def reload(self, dct):
        objects.constants.STATUS = 'GAME'
        dct['resetter']()

    def resume(self, _):
        objects.constants.STATUS = 'GAME'
        pygame.mixer.music.unpause()

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

    def handle_event(self, event, dct):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                objects.constants.STATUS = 'MAIN'
            elif event.key == pygame.K_SPACE:
                objects.constants.STATUS = 'GAME'
        for button in self.buttons:
            if button.is_clicked(event):
                button.action(dct)

    def draw(self, surface=None, dct=None):
        if surface is None:
            surface = pygame.display.get_surface()
        if int(self.percent_label.text[:-1]) < dct['percent']:
            self.percent_label.text = str(dct['percent']) + '%'
            self.percent_label.image = self.percent_label.font.render(
                self.percent_label.text, True, self.percent_label.font_color
            )
            self.percent_label.rect = self.percent_label.image.get_rect(topleft=(200, 300))
        self.fill((255, 0, 255))
        self.all_sprites.draw(surface)
