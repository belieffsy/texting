#!/usr/bin/env python
# -*- coding: utf-8 -*-


import pygame.font
from pygame.sprite import Sprite

class Msg_box():
    def __init__(self,screen,msg,msg2,msg3):
        self.screen = screen
        self.msg =msg
        self.msg2 =msg2
        self.msg3 = msg3
        self.screen_rect = screen.get_rect()

        self.color_b =(0,0,0)
        self.font = pygame.font.Font('ziti.ttf', 45)
        #self.rect= pygame.Rect(0,0,self.x,self.y)
        #self.rect.center = self.screen_rect.center

        self.image = pygame.image.load('box2.jpg')
        self.image_rect = self.image.get_rect()
        self.image_rect.center =self.screen_rect.center

        self.prep_msg(msg)
        self.prep_msg2(msg2)
        self.prep_msg3(msg3)

    def prep_msg(self,msg1):
        self.msg_image = self.font.render(self.msg,True,self.color_b)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.centerx = self.image_rect.centerx+15
        self.msg_image_rect.bottom = self.image_rect.top+100
        return self.msg_image

    def prep_msg2(self,msg2):
        self.msg2_image = self.font.render(self.msg2,True,self.color_b)
        self.msg2_image_rect = self.msg_image.get_rect()
        self.msg2_image_rect.centerx = self.image_rect.centerx+55
        self.msg2_image_rect.bottom = self.image_rect.top+190
        return self.msg2_image

    def prep_msg3(self,msg3):
        self.msg3_image = self.font.render(self.msg3,True,self.color_b)
        self.msg3_image_rect = self.msg_image.get_rect()
        self.msg3_image_rect.centerx = self.image_rect.centerx+190
        self.msg3_image_rect.bottom = self.image_rect.top+190
        return self.msg3_image


    def draw_botton(self):
        pygame.draw.circle(self.screen, self.color_b,(469,252),20,3)
        self.screen.blit(self.msg_image,self.msg_image_rect)
        self.screen.blit(self.msg2_image, self.msg2_image_rect)
        self.screen.blit(self.msg3_image, self.msg3_image_rect)

    def blitme(self):
        self.screen.blit(self.image, self.image_rect)
