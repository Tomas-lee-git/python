"""
    开发计划：
        1. 在屏幕左上角添加一个外星人，并指定合适的边距；✅
        2. 沿屏幕上边缘添加一行外星人，再不断地添加成行的外星人，直到填满屏幕的上半部分；
        3. 让外星人向两侧和向下移动，直到外星舰队被全部击落、有外星人撞到飞船
            或有外星人抵达屏幕的下边缘；
        4. 如果外星舰队都被击落，将再创建一个外星舰队；
        5. 如果有外星人撞到飞船或抵达屏幕的下边缘，销毁飞船并再创建一个外星舰队；
        6. 限制玩家可用的飞船数量，分配的飞船被用完后，游戏将结束；
"""

import pygame

from pygame.sprite import Sprite


class Alien(Sprite):
    """表示单个外星人的类"""

    def __init__(self, ai_game):
        """初始化外星人并设置其起始位置"""
        super().__init__()
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen_rect
        self.settings = ai_game.settings
        # 加载外星人并设置其 rect 属性
        self.image = pygame.image.load("images/alien.bmp")
        self.rect = self.image.get_rect()
        # # 每个外星人最初都在屏幕的左上角附近，(x, y)代表图像左上角的位置
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # 存储外星人的精确水平位置
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def update(self):
        """外星舰队左右移动，向飞船逼近"""
        is_reach_right_border = self.rect.x == (self.screen_rect.width - self.rect.width)
        # 向右移动，直到[最右边的外星人]快要超出右边界
        if not is_reach_right_border:
            self.x += self.settings.alien_speed
            self.rect.x = self.x

        # 向下移动，逼近飞船
        self.y += self.settings.alien_speed
        self.rect.y = self.y

        # 向左移动，直到[最左边的外星人]快要抵达左边界
        if is_reach_right_border:
            self.x = self.rect.x - self.settings.alien_speed
            self.rect.x = self.x

