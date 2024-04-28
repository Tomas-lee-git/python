import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """实现外星人的类"""

    def __init__(self, ai_game):
        super().__init__()  # 子类继承时不要忘了这个，不然实例化时会报错
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings
        self.image = pygame.image.load("./images/alien.bmp")
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

    def check_edge(self):
        """检测外星人是否超出屏幕上、下边缘"""
        return (self.rect.top <= 0) or (self.rect.bottom >= self.screen_rect.bottom)

    def update(self):
        """外星人移动上、下移动"""
        self.rect.y += self.settings.alien_speed * self.settings.alien_direction
