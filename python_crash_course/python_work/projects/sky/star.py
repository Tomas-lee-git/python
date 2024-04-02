import pygame

from pygame.sprite import Sprite


class Star(Sprite):  # 生成[可以被编组的实例]的类需要继承 Sprite 类
    """实现满天繁星的类"""

    def __init__(self, sky):
        """初始化星星"""
        super().__init__()
        self.screen = sky.screen
        self.screen_rect = sky.screen_rect
        # 加载图片
        self.image = pygame.image.load("./images/star.bmp")
        # 获取并设置图片的 rect 属性
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width  # 初始位置与(0, 0) 间隔图片本身的宽度
        self.rect.y = self.rect.height  # 初始位置与(0, 0) 间隔图片本身的高度
