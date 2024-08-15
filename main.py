import pygame
import math

try:
    pygame.init()
    HEIGHT = 700
    WIDTH = 900
    screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
    pygame.display.set_caption("Projectile Motion Visualization")

    x = 100
    y = HEIGHT - 200
    radius = 20
    v = int(input("Velocity: "))
    a = math.radians(int(input("Degree: ")))
    g = int(input("Gravity: "))
    t = 0

    clock = pygame.time.Clock()
    dt = 0.1

    vx = v * math.cos(a)
    vy = -v * math.sin(a)

    trajectory = []

    running = True
    simulation_running = True

    font = pygame.font.Font(None, 36)

    while running:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        if simulation_running:
            t += dt
            x = 100 + vx * t
            y = HEIGHT - 50 + vy * t + 0.5 * g * t ** 2

            trajectory.append((int(x), int(y)))

            if y >= HEIGHT - 50:
                y = HEIGHT - 50
                simulation_running = False

        screen.fill((255, 255, 255))

        if len(trajectory) > 1:
            pygame.draw.lines(screen, (255, 165, 0), False, trajectory, 2)

        pygame.draw.circle(screen, (255, 165, 0), (int(x), int(y)), radius)

        if not simulation_running:
            time_text = font.render(f"Time: {t:.2f} seconds", True, (0, 0, 0))
            screen.blit(time_text, (WIDTH // 2 - time_text.get_width() // 2, HEIGHT // 2 - time_text.get_height() // 2))

        pygame.display.flip()

    pygame.quit()

except pygame.error as e:
    print(f"Pygame encountered an error: {e}")