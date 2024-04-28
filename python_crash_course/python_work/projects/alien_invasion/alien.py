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

    def check_left_or_right_edge(self):
        """如果外星人抵达屏幕左、右边缘，返回True"""
        return (self.rect.left <= 0) or (self.rect.right >= self.screen_rect.right)

    def check_bottom_edge(self):
        """检测外星人是否抵达屏幕底部"""
        return self.rect.bottom >= self.screen_rect.bottom
    
    def update(self):
        """外星舰队左右移动，向飞船逼近"""
        self.x += self.settings.alien_speed * self.settings.fleet_direction
        self.rect.x = self.x
