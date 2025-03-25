import pygame
import math

# 初始化 Pygame
pygame.init()

# 设置窗口尺寸
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Ball Bouncing in Rotating Shape")

# 定义颜色
WHITE = (255, 255, 255)
GRAY = (192, 192, 192)
BLUE = (0, 0, 255)

# 定义形状（正八边形）的属性
shape_radius = 200
shape_center = (width // 2, height // 2)
rotation_angle = 0
rotation_speed = 0.5

# 生成正八边形的顶点
def generate_octagon_vertices(radius, center, angle):
    num_sides = 8
    return [
        (
            center[0] + radius * math.cos(math.radians(i * 360 / num_sides + angle)),
            center[1] + radius * math.sin(math.radians(i * 360 / num_sides + angle))
        )
        for i in range(num_sides)
    ]

# 计算点到线段的距离
def calculate_distance_to_segment(point, start, end):
    dx = end[0] - start[0]
    dy = end[1] - start[1]
    if dx == 0 and dy == 0:
        return math.sqrt((point[0] - start[0])**2 + (point[1] - start[1])**2)
    
    t = ((point[0] - start[0]) * dx + (point[1] - start[1]) * dy) / (dx**2 + dy**2)
    t = max(0, min(1, t))
    closest_x = start[0] + t * dx
    closest_y = start[1] + t * dy
    return math.sqrt((point[0] - closest_x)**2 + (point[1] - closest_y)**2), (closest_x, closest_y)

# 反射速度
def reflect_velocity(velocity, normal):
    dot_product = velocity[0] * normal[0] + velocity[1] * normal[1]
    return [
        velocity[0] - 2 * dot_product * normal[0],
        velocity[1] - 2 * dot_product * normal[1]
    ]

# 定义球的属性
ball_radius = 10
ball_position = [shape_center[0], shape_center[1] - shape_radius + ball_radius]
ball_velocity = [2, 2]

# 游戏主循环
running = True
clock = pygame.time.Clock()
octagon_vertices = generate_octagon_vertices(shape_radius, shape_center, rotation_angle)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 旋转形状
    rotation_angle += rotation_speed
    octagon_vertices = generate_octagon_vertices(shape_radius, shape_center, rotation_angle)

    # 更新球的位置
    ball_position[0] += ball_velocity[0]
    ball_position[1] += ball_velocity[1]

    # 检查球是否超出屏幕边界
    if ball_position[0] - ball_radius < 0 or ball_position[0] + ball_radius > width:
        ball_velocity[0] = -ball_velocity[0]
    if ball_position[1] - ball_radius < 0 or ball_position[1] + ball_radius > height:
        ball_velocity[1] = -ball_velocity[1]

    # 检查球是否超出形状边界（简化的碰撞检测）
    for i in range(len(octagon_vertices)):
        start = octagon_vertices[i]
        end = octagon_vertices[(i + 1) % len(octagon_vertices)]
        distance, closest_point = calculate_distance_to_segment(ball_position, start, end)
        if distance < ball_radius:
            # 修正法线向量方向（原方向指向形状内部，现改为向外）
            normal = [ball_position[0] - closest_point[0], ball_position[1] - closest_point[1]]
            length = math.sqrt(normal[0]**2 + normal[1]**2)
            normal = [normal[0] / length, normal[1] / length]
            ball_velocity = reflect_velocity(ball_velocity, normal)

    # 绘制背景
    screen.fill(WHITE)

    # 绘制旋转后的正八边形
    pygame.draw.polygon(screen, GRAY, octagon_vertices)

    # 绘制球
    pygame.draw.circle(screen, BLUE, (int(ball_position[0]), int(ball_position[1])), ball_radius)

    # 更新显示
    pygame.display.flip()

    # 控制帧率
    clock.tick(60)

# 退出 Pygame
pygame.quit()