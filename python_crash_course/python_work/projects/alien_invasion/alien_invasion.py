# 重构：先编写尽量简单、可运行的代码，再在代码越来越复杂时进行重构

import pygame  # 包含游戏开发所需的功能

import sys  # 使用 sys 模块的工具来退出游戏
import sched, time

from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien


class AlienInvasion:
    """管理游戏资源和行为的类"""

    def __init__(self):
        """初始化游戏并创建游戏资源"""
        pygame.init()  # 初始化游戏背景
        self.clock = pygame.time.Clock()  # 通过self.clock 控制游戏的帧率
        self.settings = Settings()
        # 把游戏窗口赋给 self.screen，让类的所有方法都能使用它
        self.screen = pygame.display.set_mode(
            (self.settings.default_screen_width, self.settings.default_screen_height)
        )
        self.screen_rect = self.screen.get_rect()
        pygame.display.set_caption(self.settings.display_caption)
        self.ship = Ship(self)
        # 创建存储子弹的编组（类似列表，但提供了有助于开发游戏的额外功能）
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        # 和子弹不同，外星人的出现是自动的，不依赖用户的按键操作，所以在__init__中直接调用
        self._create_fleet()

    def _into_full_screen(self, event):  # TODO: 全屏切换功能
        """进入全屏模式"""
        pygame.display.toggle_fullscreen()
        # self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        # self.settings.screen_width = self.screen.get_rect().width
        # self.settings.screen_height = self.screen.get_rect().height

        # 目前有个问题，切换为全屏后，飞船位置没有在底部中间位置
        # self.ship.rect.midbottom = self.ship.screen_rect.midbottom
        # self.ship.blitme()

    def _exit_full_screen(self, event):  # TODO: 全屏切换功能
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
        new_bullet = Bullet(self)
        self.bullets.add(new_bullet)

        # TODO: 持续开火功能
        # if self.settings.is_firing:
        # my_scheduler = sched.scheduler(time.time, time.sleep) # 设置定时器
        # my_scheduler.enter(60, 1, self._add_bullet, (my_scheduler,))
        # my_scheduler.run()

    def _remove_bullet(self):
        """删除飞出屏幕外的子弹"""
        for bullet in self.bullets.copy():  # 使用列表的 copy 来完成对列表元素的删除
            if bullet.rect.y <= 0:  # y 轴位置低于0，就是飞出了屏幕，需要删除
                self.bullets.remove(bullet)
        # print(f"bullets length is {len(self.bullets)}")

    def _update_bullets(self):
        """更新子弹位置并删除已消失的子弹"""
        # 在对编组调用 update()时，编组会自动对其中的每个 sprite 调用 update()
        # 也就是更新子弹编组中的每一颗子弹的位置
        self.bullets.update()
        self._remove_bullet()

    def _update_aliens(self):
        """更新每一艘飞船的位置"""
        self.aliens.update() # 对编组调用方法，会调用每一个飞船的 update 方法
    
    def _check_down(self, event):
        """响应按下"""
        if event.key == pygame.K_RIGHT:  # 按右箭头，激活向右移动标识
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:  # 按左箭头，激活向左移动标识
            self.ship.moving_left = True
        elif event.key == pygame.K_DOWN:  # 按下箭头，激活向下移动标识
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

    def _check_up(self, event):
        """响应释放"""
        if event.key == pygame.K_RIGHT:  # 按右箭头，关闭向右移动标识
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:  # 按下箭头，关闭向下移动标识
            self.ship.moving_left = False
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = False  # 按上箭头，关闭向上移动标识
        elif event.key == pygame.K_UP:
            self.ship.moving_up = False  # 按左箭头，关闭向左移动标识
        # elif event.key == pygame.K_SPACE:  # 松开空格键停火
        #     self.settings.is_firing = False

    # 拆分为辅助方法：1. 以_开头；2. 只会在类的内部使用；
    def _check_events(self):
        """侦听键盘和鼠标事件"""
        for event in pygame.event.get():  # 访问 Pygame 检测到的，包含所有事件的列表
            # print(f"event is {event}")
            # 检测并响应特定的事件
            if event.type == pygame.QUIT:
                sys.exit()  # while True 的退出条件，退出游戏程序
            elif event.type == pygame.KEYDOWN:  # 侦听“键盘按键按下”事件
                self._check_down(event)
            elif event.type == pygame.KEYUP:  # 侦听“键盘按键释放”事件
                self._check_up(event)

    def _create_alien(self, x_position, y_position):
        """根据 x, y 位置，实例化创建一个外星人"""
        # 做两件事：1. 创建外星人实例；2. 计算并赋值外星人位置
        new_alien = Alien(self)  # 生成外星人实例
        new_alien.x, new_alien.y = x_position, y_position  # 外星人 x 轴， y 轴位置
        # 更新外星人 x 轴,  y 轴位置
        new_alien.rect.x, new_alien.rect.y = new_alien.x, new_alien.y
        self.aliens.add(new_alien)  # 添加到外星人组中

    def _create_fleet(self):
        """创建一个外星舰队"""
        """
            添加一行外星人心得：
                1. 如果有一个任务，需要不断地做，直到触发某种停止机制，那应该本能地想到用
                    while condition 来实现；
                2. 原本的条件写的是：x_position < self.screen_rect.width，但这样会
                    有一个问题，没有留冗余量，会导致末尾的外星人超出屏幕；
                3. 因为第一个外星人留了自身宽度的左边距，那最后一个也需要留同样的右边距，
                    所以安全距离需要的冗余量为： 2 * 外星人自身宽度
        """
        alien = Alien(self)  # 先创建一个外星人实例，记录外星人的宽度
        alien_width, alien_height = alien.rect.size  # return tuple (width, size)
        # 动态存储每一个外星人 x, 每一行外星人 y 轴的位置
        current_x, current_y = alien_width, alien_height
        # while 循环创建多行外星人，留出飞船操作空间，不然上来就把飞船碰死了😅
        while current_y < self.screen_rect.height / 3 - 3 * alien_height:
            # while 循环创建一行外星人；
            while current_x < (
                self.screen_rect.width - 2 * alien_width
            ):  # 留出两边间距的位置
                self._create_alien(current_x, current_y)
                current_x += 2 * alien_width  # 间隔[一个外星人的宽度]放置另一个外星人
            # ❕ 重置 current_x，否则current_x停留在最大值，无法在下一行开启内部 while 循环
            current_x = alien_width
            current_y += 2 * alien_height  # 间隔[一个外星人的高度]放置另一行外星人

    def _draw_bullets(self):
        """绘制每一颗子弹"""
        for bullet in self.bullets:
            bullet.draw_bullet()

    def _update_screen(self):
        """更新屏幕上的图像，并且换到新屏幕"""
        self.screen.fill(self.settings.bg_color)  # 每次循环时都重绘屏幕
        self._draw_bullets()
        self.ship.blitme()
        self.aliens.draw(self.screen) # draw all sprites onto the surface
        pygame.display.flip() # 根据用户操作不断地更新屏幕显示

    def run_game(self):
        """开始游戏的主循环"""
        while True:  # 持续不断地侦听，直到退出游戏
            self._check_events()  # 类中定义的属性和方法都可以通过 self 来访问和调用
            self.ship.update()  # 起点在左上角(0,0)
            self._update_bullets()
            self._update_aliens()
            self._update_screen()
            self.clock.tick(self.settings.frame_rate)


if __name__ == "__main__":  # 仅当直接运行该文件时，包含的代码才会被执行
    # 创建游戏实例并运行游戏
    ai = AlienInvasion()
    ai.run_game()
