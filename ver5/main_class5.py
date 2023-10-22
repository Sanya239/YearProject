import pygame
import os
import ver5.menu5 as menu
import ver5.multy_mode5 as multy_mode
import ver5.single_mode5 as single_mode
import ver5.settings as settings
import ver5.elements.parameters_box_class5 as parameters_box_class

FPS = 30


class app():
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 800))
        pygame.display.set_caption('нарды ахах')
        self.clock = pygame.time.Clock()
        self.sprites = []
        self.mode = 0
        self.auto = False
        self.menu = menu.main_menu(self)
        self.multy = multy_mode.multy_game(self)
        self.single = single_mode.single_game(self)
        self.settings = settings.Settings(self)
        # self.menu.screen = self.screen
        self.running = True
        self.events = []

    def set_mode1(self):
        self.mode = 1
        self.menu.buttons.draw(self.screen)
        pygame.display.flip()
        self.menu.multy_play_buttonimage = self.menu.single_play_button.button_unclicked
        self.multy.menu_button.image = self.single.menu_button.button_unclicked
        self.multy.starting_position()
        pygame.time.delay(150)
        pygame.display.flip()
        self.auto = True

    def set_mode2(self):
        self.mode = 2
        self.menu.buttons.draw(self.screen)
        pygame.display.flip()
        self.menu.single_play_button.image = self.menu.single_play_button.button_unclicked
        self.single.menu_button.image = self.single.menu_button.button_unclicked
        self.single.restart()
        pygame.time.delay(150)
        pygame.display.flip()
        self.auto = True

    def set_mode3(self):
        self.menu.buttons.draw(self.screen)
        self.menu.settings_button.image = self.menu.settings_button.button_unclicked
        self.settings.menu_button.image = self.single.menu_button.button_unclicked
        self.mode = 3
        pygame.display.flip()
        pygame.time.delay(150)
        self.settings.settings_redraw()

    def update(self):
        self.events = []
        for event in pygame.event.get():
            self.events.append(event)
            # проверить закрытие окна
            if event.type == pygame.QUIT:
                self.running = False
                parameters_box_class.Parameters_box.file_rewrite()

        need_animation = True
        for event in self.events:
            need_animation = False
            if self.mode == 0:
                self.menu.update(event)
                self.clock.tick(FPS)

            elif self.mode == 1:

                self.multy.update(event)
                self.auto = self.multy.auto

            elif self.mode == 2:

                self.single.update(event)
                self.auto = self.single.auto

            elif self.mode == 3:
                self.settings.update(event)
        if self.auto == True and need_animation:
            if self.mode == 1:
                self.multy.update(None)
                self.auto = self.multy.auto

            if self.mode == 2:
                self.single.update(None)
                self.auto = self.single.auto
        pygame.display.flip()
        self.clock.tick(30)


product = app()

while product.running:
    product.update()
