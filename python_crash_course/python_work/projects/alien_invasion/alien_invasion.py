import pygame # 包含游戏开发所需的功能

import sys # 使用 sys 模块的工具来退出游戏
from settings import Settings

class AlienInvasion:
    """管理游戏资源和行为的类"""
    def __init__(self):
        """初始化游戏并创建游戏资源"""
        pygame.init() # 初始化游戏背景
        self.clock = pygame.time.Clock() # 通过self.clock 控制游戏的帧率
        self.setting = Settings()
        # 把游戏窗口赋给 self.screen，让类的所有方法都能使用它
        self.screen = pygame.display.set_mode(self.setting.screen)
        pygame.display.set_caption(self.setting.display_caption)

    def run_game(self):
        """开始游戏的主循环"""
        while True: # 持续不断地侦听，直到退出游戏
            # 侦听键盘和鼠标事件
            for event in pygame.event.get(): # 访问 Pygame 检测到的，包含所有事件的列表
                # print(f"event is {event}")
                if event.type == pygame.QUIT:
                    sys.exit() # while True 的退出条件，退出游戏程序
                # 编写一系列的 if 语句来检测并响应特定的事件
                
            self.screen.fill(self.setting.bg_color) # 每次循环时都重绘屏幕

            # 根据用户操作不断地更新屏幕显示
            pygame.display.flip()
            self.clock.tick(self.setting.frame_rate)

if __name__ == "__main__": # 仅当直接运行该文件时，包含的代码才会被执行
    # 创建游戏实例并运行游戏
    ai = AlienInvasion()
    ai.run_game()
