
#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import pygame
from chequer import Chequer
import os

def check_events(settings,chequer,pieces,button_d2,button_r2,msg_box_reset):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            pos =(int(round(x, -1)), int(round(y, -1)))
            if pos in chequer.intersection_list:
                if settings.start:
                    add_pos(settings,chequer,pos)
            elif button_d2.msg_image_rect.collidepoint(x,y):
                check_button_d(chequer, button_d2)
            elif button_r2.msg_image_rect.collidepoint(x,y):
                settings.box_reset = True
                settings.start = False
            elif msg_box_reset.msg2_image_rect.collidepoint(x,y):
                if settings.box_reset ==True:
                    reset(chequer)
                    settings.start = True
                    settings.box_reset = False

            elif settings.box_reset == True and (msg_box_reset.msg3_image_rect.collidepoint(x,y) or  msg_box_reset.circle_rect.collidepoint(x,y)):

                settings.box_reset = False
                settings.start = True


def add_pos(settings,chequer,pos):
    """如果点击下棋，添加圆心pos"""
    if chequer.color:
        chequer.poslist_b.append(pos)
        check_win(settings,chequer.poslist_b, pos)
        chequer.color -= 1
    else:
        chequer.poslist_w.append(pos)
        check_win(settings,chequer.poslist_w, pos)
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


def check_win(settings,poslist,pos):
    x,y = pos
    #判断x坐标不变
    settings.num = 0
    check(poslist, x, y, 0, 1,settings)
    print(settings.num)
    check(poslist, x, y,  0, -1,settings)
    #判断y坐标不变
    settings.num = 0
    check(poslist, x, y, 1, 0,settings)
    check(poslist, x, y, -1, 0,settings)
    #对角线
    settings.num = 0
    check(poslist, x, y, 1, -1,settings)
    check(poslist, x, y, -1, 1,settings)
    #对角线
    settings.num = 0
    check(poslist, x, y, -1, -1,settings)
    check(poslist, x, y, 1, 1,settings)

def check(poslist,x,y,i,j,settings):
    for k in range(1, 5):
        if (x + k * 30*i, y + k * 30*j) in poslist:
            settings.num += 1
            if settings.num >= 4:
                print("win")

        else:
            return

def draw_box_reset(settings,msg_box_reset):
    x, y = pygame.mouse.get_pos()
    if settings.box_reset:
        msg_box_reset.blitme()
        msg_box_reset.draw_close()
        #msg_box_reset.draw_close2()
        if msg_box_reset.msg2_image_rect.collidepoint(x, y):
            msg_box_reset.blitme_msg21()
        else:
            msg_box_reset.blitme_msg2()

        if msg_box_reset.msg3_image_rect.collidepoint(x, y):
            msg_box_reset.blitme_msg31()
        else:
            msg_box_reset.blitme_msg3()
        if msg_box_reset.circle_rect.collidepoint(x, y):
            msg_box_reset.draw_close2()



