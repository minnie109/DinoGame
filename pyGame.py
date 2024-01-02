import pygame
import sys
import random

# 初始化 Pygame
pygame.init()

# 設置遊戲視窗大小
WIDTH, HEIGHT = 800, 600
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Click the Box Game")

# 設定顏色
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# 設定方塊初始位置和大小
box_width, box_height = 50, 50
box_x, box_y = random.randint(0, WIDTH - box_width), random.randint(0, HEIGHT - box_height)

# 設定計時器
clock = pygame.time.Clock()
start_time = pygame.time.get_ticks()

running = True
while running:
    # 畫面更新速率
    clock.tick(60)

    # 監聽事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if box_x <= mouse_x <= box_x + box_width and box_y <= mouse_y <= box_y + box_height:
                end_time = pygame.time.get_ticks()
                print(f"You clicked the box! Your time: {(end_time - start_time) / 1000:.2f} seconds.")
                box_x, box_y = random.randint(0, WIDTH - box_width), random.randint(0, HEIGHT - box_height)
                start_time = pygame.time.get_ticks()

    # 填滿視窗為白色
    win.fill(WHITE)

    # 畫方塊
    pygame.draw.rect(win, RED, (box_x, box_y, box_width, box_height))

    # 更新視窗
    pygame.display.update()

# 關閉 Pygame
pygame.quit()
sys.exit()