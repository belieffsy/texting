
#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import pygame
from chequer import Chequer
import os
import time


def check_events(settings,chequer,pieces,button_d2,button_r2,msg_box_reset):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            pos =(int(round(x, -1)), int(round(y, -1)))
            if not settings.start:
                settings.close = 1
                #draw_close(settings, msg_box_reset)
            if pos in chequer.intersection_list and settings.start ==1:
                add_pos(settings,chequer,pos)
            elif button_d2.msg_image_rect.collidepoint(x,y):
                check_button_d(settings,chequer, button_d2)
            elif button_r2.msg_image_rect.collidepoint(x,y) and settings.get_win not in (-1,0,1):
                settings.box_reset = True
                settings.start = False
            elif msg_box_reset.msg2_image_rect.collidepoint(x,y):
                if settings.box_reset ==True or settings.get_win in (1,0,-1):
                    reset(chequer)
                    settings.start = True
                    settings.box_reset = False
                    settings.get_win = None

            elif settings.box_reset == True or settings.get_win in (1,0,-1): #or settings.get_win==-1 or settings.get_win==0
                if   msg_box_reset.circle_rect.collidepoint(x,y):
                    settings.box_reset = False
                    settings.start = True
                    settings.get_win = None
                elif msg_box_reset.msg3_image_rect.collidepoint(x,y):
                    if settings.box_reset == True:
                        settings.box_reset = False
                    if settings.get_win in (1,0,-1):
                        sys.exit()

def add_pos(settings,chequer,pos):
    """如果点击下棋，添加圆心pos"""
    if settings.color:
        if pos not in chequer.poslist_w:
            chequer.poslist_b.append(pos)
            check_win(settings,chequer.poslist_b, pos)
            settings.color -= 1
    else:
        if pos not in chequer.poslist_b:
            chequer.poslist_w.append(pos)
            check_win(settings,chequer.poslist_w, pos)
            settings.color += 1
    if len(chequer.poslist_b) +len( chequer.poslist_w )== len(chequer.intersection_list):
        print('a')
        settings.get_win = 0

def reset(chequer):
    #重置游戏
    chequer.poslist_w = []
    chequer.poslist_b = []
    chequer.color = 1

def check_button_d(settings,chequer,button_d2):
    """检查悔棋按钮"""
    if settings.color:
        chequer.poslist_w = chequer.poslist_w[0:-1]
        settings.color -= 1
    else:
        chequer.poslist_b = chequer.poslist_b[0:-1]
        settings.color += 1

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
    check(poslist, x, y,  0, -1,settings)
    #判断y坐标不变
    num1 = settings.num
    settings.num = 0
    check(poslist, x, y, 1, 0,settings)
    check(poslist, x, y, -1, 0,settings)
    #对角线
    num2 = settings.num
    settings.num = 0
    check(poslist, x, y, 1, -1,settings)
    check(poslist, x, y, -1, 1,settings)
    #对角线
    num3 = settings.num
    settings.num = 0
    check(poslist, x, y, -1, -1,settings)
    check(poslist, x, y, 1, 1,settings)
    num4 = settings.num
    print(num1,num2,num3,num4)

def check(poslist,x,y,i,j,settings):
    for k in range(1, 5):
        if (x + k * 30*i, y + k * 30*j) in poslist:
            settings.num += 1
            if settings.num >= 4:
                settings.start = False
                if settings.color:
                    settings.get_win = 1
                else:
                    settings.get_win = -1
        else:
            return

def draw(settings,msg_box_reset,box_black_win,box_white_win,box_get_draw,chequer):

    #绘制消息框
    if settings.box_reset:
        draw_box(msg_box_reset)
    elif settings.get_win == 1:
        draw_box(box_black_win)
    elif settings.get_win == -1:
        draw_box(box_white_win)
    elif settings.get_win == 0:
        draw_box(box_get_draw)

def draw_box(msg_box):
    """绘制消息框"""
    x, y = pygame.mouse.get_pos()
    msg_box.blitme()
    msg_box.draw_close()
    #msg_box_reset.draw_close2()
    if msg_box.msg2_image_rect.collidepoint(x, y):
        msg_box.blitme_msg21()
    else:
        msg_box.blitme_msg2()

    if msg_box.msg3_image_rect.collidepoint(x, y):
        msg_box.blitme_msg31()
    else:
        msg_box.blitme_msg3()
    if msg_box.circle_rect.collidepoint(x, y):
        msg_box.draw_close2()

def draw_close(settings,msg_box_reset):
    """绘制退出按钮，实现动画效果"""
    msg_box_reset.draw_close2()

def check_draw(settings,chequer):
    if chequer.poslist_b+chequer.poslist_w == chequer.intersection_list:
        settings.get_win = 0






