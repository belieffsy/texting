#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygame
from pygame.sprite import Sprite

class Chequer(Sprite):
    def __init__(self,settings,screen,pieces):
        super(Chequer,self).__init__()
        self.settings = settings
        self.screen = screen
        self.pieces = pieces

        self.black = 0, 0, 0
        self.white = 255,255,255
        self.intersection_list = []
        #self.poslist_b = []
        #self.poslist_w = []

        self.get_intersection()
        #self.get_mouse_pos()

    def lines(self):
        #线条
        pygame.draw.aaline(self.screen, self.black, (0,100), (600,100), 1)
        pygame.draw.aaline(self.screen, self.black, (1, 100), (1, 699), 1)
        pygame.draw.aaline(self.screen, self.black, (598, 100), (598, 699), 1)
        pygame.draw.aaline(self.screen, self.black, (1, 698), (598, 698), 1)
        for a in range(130, 800, 30):
            sta_pos = 1, a
            end_pos = 600, a
            pygame.draw.line(self.screen,self.black, sta_pos, end_pos, 1)
            sta_pos2 = a - 100, 100
            end_pos2 = a - 100, 700
            pygame.draw.line(self.screen,self.black, sta_pos2, end_pos2, 1)

    def cirs(self):
        #加粗圆点
        pos = (300, 400)
        pygame.draw.circle(self.screen, self.black, pos, 4)
        pos2 = 180, 280
        pygame.draw.circle(self.screen, self.black, pos2, 3)
        pos3 = 420, 280
        pygame.draw.circle(self.screen, self.black, pos3, 3)
        pos4 = 180, 520
        pygame.draw.circle(self.screen, self.black, pos4, 3)
        pos5 = 420, 520
        pygame.draw.circle(self.screen, self.black, pos5, 3)


    def get_intersection(self):
        """获取交点坐标"""
        for a in range (100,701,30):
            for b in range(0,601,30):
                self.intersection_list.append((b,a))


    def get_mouse_pos(self,pieces):
        x,y = pygame.mouse.get_pos()
        self.pos = int(round(x, -1)), int(round(y, -1))
        if self.pos in self.intersection_list:
            if self.settings.color:
                self.set_piece(self.pos,self.black)
            else:
                self.set_piece(self.pos,self.white)



    def set_piece(self,pos,color):
        """"""
        pygame.draw.circle(self.screen,color,pos, 15)

        #pygame.draw.circle(self.screen, self.white,pos, 15)
