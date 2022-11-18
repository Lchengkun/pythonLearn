import pygame

from pygame.sprite import Sprite


class Bullet(Sprite):
    # 飞船对子弹管理的类
    def __init__(self, ai_settings, ship, screen):
        super(Bullet, self).__init__()
        self.screen = screen

        # 在(0,0)处创建一个子弹矩形，再设置一个正确的位置 (左，上，宽，高)
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width, ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        # 储存用小数表示子弹的位置
        self.y = float(self.rect.y)
        self.color = ai_settings.bullet_color
        self.speed = ai_settings.bullet_speed

    # 每次子弹更新
    def update(self):
        # 向上移动子弹
        # 更新表示子弹位置的小数值
        self.y -= self.speed

        # 用小数值的y更新子弹的rect位置
        self.rect.y = self.y

    def drawBullet(self):
        # 绘制屏幕中的子弹
        pygame.draw.rect(self.screen, self.color, self.rect)
