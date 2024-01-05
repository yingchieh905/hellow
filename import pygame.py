import pygame
import sys
import random

# 初始化 Pygame
pygame.init()

# 設定遊戲視窗大小
window_width = 800
window_height = 600
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("射擊遊戲")

# 設定顏色
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

# 設定玩家和敵人的大小和速度
player_size = 50
player_speed = 5
enemy_size = 50
enemy_speed = 3

# 創建玩家
player = pygame.Rect(window_width // 2 - player_size // 2, window_height - player_size - 10, player_size, player_size)

# 創建敵人列表
enemies = []

# 設定計分
score = 0

# 設定字體
font = pygame.font.Font(None, 36)

# 主遊戲迴圈
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player.left > 0:
        player.x -= player_speed
    if keys[pygame.K_RIGHT] and player.right < window_width:
        player.x += player_speed

    # 移動敵人
    for enemy in enemies:
        enemy.y += enemy_speed
        if enemy.y > window_height:
            enemies.remove(enemy)
            score += 1

    # 生成新的敵人
    if random.randint(1, 10) == 1:
        enemy = pygame.Rect(random.randint(0, window_width - enemy_size), 0, enemy_size, enemy_size)
        enemies.append(enemy)

    # 檢查碰撞
    for enemy in enemies:
        if player.colliderect(enemy):
            pygame.quit()
            sys.exit()

    # 清空畫面
    window.fill(white)

    # 畫玩家
    pygame.dr
