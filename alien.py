import pygame

from pygame.sprite import Sprite


class Alien(Sprite):
    # 表示单个外星人的类
    # 初始化外星人设置，并初始化位置
    def __init__(self, ai_settings, screen):
        super(Alien, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # 加载外星人图像， 并设置rect位置
        self.image = pygame.image.load("images/alien.png")
        self.rect = self.image.get_rect()

        # 每个外星人最开始都在屏幕左上角附近
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # 存储外星人的准确位置,用小数值表示，更细致
        self.x = float(self.rect.x)

    def blitme(self):
        # 在屏幕上绘制外星人
        self.screen.blit(self.image, self.rect)

    def update(self):
        # 外星人向右或向左移动,用x小数更细致移动，再更新rect
        self.x += (self.ai_settings.alien_speed * self.ai_settings.alien_direction)
        self.rect.x = self.x


