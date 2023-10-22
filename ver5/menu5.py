import pygame
import os
import ver5.buttons5.button_class as button_class
game_folder = os.path.dirname(__file__)
import ver5.elements.parameters_box_class5 as parameters_box_class

class main_menu():

    def __init__(self, parent):
        self.parent = parent
        self.screen = self.parent.screen
        self.buttons = pygame.sprite.Group()

        self.multy_play_button = button_class.button((400, 100),text= 'multiplayer game',func=parent.set_mode1)
        self.buttons.add(self.multy_play_button)

        self.single_play_button = button_class.button((400, 200),text='local game',func=parent.set_mode2)
        self.buttons.add(self.single_play_button)

        self.settings_button = button_class.button((400,300),text='settings',func=parent.set_mode3)
        self.buttons.add(self.settings_button)
        self.menu_draw()
    def menu_draw(self):
        pygame.display.flip()
        self.screen.fill(parameters_box_class.Parameters_box.background_colour)
        pygame.time.delay(150)
        self.buttons.draw(self.screen)
        pygame.display.flip()

    def update(self,event):
            self.buttons.draw(self.screen)
            self.buttons.update(event)

            #self.screen.blit(self.single_play_button.image,self.single_play_button.rect.center)
    '''def change_mode(self):
        if self.multy_play_button.message == True:
            self.parent.set_mode1()
        elif self.single_play_button.message == True:
            self.parent.set_mode2()
        elif self.settings_button.message == True:
            self.parent.set_mode3()'''




