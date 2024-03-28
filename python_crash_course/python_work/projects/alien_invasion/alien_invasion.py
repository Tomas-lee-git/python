# 重构：先编写尽量简单、可运行的代码，再在代码越来越复杂时进行重构

import pygame  # 包含游戏开发所需的功能

import sys  # 使用 sys 模块的工具来退出游戏
from settings import Settings
from ship import Ship


class AlienInvasion:
    """管理游戏资源和行为的类"""

    def __init__(self):
        """初始化游戏并创建游戏资源"""
        pygame.init()  # 初始化游戏背景
        self.clock = pygame.time.Clock()  # 通过self.clock 控制游戏的帧率
        self.setting = Settings()
        # 把游戏窗口赋给 self.screen，让类的所有方法都能使用它
        self.screen = pygame.display.set_mode(
            (self.setting.default_screen_width, self.setting.default_screen_height)
        )

        pygame.display.set_caption(self.setting.display_caption)
        self.ship = Ship(self)

    def _into_full_screen(self, event):
        """进入全屏模式"""
        self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        self.setting.screen_width = self.screen.get_rect().width
        self.setting.screen_height = self.screen.get_rect().height
        
        # 目前有个问题，切换为全屏后，飞船位置没有在底部中间位置
        # self.ship.rect.midbottom = self.ship.screen_rect.midbottom
        # self.ship.blitme()
            
    def _exit_full_screen(self, event):
        """退出全屏模式"""
        self.screen = pygame.display.set_mode(
            (self.setting.default_screen_width, self.setting.default_screen_height)
        )
    
    def _check_down(self, event):
        """响应按下"""
        if event.key == pygame.K_RIGHT: # 按右箭头，激活向右移动标识
            self.ship.moving_right = True 
        elif event.key == pygame.K_LEFT: # 按左箭头，激活向左移动标识
            self.ship.moving_left = True
        elif event.key == pygame.K_DOWN: # 按下箭头，激活向下移动标识
            self.ship.moving_down = True
        elif event.key == pygame.K_UP: # 按上箭头，激活向上移动标识
            self.ship.moving_up = True
        elif event.key == pygame.K_q: # 按 Q 退出游戏
            sys.exit()
        elif event.key == pygame.K_F12: # f12 进入全屏
            self._into_full_screen(event)
        elif event.key == pygame.K_ESCAPE: # esc 退出全屏
            self._exit_full_screen(event)
        
        
        
    def _check_up(self, event):
        """响应释放"""
        if event.key == pygame.K_RIGHT: # 按右箭头，关闭向右移动标识
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT: # 按下箭头，关闭向下移动标识
            self.ship.moving_left = False
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = False # 按上箭头，关闭向上移动标识
        elif event.key == pygame.K_UP:
            self.ship.moving_up = False # 按左箭头，关闭向左移动标识

    # 拆分为辅助方法：1. 以_开头；2. 只会在类的内部使用；
    def _check_events(self):
        """侦听键盘和鼠标事件"""
        for event in pygame.event.get():  # 访问 Pygame 检测到的，包含所有事件的列表
            print(f"event is {event}")
            # 检测并响应特定的事件
            if event.type == pygame.QUIT:
                sys.exit()  # while True 的退出条件，退出游戏程序
            elif event.type == pygame.KEYDOWN: # 侦听“键盘按键按下”事件
                self._check_down(event)
            elif event.type == pygame.KEYUP: # 侦听“键盘按键释放”事件
                self._check_up(event)

    def _update_screen(self):
        """更新屏幕的相关操作"""
        self.screen.fill(self.setting.bg_color)  # 每次循环时都重绘屏幕
        self.ship.blitme()

        # 根据用户操作不断地更新屏幕显示
        pygame.display.flip()

    def run_game(self):
        """开始游戏的主循环"""
        while True:  # 持续不断地侦听，直到退出游戏
            self._check_events() # 类中定义的属性和方法都可以通过 self 来访问和调用
            self._update_screen()
            self.ship.update() # 移动飞船，起点在左上角(0,0)
            self.clock.tick(self.setting.frame_rate)


if __name__ == "__main__":  # 仅当直接运行该文件时，包含的代码才会被执行
    # 创建游戏实例并运行游戏
    ai = AlienInvasion()
    ai.run_game()
