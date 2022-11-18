import pygame

from Setting import Settings

from ship import Ship

import eventFunction as ef

from pygame.sprite import Group


class Game:
    def __init__(self):
        # 初始化游戏以及资源
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption('Alien Invasion')

        # 设置背景
        self.bg_color = self.settings.bg_color
        self.ship = Ship(self.settings)
        # 创建一个编组Group，类似与列表，用于存储子弹
        self.bullets = Group()
        self.aliens = Group()
        # 创建一个外星人
        # self.alien = Alien(self.settings, self.screen)

    def run_game(self):
        pygame.init()  # 初始化游戏
        # 创建外星人
        ef.createAlienGroup(self.settings, self.screen, self.aliens, self.ship)
        # 开始游戏的主循环
        while True:
            ef.eventFunction(self.ship, self.settings, self.screen, self.bullets)
            self.ship.update_moving()
            ef.updateBullet(self.bullets, self.aliens)
            ef.updateAlien(self.settings, self.aliens, self.screen)
            ef.updateScreen(self.settings, self.screen, self.ship, self.bullets, self.aliens)


if __name__ == '__main__':
    ai = Game()
    ai.run_game()
