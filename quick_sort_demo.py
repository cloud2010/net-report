import pygame
import random

# 初始化Pygame
pygame.init()

# 设置窗口大小
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("快速排序演示")

# 设置颜色
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# 生成随机数组
array = [random.randint(10, height - 10) for _ in range(width // 10)]

def draw_array(arr, pivot_index=None, left_index=None, right_index=None):
    screen.fill(WHITE)
    for i, value in enumerate(arr):
        color = BLACK
        if i == pivot_index:
            color = RED
        elif i == left_index or i == right_index:
            color = GREEN
        pygame.draw.rect(screen, color, (i * 10, height - value, 10, value))
    pygame.display.update()

def quick_sort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
            draw_array(arr, high, i, j)
            pygame.time.delay(50)
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    # 这里的 j 可能在循环结束后未定义，使用 high - 1 替代
    draw_array(arr, high, i + 1, high - 1)
    pygame.time.delay(50)
    return i + 1

# 主循环
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    quick_sort(array, 0, len(array) - 1)
    draw_array(array)
    pygame.time.delay(1000)
    running = False

pygame.quit()