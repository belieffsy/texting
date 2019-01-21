#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pygame
from pygame.sprite import Group
import sys
from settings import Settings
from chequer import Chequer
import functions as f
from button import Button
from msg_box import Msg_box
from count_down import Count_down
import time

import subprocess



def run_game():
    pygame.init()
    settings = Settings()
    # 创建存储棋子的编组
    pieces = Group()

    screen = pygame.display.set_mode((settings.screen_width,settings.screen_height),4,0)
    chequer = Chequer(settings,screen,pieces)
    pygame.display.set_caption("五子棋")
    background = pygame.image.load("background3.jpg").convert()
    #按钮
    button_d = Button(screen,"悔棋",30,(65,49),(20,20,90,55))
    button_d2 = Button(screen, "悔棋", 35, (65, 49), (18, 18, 95, 63))
    button_r = Button(screen, "重新開始", 30, (200, 49), (130, 20, 140, 58))
    button_r2 = Button(screen, "重新開始", 33, (200, 49), (128, 18, 145, 62))
    button_s = Button(screen, "設置", 30, (525, 49), (480, 20, 90, 55))
    button_s2 = Button(screen, "設置", 35, (525, 49), (478, 18, 95, 63))
    #弹框
    msg_box_reset = Msg_box(screen,"確定重新開始？","確定","取消")
    box_black_win = Msg_box(screen, "黑棋獲勝!", "重置", "退出游戲")
    box_white_win = Msg_box(screen, "白棋獲勝!", "重置", "退出游戲")
    box_get_draw = Msg_box(screen, '棋盤下滿了,平局!', "重置", "退出游戲")
    box_get_draw2 = Msg_box(screen, '時間到,此局平局!', "重置", "退出游戲")
    box_open_jinshou = Msg_box(screen, "開啓黑棋禁手？", "開啓", "禁手規則")
    box_close_jinshou = Msg_box(screen, "關閉黑棋禁手？", "關閉", "禁手規則")
    box_jinshou = Msg_box(screen,"黑棋禁手,不能落子", "確定", "禁手規則")
    #倒计时
    count_down = Count_down(screen)

    while True:
        f.check_events(settings,chequer,pieces,button_d2,button_r2,button_s2,msg_box_reset,count_down)
        #screen.fill((settings.bg_color))
        screen.blit(background,(0,0))
        chequer.lines()
        chequer.cirs()
        chequer.get_mouse_pos(pieces)
        for pos in settings.poslist_b:
            chequer.set_piece(pos,chequer.black)
        for pos in settings.poslist_w:
            chequer.set_piece(pos,chequer.white)

        ##绘制各种按钮————悔棋，重新开始，设置
        f.draw_button(button_d, button_d2)
        f.draw_button(button_r, button_r2)
        f.draw_button(button_s, button_s2)


        f.draw(settings,msg_box_reset,box_black_win,box_white_win,box_get_draw,box_get_draw2,box_open_jinshou,box_close_jinshou,box_jinshou)

        #f.tine_down(settings)
        f.prep_time(settings, count_down)
        count_down.draw()

        pygame.display.flip()

run_game()
