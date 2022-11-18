import pygame

import sys

from bullet import Bullet

from alien import Alien


# 事件管理 响应鼠标事件与键盘事件

def eventKeydown(event, ship, ai_settings, screen, bullets):
    if event.key == pygame.K_RIGHT:
        # 飞船向右移动，按下键moving就为True
        ship.moving_right = True
    elif event.key == pygame.K_ESCAPE:
        sys.exit()
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        if len(bullets) < ai_settings.bullet_allowed:
            new_bullet = Bullet(ai_settings, ship, screen)
            bullets.add(new_bullet)


def eventKeyUp(event, ship):
    if event.key == pygame.K_RIGHT:
        # 松下键moving就改为False
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False


def eventFunction(ship, ai_settings, screen, bullets):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        # 按下键
        elif event.type == pygame.KEYDOWN:
            eventKeydown(event, ship, ai_settings, screen, bullets)
        elif event.type == pygame.KEYUP:
            eventKeyUp(event, ship)


def updateScreen(ai_settings, screen, ship, bullets, aliens):
    # 更新屏幕上的图像，每次切换到新屏幕
    # 每次循环都绘制新屏幕
    screen.fill(ai_settings.bg_color)
    # 在飞船和外星人后绘制子弹
    for bullet in bullets:
        bullet.drawBullet()
    ship.blitme()
    aliens.draw(screen)
    # draw 自动对编组的每个元素进行绘制，绘制位置由rect决定

    # 让绘制的屏幕可见

    pygame.display.flip()


def updateBullet(bullets, aliens):
    # 更新子弹的位置
    bullets.update()
    # 删除多余的子弹
    for bullet in bullets:
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    # 用groupcollide来检测两个编组是否有碰撞，并返回一个字典
    # 首先是遍历一遍编组bullets，然后遍历一遍aliens编组，每当有两个的rect值重叠（碰撞），就会返回字典中的一个键-值对，键为每一个子弹，值为被击倒的外星人，第一个TRUE为子弹的，第二个为外星人的，TRUE表示删除这个键值对
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)


def getNumberAlienRow(ai_settings, alien_width):
    # 计算每一行能容纳多少个外星人
    # 这一行能用的宽度
    availableRow = ai_settings.screen_width - 2 * alien_width
    # 在有限的宽度中，能容纳多少个外星人
    numberAlienRow = int(availableRow / (2 * alien_width))
    return numberAlienRow


def getNumerAlienHeight(ai_settings, ship_height, alien_height):
    # 计算屏幕能容纳多少行外星人
    # 有多少最大利用空间（高度）,可利用垂直空间：屏幕高度-第一行外星人的上边距（外星人的高度）-飞船高度-最初外星人群与飞船的距离（外星人高度两倍）
    availableHeightSpace = ai_settings.screen_width - 3 * alien_height - ship_height
    # 有多少行
    numberRow = int(availableHeightSpace / (4 * alien_height))
    return numberRow


def createAlien(ai_settings, screen, aliens, alien_number, row_number):
    # 创建一个外星人，并把它放在这行
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    # 外星人的x坐标,以此用rect来确定外星人位置
    alien.x = alien_width + alien_width * 2 * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)


def createAlienGroup(ai_settings, screen, aliens, ship):
    # 创建一个外星人的组
    # 创建一个外星人，并计算一行能容下多少个外星人
    alien = Alien(ai_settings, screen)
    alien_number_row = getNumberAlienRow(ai_settings, alien.rect.width)
    number_rows = getNumerAlienHeight(ai_settings, ship.rect.height, alien.rect.height)
    # 创建第一群外星人
    for number_row in range(number_rows):
        # 第一行
        for alien_number in range(alien_number_row):
            createAlien(ai_settings, screen, aliens, alien_number, number_row)


def updateAlien(ai_settings, aliens, screen):
    # 更新外星人,检查是否在屏幕边缘，并调整方向
    actionEdge(ai_settings, aliens, screen)
    aliens.update()


def actionEdge(ai_settings, aliens, screen):
    screen_rect = screen.get_rect()
    # 外星人到达边缘后的措施
    for alien in aliens:
        if alien.rect.right >= screen_rect.right or alien.rect.left <= 0:
            changeDirection(ai_settings, aliens)
            break


def changeDirection(ai_settings, aliens):
    # 到达边缘后，将外星人向下移动，并改变方向
    for alien in aliens:
        alien.rect.y += ai_settings.alien_down_speed
    ai_settings.alien_direction *= -1
