#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pygame.font
from pygame.sprite import Sprite

class Button():
    def __init__(self,screen,msg,size,msg_pos,ellipse_rect):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.msg =msg
        self.size = size
        self.msg_pos = msg_pos
        self.ellipse_rect = ellipse_rect

        self.color_b =(0,0,0)
        self.font = pygame.font.Font('ziti.ttf', self.size)

        self.prep_msg(msg)

    def prep_msg(self,msg):
        self.msg_image = self.font.render(self.msg,True,self.color_b)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.msg_pos
        return self.msg_image

    def draw_button(self):
        pygame.draw.ellipse(self.screen, self.color_b,self.ellipse_rect,2)
        self.screen.blit(self.msg_image,self.msg_image_rect)
