import pygame


class Ship:
    def __init__(self, ai_settings):
        # 初始化飞船并设置飞船初始化位置
        self.settings = ai_settings
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        self.screen.fill((230, 230, 230))
        # 加载飞船图像并获取其外接矩形
        self.image = pygame.image.load('images/ship.png')
        # 飞船的位置
        self.rect = self.image.get_rect()
        # 屏幕的位置
        self.screen_rect = self.screen.get_rect()

        # 将每搜新飞船放在屏幕底部中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # 将飞船的center中存储小数值，centerx只能存储整数，小数值的移动能让游戏更细致移动
        self.center = float(self.rect.centerx)

        # 飞船动不动的标志
        self.moving_right = False
        self.moving_left = False

    def blitme(self):
        # 在指定位置绘制飞船位置
        self.screen.blit(self.image, self.rect)

    def update_moving(self):
        # 根据移动的标志调整飞船的位置
        # 调整center的值而不是rect，从而更细致的移动
        if self.moving_right and (self.rect.right < self.screen_rect.right):
            self.center += self.settings.ship_speed
        if self.moving_left and (self.rect.left > 0):
            self.center -= self.settings.ship_speed

        # 通过center来改变rect的值，来改变移动位置
        self.rect.centerx = self.center
