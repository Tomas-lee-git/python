"""
    开发计划：
        1. 渲染一颗星星；
        2. 渲染一排星星；
        3. 渲染多行，直到铺满屏幕的星星；
        4. 按下鼠标左键，随机渲染一颗星星；
        4. 按下鼠标右键，恢复所有星星；
"""
import pygame
import sys
from random import choice

from star import Star

class Sky:
    """实现夜晚天空的类"""
    def __init__(self):
        """初始化游戏并创建游戏资源"""
        pygame.init() # 初始化游戏背景
        self.clock = pygame.time.Clock()  # 通过self.clock 控制游戏的帧率
        self.screen = pygame.display.set_mode((1200, 900)) # 设置游戏窗口大小
        self.screen_rect = self.screen.get_rect() # 获取游戏窗口 rect
        pygame.display.set_caption("Sky full of stars")
        self._full_sky_stars()
    
    def _create_star(self, x_position, y_position):
        """生成一个星星"""
        star = Star(self)
        star.rect.x = x_position
        star.rect.y = y_position
        self.stars.add(star)
        
    def _create_all_stars(self):
        """生成众多星星"""
        star = Star(self)
        star_width = star.rect.width # 获取一个星星的宽度
        star_height = star.rect.height # 获取一个星星的高度
        current_x  = 0.3 * star_width 
        current_y  = 0.5 * star_height 
        # 不断地重复[生成一整行星星], 直到生成 1/3 屏幕的星星
        while current_y < (self.screen_rect.height / 3 - star_height):
            # 不断地生成星星，直到铺满一行
            while current_x < (self.screen_rect.width - star_width): # 留出两个✨边距
                self._create_star(current_x, current_y) # 不断地生成星星
                current_x += 1.3 * star_width # 动态调整最新星星的 x 轴位置

            current_y += 1.5 * star_height # 动态调整最新一行中星星的 y 轴位置
            # 绘制完一行之后，需要重置 current_x，以便开始绘制新的一行
            current_x = 0.3 * star_width

    def _full_sky_stars(self):
        #启用游戏编组来管理众多星星✨，生成[可以被编组的实例]的类需要继承 Sprite 类
        self.stars = pygame.sprite.Group()
        self._create_all_stars() # 生成星空中的所有星星
    
    def _randint_stars(self):
        """在漫天繁星中随机选中一个星星来展示"""
        # Group 没有 choice 方法，先把 Group 转换成list，再使用 choice
        star_list = self.stars.sprites()
        special_star = choice(star_list) # 挑选一个
        self.stars = pygame.sprite.Group() # 清空屏幕上的所有星星
        self.stars.add(special_star) # 渲染挑选出来的那颗星星

    def _check_event(self):
        """检查事件"""
        # 必须得添加 while 的退出条件，不然游戏就卡死了，游戏窗口都不显示了
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q: # 按 Q 退出游戏
                    sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed()[0]: # 按下鼠标左键，随机挑选一个星星
                    self._randint_stars()
                elif pygame.mouse.get_pressed()[2]: # 按下鼠标右键，恢复显示所有星星
                    self._full_sky_stars()
        
    def run_game(self):
        """开始游戏的主循环"""
        while True: # 游戏是一个不断刷新的过程，所以启动后必须不断地更新屏幕才能正常渲染游戏
            self._check_event()
            self.screen.fill((0, 0, 0)) # 黑色屏幕背景
            self.stars.draw(self.screen) # 把所有星星绘制到屏幕中
            # flip() the display to put your work on screen
            pygame.display.flip()
            self.clock.tick(60)  # limits FPS to 60
        
        
if __name__ == "__main__":
    sky = Sky() # 创建游戏实例
    sky.run_game() # 启动游戏
        