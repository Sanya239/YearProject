import pygame
import ver5.elements.parameters_box_class5 as parameters_box_class

class Checkbox(pygame.sprite.Sprite):
    def __init__(self,parent, position=(0, 0), text='',size = (300,100),parameter=0):
        pygame.sprite.Sprite.__init__(self)
        self.checkbox_clicked = pygame.Surface(size)
        self.checkbox_clicked.fill((255,255,255))
        self.checkbox_unclicked = pygame.Surface(size)
        self.checkbox_unclicked.fill((255,255,255))
        self.parent = parent
        self.position = position

        self.rect = self.checkbox_clicked.get_rect()
        self.rect.center = self.position
        pygame.font.init()
        self.font = pygame.font.Font(None, int(self.rect.height * 0.60))
        self.text = self.font.render(text, True, parameters_box_class.Parameters_box.font_colour)



        self.checkbox_unclicked.blit(self.text, (50, int(self.rect.height*0.2)))
        pygame.draw.rect(self.checkbox_unclicked, (0, 0, 0),
                         (int(self.rect.width*0.66), int(self.rect.height * 0.2), int(self.rect.height * 0.50), int(self.rect.height * 0.50)),
                         width=1)
        self.checkbox_unclicked.set_colorkey((255,255,255))

        self.checkbox_clicked.blit(self.text, (50, int(self.rect.height*0.2)))
        pygame.draw.rect(self.checkbox_clicked, (0, 0, 0),
                         (int(self.rect.width*0.66), int(self.rect.height * 0.2), int(self.rect.height * 0.50), int(self.rect.height * 0.50)),
                         width=1)
        pygame.draw.line(self.checkbox_clicked,(0,0,0),(int(self.rect.width*0.66), int(self.rect.height * 0.2)),
                         (int(self.rect.width*0.66)+int(self.rect.height * 0.50), int(self.rect.height * 0.2)+int(self.rect.height * 0.50)),width=2)
        pygame.draw.line(self.checkbox_clicked, (0, 0, 0), (int(self.rect.width * 0.66) + int(self.rect.height * 0.50), int(self.rect.height * 0.2)),
                         (int(self.rect.width * 0.66),
                          int(self.rect.height * 0.2) + int(self.rect.height * 0.50)), width=2)
        self.checkbox_clicked.set_colorkey((255, 255, 255))
        '''self.text = self.font.render(text, True, (100, 100, 100))
        self.checkbox_triggered.blit(self.text, (50, int(self.rect.height * 0.2)))'''
        self.parameter = parameter

        self.message = parameters_box_class.Parameters_box.players[self.parameter] == 'bot'
        self.change_status()

    def update(self, event: pygame.event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if (pygame.mouse.get_pos()[0] > self.rect.left and
                    pygame.mouse.get_pos()[0] < self.rect.right and
                    pygame.mouse.get_pos()[1] < self.rect.bottom and
                    pygame.mouse.get_pos()[1] > self.rect.bottom - self.rect.height):

                self.change_status()
                self.parent.settings_redraw()


    def change_status(self):
        if self.message == True:
            self.message = False
            self.image = self.checkbox_unclicked
            parameters_box_class.Parameters_box.players[self.parameter] = 'bot'
            print('bot')
        else:
            self.message = True
            self.image = self.checkbox_clicked
            print('human')
            parameters_box_class.Parameters_box.players[self.parameter] = 'human'
