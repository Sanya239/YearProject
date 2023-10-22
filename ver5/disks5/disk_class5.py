import pygame
import os

game_folder = os.path.dirname(__file__)


class disk(pygame.sprite.Sprite):
    def __init__(self, colour, position):
        pygame.sprite.Sprite.__init__(self)
        self.position = position
        self.black_disk = pygame.image.load(os.path.join(game_folder, 'black_disk2.bmp')).convert()
        self.black_disk.set_colorkey((255, 0, 0))
        self.white_disk = pygame.image.load(os.path.join(game_folder, 'white_disk2.bmp')).convert()
        self.white_disk.set_colorkey((255, 0, 0))
        self.invisible_disk = pygame.image.load(os.path.join(game_folder, 'invisible_disk1.bmp')).convert()
        self.invisible_disk.set_colorkey((0, 0, 0))
        self.animation_set1 = []

        self.animation_set2 = []
        im = pygame.image.load(os.path.join(game_folder,'black_disk_animated.bmp'))
        im.set_colorkey((255,0,0))
        for i in range(19):
            self.animation_set2.append(pygame.transform.rotate(im,-i*24))
        im = pygame.image.load(os.path.join(game_folder, 'white_disk_animated.bmp'))
        im.set_colorkey((255, 0, 0))
        for j in range(19):
            self.animation_set1.append(pygame.transform.rotate(im, -j * 24))
        self.animation_set1.append(self.white_disk)
        self.animation_set2.append(self.black_disk)
        self.placed = False
        self.colour = colour
        self.animation_mode_ON = False
        self.animation_tick = 0
        if self.colour == 1:
            self.image = self.white_disk
        elif self.colour == 2:
            self.image = self.black_disk
        elif self.colour == 0:
            self.image = self.invisible_disk
        self.rect = self.image.get_rect()
        self.rect.center = (self.position[0] * 80 + 120, self.position[1] * 80 + 120)

    def flip(self, colour):
        if colour == 0:
            self.colour = 0
            self.image = self.invisible_disk
        if colour == 1:
            self.colour = 1
            self.animation_mode_ON = True
            self.animation_tick = 0

        if colour == 2:
            self.colour = 2
            self.animation_mode_ON = True
            self.animation_tick = 0

    def update(self):
        if self.animation_mode_ON == True:
            if self.colour == 1:
                self.image = self.animation_set1[self.animation_tick]
                self.rect = self.image.get_rect()
                self.rect.center = (self.position[0] * 80 + 120, self.position[1] * 80 + 120)

            if self.colour == 2:
                self.image = self.animation_set2[self.animation_tick]
                self.rect = self.image.get_rect()
                self.rect.center = (self.position[0] * 80 + 120, self.position[1] * 80 + 120)
            self.animation_tick += 1
            if self.animation_tick == 20:
                self.animation_mode_ON = False
