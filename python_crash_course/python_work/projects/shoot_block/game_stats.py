class GameStats:
    """管理飞船统计信息的类"""

    def __init__(self, ai_game):
        """初始化游戏统计信息"""
        self.settings = ai_game.settings
        self.rest_stats()

    def rest_stats(self):
        """重置游戏统计信息"""
        self.ship_left = self.settings.ship_limit
        self.alien_destroyed_num = 0
        self.fired_bullets_num = 0
        self.ship_collided_num = 0

    def minus_ship_num(self):
        """可用飞船数量减一"""
        self.ship_left -= 1
        # print(f"ship number is {self.ship_left}")

    def count_destroyed_blocks_num(self):
        """统计被消灭的标靶的数量"""
        self.settings.block_destroyed_num += 1

    def count_fired_bullets_num(self):
        """统计发射的子弹数量"""
        self.settings.fired_bullets_num += 1

    def count_ship_collided_num(self):
        """统计飞船被外星飞船撞毁的次数"""
        self.settings.ship_collided_num += 1
