# 在pygame 中，原点(0,0)位于游戏窗口的左上角，右下角的坐标为游戏窗口的宽、高(1200, 800)
import pygame


class Ship:
    """管理飞船的类"""

    def __init__(self, ai_game):  # ai_game是 AlienInvasion 实例的引用
        "初始化飞船并设置其初始位置"
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen_rect
        self.settings = ai_game.settings
        # 加载飞船图像并获取其外形矩形
        self.image = pygame.image.load("images/ship.bmp")
        self.rect = self.image.get_rect()
        self.center_ship()
        # 飞船移动的标志
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        """根据移动标志调整飞船的位置"""
        """
            这里都用if，而不是用if, elif的原因:
                1. 如果用 if elif，那么 if 始终处于优先地位；
                2. 如果用多个 if，那么各个 if 的条件的优先地位是一致的；
                3. 在用户同时按下多个按键时，需要得到同等的对待：
                    3.1 用户同时按下上、下，左、右，那么飞船应保持不动，也就是x，y的加减
                        是同时发生的，用户看不到位置的变化；
                    3.2 如果用户想让用户倾斜移动，如左上，左下，右上，又下，需要同时响应x和y
                        方向的变动；
                    3.3 因为以上情况，需要使用相同优先级的四个if；
                    3.4 如果使用了 if else，那只会响应四个中的一个，没法实现“静止”，“倾斜”
                        的要求；
                        
        """
        """
            检测飞船位置的更新值，防止飞船飞出屏幕外：
                1. 飞船上下左右的坐标：
                    a. self.rect.right 飞船外接矩形的右边缘的 x 坐标；
                    b. self.rect.left 飞船外接矩形左边缘的 x 坐标；
                    c. self.rect.top 飞船外接矩形的上边缘的 y 坐标；
                    d. self.rect.bottom 飞船外接矩形的右边缘的 y 坐标；
                2. 游戏窗口上下左右的坐标：
                    a. self.screen_rect.right, 游戏窗口右侧边缘 x 坐标；
                    b. self.screen_rect.left, 游戏窗口右侧边缘 x 坐标；
                    c. self.screen_rect.top, 游戏窗口右侧边缘 x 坐标；
                    d. self.screen_rect.bottom, 游戏窗口右侧边缘 x 坐标；
        """
        # 把 self.rect.x 经过 float 转换为浮点数，存储飞船位置更细致地变化
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > self.screen_rect.left:
            self.x -= self.settings.ship_speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.ship_speed
        if self.moving_up and self.rect.top > self.screen_rect.top:
            self.y -= self.settings.ship_speed

        # 实际更新飞船的位置
        self.rect.x = self.x
        self.rect.y = self.y

    def blitme(self):
        """在指定位置绘制飞船"""
        # Surface.blit, draw one image onto another
        self.screen.blit(self.image, self.rect)
        
    def center_ship(self):
        """讲飞船放在屏幕底部的中央"""
        self.rect.midbottom = self.screen_rect.midbottom
        # 在飞船的位置属性 x,y 中存储一个浮点数
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
