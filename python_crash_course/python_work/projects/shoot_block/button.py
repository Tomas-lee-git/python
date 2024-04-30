import pygame

class Button:
    """管理按钮的类"""
    
    def __init__(self, ai_game, msg):
        """初始化按钮"""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen_rect
        
        # 设置按钮的尺寸和其它属性
        self.width, self.height = 200, 50
        self.button_color =(0, 135, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)
        
        self.rect = pygame.Rect(0, 0, self.width, self.height) # 创建按钮
        self.rect.center = self.screen_rect.center # 按钮在屏幕上居中
        
        # 创建按钮上的文字
        self._pre_msg(msg)
        
    def _pre_msg(self, msg):
        """把文字 msg 渲染为图像"""
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center # 文字在按钮中居中显示
        
    def draw_button(self):
        """绘制一个用颜色填充的按钮，再绘制文本"""
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)
