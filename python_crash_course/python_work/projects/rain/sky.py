"""
    开发计划：
        1. 渲染一颗雨滴；
        2. 渲染一排雨滴；
        3. 渲染多行，直到铺满屏幕的雨滴；
        4. 让雨滴向下落，知道到达屏幕的下边缘后消失；
        5. 当一行雨滴消失在屏幕的下边缘后，在屏幕上边缘附近又出现一行雨滴，开始下落；
"""

import pygame
import sys

from rain import Rain

class Sky:
    """实现雨天的类"""
    def __init__(self):
        """初始化游戏并创建游戏资源"""
        pygame.init() # 初始化游戏背景
        self.clock = pygame.time.Clock() # 通过 self.clock 控制游戏的帧率
        self.screen = pygame.display.set_mode((1200, 900)) # 设置游戏窗口大小
        self.screen_rect = self.screen.get_rect() # 获取游戏窗口 rect
        pygame.display.set_caption("🌧️ Sky full of rains 🌧️") # 设置游戏窗口标题
        self._full_sky_rains()
        
    def _create_rain(self, x_position, y_position):
        """生成一滴雨"""
        rain = Rain(self)
        rain.rect.x += x_position # 设置间隔宽度
        rain.rect.y += y_position # 设置间隔宽度
        self.rains.add(rain) # 添加到编组里统一处理
        
    def _create_all_rains(self):
        """生成众多的雨滴"""
        rain = Rain(self) # 生成一个实例摸摸底
        # 获取雨滴图片的宽高
        rain_width, rain_height = rain.rect.width, rain.rect.height
        current_x = rain_width
        current_y = rain_height
        while current_y <= self.screen_rect.height / 30: # 绘制多排雨滴
            while current_x <= self.screen_rect.right - 2 * rain_width:
                self._create_rain(current_x, current_y) # 绘制一排雨滴
                current_x += rain_width * 2
            current_y += 2 * rain_height
            current_x = rain_width # 重制每一行的起点，绘制下一行
                

    def _full_sky_rains(self):
        # 启用游戏编组来管理雨滴，生成被编组的实例的类，需要继承 Sprite 类
        self.rains = pygame.sprite.Group()
        self._create_all_rains()

    def _check_rain_edge(self):
        """雨滴落出屏幕后，新生成雨滴"""
        for rain in self.rains:
            if rain.check_edge():
                self.rains.empty() # 清除已经落出屏幕的雨滴
                self._create_all_rains()
                break

    def rain_drops(self):
        """雨滴滑落"""
        self._check_rain_edge()
        self.rains.update()
        
    def _check_event(self):
        """检查事件"""
        for event in pygame.event.get():
            # 必须得添加游戏的退出相应，不然游戏就卡死了，游戏窗口都不显示了
            if event.type == pygame.QUIT:
                sys.exit()
        
    def run_game(self):
        """开始游戏的主循环"""
        while True: # 游戏是一个不断刷新的过程，所以启动后必须不断地更新屏幕才能正常渲染游戏
            self._check_event()
            self.screen.fill((230, 230, 230)) # 游戏背景色
            self.rains.draw(self.screen) # 绘制素材到屏幕上
            self.rain_drops()
            pygame.display.flip()
            self.clock.tick(60) # FPS



    
if __name__ == "__main__":
    sky = Sky()
    sky.run_game()