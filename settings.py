

#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Settings:
    def __init__(self):
        self.screen_width = 600
        self.screen_height = 700
        self.bg_color = (200,200,200)

        #1为黑棋，0为白棋
        self.color = 1

        #重置框按钮,True时绘制重新开始框
        self.box_reset = False

        #开始游戏
        self.start = True

        #判断连子,五连子时获胜(四个条线，8个方向)
        self.num = 0
        self.num2 = 0
        self.num3 = 0
        self.num4 = 0

        #判断哪方获胜，1为黑棋获胜，-1为白棋获胜,0为平局,绘制对应的消息框
        self.get_win =-1

        #绘制退出按钮，实现动画效果
        self.close = 0



