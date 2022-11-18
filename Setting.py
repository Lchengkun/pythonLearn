class Settings:
    # 存储游戏所有设置的类
    def __init__(self):
        # 初始化

        # 屏幕设置
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # 飞船的属性设置

        # 每次循环飞船最多移动
        self.ship_speed = 1.5

        # 子弹设置
        self.bullet_speed = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullet_allowed = 5

        # 外星人设置
        self.alien_speed = 1
        # 外星人碰到屏幕边缘后，外星人向下的速度
        self.alien_down_speed = 10
        # 外星人移动方向，1为右，-1为左
        self.alien_direction = 1
