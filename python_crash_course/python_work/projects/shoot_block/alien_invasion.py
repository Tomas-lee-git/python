# 重构：先编写尽量简单、可运行的代码，再在代码越来越复杂时进行重构

import pygame  # 包含游戏开发所需的功能

import sys  # 使用 sys 模块的工具来退出游戏
from time import sleep  # 暂停游戏

from settings import Settings
from ship import Ship
from bullet import Bullet
from game_stats import GameStats
from block import Block
from button import Button


class HorizontalAlienInvasion:
    """管理横屏游戏资源和行为的类"""

    def __init__(self):
        """初始化游戏并创建游戏资源"""
        pygame.init()  # 初始化游戏背景
        self.clock = pygame.time.Clock()  # 通过self.clock 控制游戏的帧率
        self.settings = Settings()
        # 把游戏窗口赋给 self.screen，让类的所有方法都能使用它
        self.screen = pygame.display.set_mode(
            (self.settings.default_screen_width, self.settings.default_screen_height)
        )

        pygame.display.set_caption(self.settings.display_caption)
        self.screen_rect = self.screen.get_rect()

        # 游戏统计信息
        self.stats = GameStats(self)
        
        self.play_button = Button(self, "Play")

        # 游戏是否正常进行
        self.game_active = False

        self.ship = Ship(self)
        # 创建存储子弹的编组（类似列表，但提供了有助于开发游戏的额外功能）
        self.bullets = pygame.sprite.Group()
        self.block = Block(self)

    def _into_full_screen(self, event):
        """进入全屏模式"""
        pygame.display.toggle_fullscreen()
        # self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        # self.settings.screen_width = self.screen.get_rect().width
        # self.settings.screen_height = self.screen.get_rect().height

        # 目前有个问题，切换为全屏后，飞船位置没有在底部中间位置
        # self.ship.rect.midbottom = self.ship.screen_rect.midbottom
        # self.ship.blitme()

    def _exit_full_screen(self, event):
        """退出全屏模式"""
        pygame.display.toggle_fullscreen()
        # self.screen = pygame.display.set_mode(
        #     (self.settings.default_screen_width, self.settings.default_screen_height)
        # )

    # def _add_bullet(self):
    #     """添加 bullet """
    #     new_bullet = Bullet(self)
    #     self.bullets.add(new_bullet)

    def _fire_bullet(self):
        """创建一颗子弹，并将其加入编组 bullets"""
        if self.game_active:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)
            self.stats.count_fired_bullets_num()

        # TODO: 持续开火功能
        # if self.settings.is_firing:
        # my_scheduler = sched.scheduler(time.time, time.sleep) # 设置定时器
        # my_scheduler.enter(60, 1, self._add_bullet, (my_scheduler,))
        # my_scheduler.run()

    def _remove_bullet(self):
        """删除飞出屏幕外的子弹"""
        for bullet in self.bullets.copy():  # 使用列表的 copy 来完成对列表元素的删除
            if (
                bullet.rect.x >= self.screen_rect.right
            ):  # x 轴位置大于游戏窗口右侧位置，就是飞出了屏幕，需要删除
                self.bullets.remove(bullet)
        # if self.bullets:
        #     print(f"bullets length is {len(self.bullets)}")

    def _update_bullets(self):
        """更新子弹位置并删除已消失的子弹"""
        # 在对编组调用 update()时，编组会自动对其中的每个 sprite 调用 update()
        # 也就是更新子弹编组中的每一颗子弹的位置
        self.bullets.update()
        self._remove_bullet()
        self._check_collision_bullet_block()
        

    def _keyboard_down(self, event):
        """响应按下"""
        if event.key == pygame.K_DOWN:  # 按下箭头，激活向下移动标识
            self.ship.moving_down = True
        elif event.key == pygame.K_UP:  # 按上箭头，激活向上移动标识
            self.ship.moving_up = True
        elif event.key == pygame.K_q:  # 按 Q 退出游戏
            sys.exit()
        elif event.key == pygame.K_F12:  # f12 进入全屏
            self._into_full_screen(event)
        elif event.key == pygame.K_ESCAPE:  # esc 退出全屏
            self._exit_full_screen(event)
        elif event.key == pygame.K_SPACE:  # 空格键开火
            self._fire_bullet()

    def _keyboard_up(self, event):
        """响应释放"""
        if event.key == pygame.K_DOWN:
            self.ship.moving_down = False  # 按上箭头，关闭向上移动标识
        elif event.key == pygame.K_UP:
            self.ship.moving_up = False  # 按左箭头，关闭向左移动标识
        # elif event.key == pygame.K_SPACE:  # 松开空格键停火
        #     self.settings.is_firing = False

    def _check_click_play_button(self, mos_position):
        """检查是否点击了 Play 按钮"""
        if self.play_button.rect.collidepoint(mos_position):
            print("play button has been clicked")
            self.game_active = True
            self.stats.rest_stats()

    
    def _mouse_down(self, event):
        """检测鼠标点击事件"""
        mos_position = pygame.mouse.get_pos() # 获取鼠标点击的位置
        self._check_click_play_button(mos_position)
    
    # 拆分为辅助方法：1. 以_开头；2. 只会在类的内部使用；
    def _check_events(self):
        """侦听键盘和鼠标事件"""
        for event in pygame.event.get():  # 访问 Pygame 检测到的，包含所有事件的列表
            # print(f"event is {event}")
            # 检测并响应特定的事件
            if event.type == pygame.QUIT:
                sys.exit()  # while True 的退出条件，退出游戏程序
            elif event.type == pygame.KEYDOWN:  # 侦听“键盘按键按下”事件
                self._keyboard_down(event)
            elif event.type == pygame.KEYUP:  # 侦听“键盘按键释放”事件
                self._keyboard_up(event)
            elif event.type == pygame.MOUSEBUTTONDOWN: # 侦听“鼠标点击”事件
                self._mouse_down(event)

    def _restart_or_over_game(self):
        """重新开始一轮游戏，或者游戏结束"""
        if self.stats.ship_left > 1:  # 还有剩余飞船，重开游戏
            self.stats.minus_ship_num()
            self.bullets.empty()
            sleep(0.5)
        else:  # 没有剩余飞船，游戏结束
            self.game_active = False

        if not self.game_active:
            print(f"fired bullets are {self.settings.fired_bullets_num}")
            print(f"collided ship are {self.settings.ship_collided_num}")

    def _draw_bullets(self):
        """绘制每一颗子弹"""
        for bullet in self.bullets:
            bullet.draw_bullet()

    def _update_block(self):
        """更新标靶的位置"""
        if self.block._check_y_edge(): # 如果即将超出屏幕，就调转方向
            self.settings.block_direction *= -1
        self.block.update()

    def _check_collision_bullet_block(self):
        """检测子弹是否击中标靶"""
        collision = pygame.sprite.spritecollide( self.block,self.bullets, True)
        if collision: # 击中之后得一分
            self.settings.block_destroyed_num += 1
        
        # 如果玩家三次未击中目标，游戏结束
        if self.settings.fired_bullets_num == 3 and self.settings.block_destroyed_num == 0:
            self.game_active = False
            
    def _draw_screen(self):
        """绘制屏幕上的图像，并且换到新屏幕"""
        self.screen.fill(self.settings.bg_color)  # 每次循环时都重绘屏幕
        self.ship.blitme()
        self._draw_bullets()
        self.block.draw_block()
        if not self.game_active: # 游戏非活跃时，显示 Play 按钮
            self.play_button.draw_button()

        # 根据用户操作不断地更新屏幕显示
        pygame.display.flip()

    def run_game(self):
        """开始游戏的主循环"""
        while True:  # 持续不断地侦听，直到退出游戏
            self._check_events()  # 类中定义的属性和方法都可以通过 self 来访问和调用

            if self.game_active:  # 游戏结束之后，就不需要更新游戏活动的素材元素了
                self.ship.update()  # 起点在左上角(0,0)
                self._update_bullets()
                self._update_block()

            self._draw_screen()
            self.clock.tick(self.settings.frame_rate)


if __name__ == "__main__":  # 仅当直接运行该文件时，包含的代码才会被执行
    # 创建游戏实例并运行游戏
    ai = HorizontalAlienInvasion()
    ai.run_game()
