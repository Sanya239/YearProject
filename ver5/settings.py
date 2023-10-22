import pygame
import ver5.buttons5.button_class as button_class
import ver5.elements.checkbox_class as checkbox_class
import ver5.elements.dialog_window_class as dialog_window_class
import ver5.elements.parameters_box_class5 as parameters_box_class
import time

class Settings():
    def __init__(self, parent):
        self.parent = parent
        self.screen = self.parent.screen
        pygame.font.init()
        self.font = pygame.font.Font(None, 60)
        self.elements = pygame.sprite.Group()
        self.title = pygame.Surface((300, 100))
        self.title.fill(parameters_box_class.Parameters_box.background_colour)
        self.title.blit(self.font.render('Settings', True,parameters_box_class.Parameters_box.font_colour), (0, 0))

        self.menu_button = button_class.button((125, 50), text='menu', func=self.return_to_menu)

        self.player1_checkbox = checkbox_class.Checkbox(self,position=(200,200), text= '1st player is bot',size=(400,50),parameter=0)

        self.player2_checkbox = checkbox_class.Checkbox(self,position=(200,300), text= '2nd player is bot',size=(400,50),parameter=1)

        self.dialog_R = dialog_window_class.Dialog_window(self,position=(400,400),text=str(parameters_box_class.Parameters_box.background_colour[0]),parameter=0)
        self.dialog_G = dialog_window_class.Dialog_window(self, position= (400,500),text=str(
            parameters_box_class.Parameters_box.background_colour[1]), parameter=1)
        self.dialog_B = dialog_window_class.Dialog_window(self, position=(400,600),text=str(
            parameters_box_class.Parameters_box.background_colour[2]), parameter=2)

        self.last_click = 0
    def titles(self):
        self.screen.blit(self.title, (300, 60))
        self.screen.blit(self.font.render('parameter R:',True,parameters_box_class.Parameters_box.font_colour),(20,380))
        self.screen.blit(self.font.render('parameter G:', True, parameters_box_class.Parameters_box.font_colour),
                         (20,480))
        self.screen.blit(self.font.render('parameter B:', True, parameters_box_class.Parameters_box.font_colour),
                         (20, 580))
    def settings_redraw(self):
        self.screen.fill(parameters_box_class.Parameters_box.background_colour)
        self.elements.add(self.menu_button)
        self.elements.add(self.player1_checkbox)
        self.elements.add(self.player2_checkbox)
        self.elements.add(self.dialog_R)
        self.elements.add(self.dialog_B)
        self.elements.add(self.dialog_G)
        self.elements.draw(self.screen)
        self.titles()

    def return_to_menu(self):
        self.dialog_R.deactivation()
        self.parent.mode = 0
        self.elements.draw(self.screen)
        self.parent.menu.menu_draw()
        self.elements = pygame.sprite.Group()

    def update(self,event: pygame.event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if time.time() - self.last_click >= 0.2:
                self.last_click = time.time()
                self.elements.update(event)
                self.elements.draw(self.screen)


        elif event.type == pygame.MOUSEMOTION or event.type == pygame.KEYDOWN:
            self.elements.update(event)
            self.elements.draw(self.screen)


