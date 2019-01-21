
#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import pygame
from chequer import Chequer
import os
import time
import subprocess


def check_events(settings,chequer,pieces,button_d2,button_r2,button_s2,msg_box_reset,count_down):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            pos =(int(round(x, -1)), int(round(y, -1)))
            if not settings.start:
                settings.close = 1
            if pos in chequer.intersection_list and settings.start ==1:
                add_pos(settings,chequer,pos)
            elif button_d2.msg_image_rect.collidepoint(x,y):
                #悔棋按钮
                check_button_d(settings,chequer, button_d2)
            elif button_r2.msg_image_rect.collidepoint(x,y) and settings.get_win not in (-1,0,1):
                #点击重新开始，重新开始弹框
                settings.box_reset = True
                settings.start = False
            elif button_s2.msg_image_rect.collidepoint(x,y) and settings.get_win not in (-1,0,1):
                #点击设置，设置弹框
                settings.jinshou_box = True
                settings.start = False
            elif msg_box_reset.msg2_image_rect.collidepoint(x,y):
                #弹框左按钮————确定，重置,开启，关闭
                if settings.box_reset ==True or settings.get_win in (1,0,-1):
                    #重新开始————确定；胜利弹框————重置
                    reset(settings,chequer,count_down)
                    settings.start = True
                    settings.box_reset = False
                    settings.get_win = None
                elif settings.jinshou_box:#禁手弹框————开启，关闭
                    if settings.open_jinshou:
                        settings.open_jinshou = False
                    else:
                        settings.open_jinshou = True
                    settings.jinshou_box = False
                    settings.start = True
                elif settings.jinshou:#判断禁手位置弹框的确定
                    settings.jinshou = False
                    settings.start = True
            elif settings.box_reset == True or settings.get_win in (1,0,-1) or settings.jinshou_box or settings.jinshou : #or settings.get_win==-1 or settings.get_win==0
                if  msg_box_reset.circle_rect.collidepoint(x,y):
                    settings.box_reset = False
                    settings.start = True
                    settings.get_win = None
                    settings.jinshou_box = False
                    settings.jinshou =False
                elif msg_box_reset.msg3_image_rect.collidepoint(x,y):
                    if settings.box_reset == True:
                        settings.box_reset = False
                    if settings.get_win in (1,0,-1):
                        sys.exit()
                    if settings.jinshou_box or settings.jinshou or settings.open_jinshou:
                        subprocess.Popen(['start', 'jinshou.docx'], shell=True)



def add_pos(settings,chequer,pos):
    """如果点击下棋，添加圆心pos"""
    if settings.color:
        if pos not in settings.poslist_w:
            settings.poslist_b.append(pos)
            chequer.intersection_list.remove(pos)
            check_win(settings,settings.poslist_b, pos,chequer)
            settings.color -= 1
    else:
        if pos not in settings.poslist_b:
            chequer.intersection_list.remove(pos)
            settings.poslist_w.append(pos)
            check_win(settings,settings.poslist_w, pos,chequer)
            settings.color += 1
    if chequer.intersection_list ==[]:
        settings.get_win = 0

def reset(settings,chequer,count_down):
    #重置游戏
    chequer.intersection_list.extend(settings.poslist_w)
    chequer.intersection_list.extend(settings.poslist_b)
    settings.poslist_w = []
    settings.poslist_b = []
    settings.color = 1
    #重置倒计时
    settings.tt = 0
    settings.min = 30
    settings.sec = 60
    settings.n = 1
    count_down.prep2_msg('%s:00' % (settings.min))
    #重置提醒禁手次数
    settings.warning = 2

def check_button_d(settings,chequer,button_d2):
    """检查悔棋按钮"""
    if settings.poslist_w !=[] or settings.poslist_b !=[]:
        if settings.color:
            chequer.intersection_list.append(settings.poslist_w[-1])
            settings.poslist_w = settings.poslist_w[0:-1]
            settings.color -= 1
        else:
            chequer.intersection_list.append(settings.poslist_b[-1])
            settings.poslist_b = settings.poslist_b[0:-1]
            settings.color += 1

def draw_button(button,button_2):
    #绘制各种按钮————悔棋，重新开始，设置
    x, y = pygame.mouse.get_pos()
    if button_2.msg_image_rect.collidepoint(x, y):
        button_2.draw_button()
    else:
        button.draw_button()

def check_win(settings,poslist,pos,chequer):
    """判断落子八个方向连珠个数，如果五子，判出胜负"""
    x,y = pos
    active33 = 0
    active44 = 0
    #(0,1,0,-1)判断x坐标不变(竖线），(1,0,-1,0)判断y轴不变（横线）
    #(1,-1,-1,1)判断对角线(撇)，(-1,-1,1,1)判断对角线(捺)
    for q,w,e,r in ((0,1,0,-1),(1,0,-1,0),(1,-1,-1,1),(-1,-1,1,1)):
        settings.num = 0
        settings.points =[]
        check(poslist, x, y, q, w,settings)
        check(poslist, x, y,  e, r,settings)
        if settings.num >= 4:
            settings.start = False
            if settings.open_jinshou and settings.num > 4 and settings.color == 1:
                if settings.warning > 0:
                    settings.jinshou = True
                    settings.get_win = None
                    jinshou(settings, chequer)
                    settings.warning -= 1
                else:
                    settings.get_win = -1
            else:
                if settings.color:
                    settings.get_win = 1
                else:
                    settings.get_win = -1
        settings.points.append(pos)
        if settings.num >= 2 and settings.color ==1 and settings.open_jinshou:
            if check_active(settings, q, w, e, r,chequer)==2:
                active33 += 1
            elif check_active(settings, q, w, e, r,chequer)==1 and settings.num > 2:
                active44 += 1
    if active33 >= 2 or active44>=2 :
        jinshou(settings,chequer)
        settings.start = False
        if settings.warning>0:
            settings.warning -=1
            settings.jinshou = True
        else:
            settings.get_win = -1

def check(poslist,x,y,i,j,settings):
    """判断落子一个方向的连珠个数"""
    for k in range(1, 5):
        if (x + k * 30*i, y + k * 30*j) in poslist:
            settings.num += 1
            settings.points.append((x + k * 30*i, y + k * 30*j))
        else:
            return

def check_active(settings,i,j,k,l,chequer):
    m=0
    for n in range(len(settings.points)):
        x,y = settings.points[n]
        if ((x + 30*i, y + 30*j)  in chequer.intersection_list) or  ((x +  30*k, y + 30*l) in chequer.intersection_list):
            m += 1
    return m

def jinshou(settings,chequer):
    chequer.intersection_list.append(settings.poslist_b[-1])
    settings.poslist_b = settings.poslist_b[0:-1]
    settings.color += 1

def draw(settings,msg_box_reset,box_black_win,box_white_win,box_get_draw,box_get_draw2,box_open_jinshou,box_close_jinshou,box_jinshou):
    """绘制各种弹框————重新开始，白棋获胜，黑棋获胜，平局，黑棋禁手"""
    if settings.box_reset:
        draw_box(msg_box_reset,settings)
    elif settings.get_win == 1:
        draw_box(box_black_win,settings)
    elif settings.get_win == -1:
        draw_box(box_white_win,settings)
    elif settings.get_win == 0:
        if settings.min ==0 and settings.sec == 0:
            draw_box(box_get_draw2,settings)
        else:
            draw_box(box_get_draw,settings)
    elif settings.jinshou_box:
        if settings.open_jinshou:
            draw_box(box_close_jinshou,settings)
        else :
            draw_box(box_open_jinshou,settings)
    elif settings.jinshou:
        draw_box(box_jinshou,settings)

def draw_box(msg_box,settings):
    """绘制弹框消息"""
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
    #检查是否平局 如果棋子下满棋盘，则为平局
    if chequer.intersection_list == []:
        settings.get_win = 0
    elif settings.min ==0 and settings.sec == 0:
        settings.get_win = 0

def tine_down(settings):
    if settings.poslist_b and settings.start:
        t = time.time()
        if t - settings.tt >=1:
            settings.tt=t
            return True
def prep_time(settings,count_down):
    """倒计时的设置"""
    if tine_down(settings):
        if settings.n:
            settings.n -=1
        elif settings.sec==60 and not settings.n:
            settings.sec -=1
            settings.min -=1
        elif settings.sec ==0 and settings.min == 0:
            settings.get_win = 0
            settings.start = False
        elif settings.sec == 0 and settings.min != 0:
            settings.sec = 59
            settings.min -= 1
        else:
            settings.sec -=1
        if settings.sec == 60:
            count_down.prep2_msg('%s:00'%settings.min)
        elif settings.sec<10:
            count_down.prep2_msg('%s:0%s' % (settings.min, settings.sec))
        else:
            count_down.prep2_msg('%s:%s' % (settings.min,settings.sec))




