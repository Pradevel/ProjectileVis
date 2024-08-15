import pygame
import math

pygame.init()
HEIGHT = 600
WIDTH = 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Projectile")


x, y = 100, 550
radius = 20
v = int(input("Velocity :"))
a = math.radians(int(input("Degree: ")))
g = int(input("Gravity: "))
t = 0

clock = pygame.time.Clock()
dt = 0.1

vx = v * math.cos(a)
vy = -v * math.sin(a)

running = True
while running:
    clock.tick(60)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    t += dt
    x = 100 + vx * t
    y = HEIGHT - 50 + vy * t + 0.5 * g * t ** 2
    if y >= HEIGHT - 50:
        y = HEIGHT - 50
        t = 0

    screen.fill((255, 255, 255))
    pygame.draw.circle(screen, (255, 165, 0), (int(x), int(y)), radius)
    pygame.display.flip()

pygame.quit()