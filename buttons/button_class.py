import pygame
import os
import time

game_folder = os.path.dirname(__file__)


class button(pygame.sprite.Sprite):
    def __init__(self):
        self.button_unclicked = pygame.image.load(os.path.join(game_folder, 'button_unclicked.png')).convert()
        self.button_unclicked.set_colorkey((255,255,255))
        pygame.sprite.Sprite.__init__(self)
        self.image = self.button_unclicked
        self.rect = self.image.get_rect()
        self.message = False
        # self.rect.center = (WIDTH / 2, HEIGHT / 2)

    def update(self, event):
        if event == None:
            self.image = pygame.transform.flip(self.button_unclicked,False,True).set_colorkey((255,255,255))
            #self.image.set_colorkey()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if (pygame.mouse.get_pos()[0] > self.rect.left and
                    pygame.mouse.get_pos()[0] < self.rect.right and
                    pygame.mouse.get_pos()[1] < self.rect.bottom and
                    pygame.mouse.get_pos()[1] > self.rect.bottom - self.rect.height):
                button_clicked = pygame.image.load(os.path.join(game_folder, 'button_clicked.png')).convert()
                self.image = button_clicked
                self.message = True
