import pygame

from pygame.sprite import Sprite


class Bullet(Sprite):  # 继承自 Sprite 类
    """管理飞船所发射子弹的类"""

    def __init__(self, ai_game):
        """在飞船的当前位置创建一个子弹对象"""
        super().__init__()  # 使用父类的属性
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        # 在(0, 0)处创建一个表示子弹的矩形，再根据飞船的位置调整到正确的位置
        self.rect = pygame.Rect(
            0, 0, self.settings.bullet_width, self.settings.bullet_height
        )
        self.rect.midtop = ai_game.ship.rect.midtop
        # 存储用浮点数表示的子弹的位置(子弹只会在 y 轴方向向上移动，也就是 y 不断接近0)
        self.y = float(self.rect.y)

    def update(self):
        """更新子弹的准确位置（向上移动）"""
        self.y -= self.settings.bullet_speed
        # 更新表示子弹的 rect 的位置
        self.rect.y = self.y

    def draw_bullet(self):
        """在屏幕上绘制子弹"""
        pygame.draw.rect(self.screen, self.color, self.rect)
