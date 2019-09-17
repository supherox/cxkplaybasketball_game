import pygame
from pygame.sprite import Sprite

class zhouqi(Sprite):

    def __init__(self, ai_settings, screen,):

        super(zhouqi, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        self.image = pygame.image.load('pic/zhouqim.bmp')
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width*0.3
        self.rect.y = self.rect.height*0.3

        self.x = float(self.rect.x)

    def blitme(self):

        self.screen.blit(self.image, self.rect)

    def update(self):

        self.x += (self.ai_settings.zhouqi_speed_factor*self.ai_settings.fleet_direction)
        self.rect.x =self.x


    def check_edges(self):

        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True
