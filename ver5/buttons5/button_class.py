import pygame
import os
import time

game_folder = os.path.dirname(__file__)


class button(pygame.sprite.Sprite):
    def __init__(self, position=(0, 0), text= '',func=print):
        pygame.sprite.Sprite.__init__(self)
        self.working = True
        self.func = func
        self.button_unclicked = pygame.image.load(os.path.join(game_folder, 'button_unclicked.png'))
        self.button_clicked = pygame.transform.flip(self.button_unclicked, False, True)
        self.image = self.button_unclicked
        self.rect = self.image.get_rect()
        self.rect.center = position

        pygame.font.init()
        self.font = pygame.font.Font(None, int(self.rect.height*0.60))
        self.text = self.font.render(text, True, (0, 0, 0))

        self.button_unclicked.set_colorkey((255, 255, 255))
        self.button_unclicked.blit(self.text,
                                   (int((self.rect.width-self.text.get_rect().width)/2),int((self.rect.height-self.text.get_rect().height)/2)))

        self.text = self.font.render(text, True, (254, 254, 254))
        self.button_clicked.set_colorkey((255, 255, 255))
        self.button_clicked.blit(self.text,
                                   (int((self.rect.width - self.text.get_rect().width) / 2),
                                    int((self.rect.height - self.text.get_rect().height) / 2)))

        self.invisible_button = pygame.image.load(os.path.join(game_folder, 'invisible_button.bmp')).convert()
        self.invisible_button.set_colorkey((0, 0, 0))



        self.message = False
        # self.rect.center = (WIDTH / 2, HEIGHT / 2)
        self.animation_tick = 0
        self.image = self.button_unclicked

    def update(self, event):


        if event.type == pygame.MOUSEBUTTONDOWN and self.working:
            if (pygame.mouse.get_pos()[0] > self.rect.left and
                    pygame.mouse.get_pos()[0] < self.rect.right and
                    pygame.mouse.get_pos()[1] < self.rect.bottom and
                    pygame.mouse.get_pos()[1] > self.rect.bottom - self.rect.height):

                self.image = self.button_clicked

                self.message = True
                self.func()
        elif event.type == pygame.MOUSEMOTION:
            if self.image == self.button_clicked:
                if not (pygame.mouse.get_pos()[0] > self.rect.left and
                        pygame.mouse.get_pos()[0] < self.rect.right and
                        pygame.mouse.get_pos()[1] < self.rect.bottom and
                        pygame.mouse.get_pos()[1] > self.rect.bottom - self.rect.height):
                    self.image = self.button_unclicked

    def hide(self):
        self.image = self.invisible_button
        self.working = False

    def show(self):
        self.image = self.button_unclicked
        self.working = True
