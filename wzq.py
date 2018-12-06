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
import time

def run_game():
    pygame.init()
    settings = Settings()

    # 创建存储棋子的编组
    pieces = Group()

    screen = pygame.display.set_mode((settings.screen_width,settings.screen_height),4,0)
    chequer = Chequer(settings,screen,pieces)
    pygame.display.set_caption("五子棋")
    background = pygame.image.load("background3.jpg").convert()
    button_d = Button(screen,"悔棋",32,(65,49),(20,20,90,55))
    button_d2 = Button(screen, "悔棋", 35, (65, 49), (18, 18, 95, 63))
    button_r = Button(screen, "重新開始", 30, (200, 49), (130, 20, 140, 58))
    button_r2 = Button(screen, "重新開始", 33, (200, 49), (128, 18, 145, 62))

    msg_box_reset = Msg_box(screen,"確定重新開始？","確定","取消")
    box_black_win = Msg_box(screen, "黑棋獲勝!", "重置", "退出")
    box_white_win = Msg_box(screen, "白棋獲勝!", "重置", "退出")
    box_get_draw = Msg_box(screen, "平局!", "重置", "退出")
    while True:
        f.check_events(settings,chequer,pieces,button_d2,button_r2,msg_box_reset)
        #screen.fill((settings.bg_color))
        screen.blit(background,(0,0))
        chequer.lines()
        chequer.cirs()
        chequer.get_mouse_pos(pieces)
        for pos in chequer.poslist_b:
            chequer.set_piece(pos,chequer.black)
        for pos in chequer.poslist_w:
            chequer.set_piece(pos,chequer.white)

        f.draw_button_d(button_d,button_d2)
        f.draw_button_r(button_r, button_r2)

        f.draw(settings,msg_box_reset,box_black_win,box_white_win,box_get_draw,chequer)



        pygame.display.flip()

run_game()
