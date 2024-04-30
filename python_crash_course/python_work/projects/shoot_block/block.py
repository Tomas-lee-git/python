import pygame

class Block:
    """管理标靶的类"""
    
    def __init__(self, ai_game):
        """初始化标靶"""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen_rect
        self.settings = ai_game.settings
        
        # 设置标靶的尺寸和其它属性
        self.width, self.height = 50, 100
        self.block_color = (170, 238, 187)
        
        # 创建标靶，使它在屏幕右边缘的中间位置
        left_position = self.screen_rect.right - self.width
        top_position =  self.screen_rect.bottom / 2  - self.height / 2
        self.rect = pygame.Rect(left_position, top_position, self.width, self.height)
        
    def draw_block(self):
        """绘制一个用颜色填充的标靶，再绘制文本"""
        self.screen.fill(self.block_color, self.rect)
        
    def _check_y_edge(self):
        """检测标靶在Y轴方向上是否超出了屏幕"""
        over_bottom = self.rect.bottom >= self.screen_rect.bottom
        over_top = self.rect.top <= 0
        return over_bottom or over_top
    
    def update(self):
        """标靶上下移动"""
        self.rect.y += self.settings.block_speed * self.settings.block_direction
        