import pygame

class Label(pygame.sprite.Sprite):
    def __init__(self,text='',position=(0,0),size=(0,0),colour = (0,0,0)):
        pygame.sprite.Sprite.__init__(self)
        self.size_x,self.size_y = size
        self.surf = pygame.surface.Surface((self.size_x,self.size_y))
        self.text = text
        self.colour = colour
        self.position = position
        self.font = pygame.font.Font(None, int(self.size_y*0.6))
        self.surf.blit(self.font.render(self.text,True,self.colour),(20,int(self.size_y*0.2)))
        self.image = self.surf.copy()
        self.rect = self.image.get_rect()
        self.rect.center = self.position
