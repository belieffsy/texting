
#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygame
import pygame.font
from pygame.sprite import Sprite
import time

class Count_down():
    def __init__(self,screen):
        self.screen = screen
        self.msg1 = '倒計時:'
        #self.msg2 = '30:00'

        self.color_b = (0, 0, 0)
        self.font = pygame.font.Font('ziti.ttf', 22)
        self.font2 = pygame.font.Font('ziti.ttf', 40)

        self.prep1_msg()
        self.prep2_msg('30:00')

    def prep1_msg(self):
        self.msg1_image = self.font.render(self.msg1, True, self.color_b)
        self.msg1_image_rect = self.msg1_image.get_rect()
        self.msg1_image_rect.center = (370, 20)
        return self.msg1_image

    def prep2_msg(self,msg):
        self.msg2_image = self.font2.render(msg, True, self.color_b)
        self.msg2_image_rect = self.msg2_image.get_rect()
        self.msg2_image_rect.center = pygame.Rect(330,30,90,50).center
        return self.msg2_image

    def draw(self):
        #pygame.draw.ellipse(self.screen, self.color_b,self.ellipse_rect,2)
        self.screen.blit(self.msg1_image,self.msg1_image_rect)
        self.screen.blit(self.msg2_image, self.msg2_image_rect)
        pygame.draw.rect(self.screen,self.color_b,[330,30,90,50],1)

        #pygame.draw.rect()




