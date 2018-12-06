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
        self.font2 = pygame.font.Font('ziti.ttf', 50)
        #self.rect= pygame.Rect(0,0,self.x,self.y)
        #self.rect.center = self.screen_rect.center

        self.image = pygame.image.load('box2.jpg')
        self.image_rect = self.image.get_rect()
        self.image_rect.center =self.screen_rect.center

        self.x, self.y = self.image_rect.centerx + 168, self.image_rect.top + 23
        self.circle_rect = pygame.Rect(self.x - 20, self.y - 20, 50, 50)

        self.prep_msg(msg)
        self.prep_msg2(msg2, self.font)
        self.prep_msg3(msg3,self.font)

        self.prep_msg21(msg2, self.font2)
        self.prep_msg31(msg3, self.font2)

        #self.draw_close2()



    def prep_msg(self,msg1):
        self.msg_image = self.font.render(self.msg,True,self.color_b)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.centerx = self.image_rect.centerx+15
        self.msg_image_rect.bottom = self.image_rect.top+100
        return self.msg_image

    def prep_msg2(self,msg2,font):
        self.msg2_image = font.render(self.msg2,True,self.color_b)
        self.msg2_image_rect = self.msg2_image.get_rect()
        x, y = self.image_rect.centerx-60 , self.image_rect.top + 170
        self.msg2_image_rect.center = (x, y)
        return self.msg2_image

    def prep_msg3(self,msg3,font):
        self.msg3_image = font.render(self.msg3,True,self.color_b)
        self.msg3_image_rect = self.msg3_image.get_rect()
        x, y = self.image_rect.centerx + 90, self.image_rect.top + 170
        self.msg3_image_rect.center = (x, y)
        return self.msg3_image

    def prep_msg21(self,msg2,font):
        #鼠标在其位置是按钮放大
        self.msg21_image = font.render(self.msg2,True,self.color_b)
        self.msg21_image_rect = self.msg21_image.get_rect()
        x,y= self.image_rect.centerx-60,self.image_rect.top+170
        self.msg21_image_rect.center = (x,y)
        return self.msg21_image

    def prep_msg31(self,msg3,font):
        # 鼠标在其位置是按钮放大
        self.msg31_image = font.render(self.msg3,True,self.color_b)
        self.msg31_image_rect = self.msg31_image.get_rect()
        x, y = self.image_rect.centerx + 90, self.image_rect.top + 170
        self.msg31_image_rect.center = (x, y)
        return self.msg31_image


    #def draw_botton(self):


    def blitme(self):
        """在屏幕生画弹框"""
        self.screen.blit(self.image, self.image_rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)

    def blitme_msg2(self):
        #按钮1
        self.screen.blit(self.msg2_image, self.msg2_image_rect)

    def blitme_msg21(self):
        #按钮1放大效果
        self.screen.blit(self.msg21_image, self.msg21_image_rect)

    def blitme_msg3(self):
        #按钮2
        self.screen.blit(self.msg3_image, self.msg3_image_rect)

    def blitme_msg31(self):
        #按钮2放大效果
        self.screen.blit(self.msg31_image, self.msg31_image_rect)

    def draw_close(self):
        pygame.draw.circle(self.screen, self.color_b, (self.x,self.y), 20, 4)

    def draw_close2(self):
        pygame.draw.circle(self.screen, self.color_b, (self.x-1,self.y+1), 22, 7)

