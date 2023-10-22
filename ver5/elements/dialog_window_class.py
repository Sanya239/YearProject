import pygame
import ver5.elements.parameters_box_class5 as parameters_box_class

class Dialog_window(pygame.sprite.Sprite):
    def __init__(self, parent, size=(200, 100), text="", position = (400,400), colour=(0,0,0), parameter = 0, max_number = 255):
        self.parent = parent
        self.position = position
        self.parameter = parameter
        self.prev_text ='text'
        self.colour = colour
        self.max_number = max_number
        self.font = pygame.font.Font(None,80)
        pygame.sprite.Sprite.__init__(self)
        self.size_x, self.size_y = size
        self.surf = pygame.Surface((self.size_x, self.size_y))
        self.surf.fill((255, 255, 255))
        pygame.draw.rect(self.surf, self.colour, (2, 2, self.size_x -5, self.size_y - 5), width=2)
        self.working = False
        self.rect = self.surf.get_rect()
        self.rect.center = self.position
        self.text = text
        self.text2 = text
        self.text_render(text)
        if self.max_number<1000:
            self.deactivation_func = self.parent.settings_redraw
        else:
            self.deactivation_func = print

    def activation(self):
        pygame.draw.rect(self.surf, (128, 128, 255), (0, 0, self.size_x-1, self.size_y-1), width=2)
        self.working = True


    def deactivation(self):
        if self.text == '':
            self.text = '0'
            self.text_render(self.text2)
        pygame.draw.rect(self.surf, (255, 255, 255), (0, 0, self.size_x-1, self.size_y-1), width=2)
        self.working = False
        if self.prev_text != self.text:
            self.deactivation_func()
            #self.parent.settings_redraw()
        self.prev_text = self.text
    def text_render(self,text):
        self.image = self.surf.copy()
        self.image.blit(self.font.render(text,True,self.colour),(20,10))
        if self.parameter <= 2:
            if not self.text == '':
                parameters_box_class.Parameters_box.background_colour[self.parameter] = int(self.text)
            else:
                parameters_box_class.Parameters_box.background_colour[self.parameter] = 0

    def update(self, event: pygame.event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if (pygame.mouse.get_pos()[0] > self.rect.left and
                    pygame.mouse.get_pos()[0] < self.rect.right and
                    pygame.mouse.get_pos()[1] < self.rect.bottom and
                    pygame.mouse.get_pos()[1] > self.rect.bottom - self.rect.height):
                self.activation()
            else:
                self.deactivation()
            self.image = self.surf.copy()
            self.text_render(self.text2)

        if self.working == True:
            if event.type == pygame.KEYDOWN:

                if event.key in range(48, 58):
                    new_text = self.text+(str(event.key-48))
                    if not int(new_text)>self.max_number:
                        self.text = new_text
                        self.text2 += str(event.key-48)
                        if self.text == '00' and self.max_number < 1000:
                            self.text = '0'
                            self.text2 ='0'

                    if len(self.text)%4 == 0 and int(self.text)<999999999999999:
                        self.text2 +='.'
                if event.key == pygame.K_BACKSPACE:
                    if self.text2!='':
                        if self.text2[-1] == '.':
                            self.text2 = self.text2[0:-1]
                    self.text = self.text[0: -1]
                    self.text2 = self.text2[0:-1]

                self.text_render(self.text2)
                print(self.text2)
                print(self.text)
