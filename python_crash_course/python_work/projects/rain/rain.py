import pygame
from pygame.sprite import Sprite
    
class Rain(Sprite): # 生成被编组的实例的类，需要继承 Sprite 类
    """实现雨滴的类"""
    def __init__(self, sky):
        """初始化雨滴"""
        super().__init__() # 继承父类的属性
        self.screen = sky.screen
        self.screen_rect = sky.screen_rect
        # 加载图片
        self.image = pygame.image.load("./images/rain.bmp")
        # 获取、设置图片的 rect 属性
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width # 设置间隔为图片本身的宽度
        self.rect.y = self.rect.height # 设置间隔为图片本身/3的高度, 模拟落雨
        self.speed = 5 # 雨滴滑落的速度
        
    def check_edge(self):
        """检查雨滴是否落出屏幕"""
        return self.rect.bottom >=  self.screen_rect.bottom
    
    def update(self):
        """实现雨滴滑落效果"""
        self.rect.y += self.speed