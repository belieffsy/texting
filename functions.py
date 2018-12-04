
#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import pygame
from chequer import Chequer
import os

def check_events(chequer,pieces,button_d2,button_r2):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            pos =(int(round(x, -1)), int(round(y, -1)))
            if pos in chequer.intersection_list:
                add_pos(chequer,pos)
            elif button_d2.msg_image_rect.collidepoint(x,y):
                check_button_d(chequer, button_d2)
            elif button_r2.msg_image_rect.collidepoint(x,y):
                reset(chequer)

def add_pos(chequer,pos):
    """如果点击下棋，添加圆心pos"""
    if chequer.color:
        chequer.poslist_b.append(pos)
        check_win(chequer.poslist_b, pos)
        chequer.color -= 1
    else:
        chequer.poslist_w.append(pos)
        check_win(chequer.poslist_w, pos)
        chequer.color += 1

def reset(chequer):
    #重置游戏
    chequer.poslist_w = []
    chequer.poslist_b = []
    chequer.color = 1

def check_button_d(chequer,button_d2):
    """检查悔棋按钮"""
    if chequer.color:
        chequer.poslist_w = chequer.poslist_w[0:-1]
        chequer.color -= 1
    else:
        chequer.poslist_b = chequer.poslist_b[0:-1]
        chequer.color += 1

def draw_button_d(button_d,button_d2):
    #悔棋按钮
    x, y = pygame.mouse.get_pos()
    if button_d2.msg_image_rect.collidepoint(x, y):
        button_d2.draw_button()
    else:
        button_d.draw_button()

def draw_button_r(button_r,button_r2):
    #重新开始按钮
    x, y = pygame.mouse.get_pos()
    if button_r2.msg_image_rect.collidepoint(x, y):
        button_r2.draw_button()
    else:
        button_r.draw_button()


def check_win(poslist,pos):
    x,y = pos
    #判断x坐标不变
    n = 0
    check(poslist, x, y, 0, 1, n)
    check(poslist, x, y,  0, -1, n)
    #判断y坐标不变
    m = 0
    check(poslist, x, y, 1, 0, m)
    check(poslist, x, y, -1, 0, m)
    #对角线
    j = 0
    check(poslist, x, y, 1, -1, j)
    check(poslist, x, y, -1, 1, j)
    #对角线
    k = 0
    check(poslist, x, y, -1, -1, k)
    check(poslist, x, y, 1, 1, k)

def check(poslist,x,y,i,j,n):
    for k in range(1, 5):
        if (x + k * 30*i, y + k * 30*j) in poslist:
            n += 1
            if n >= 4:
                print("win")
                n = 0
        else:
            return n





