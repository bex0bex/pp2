import pygame
import sys
import math
import datetime

pygame.init()

WIDTH, HEIGHT = 500, 500
CENTER = (WIDTH // 2, HEIGHT // 2)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mickey Clock")

background = pygame.image.load("l7/clock/mickeyclock.jpeg")
background = pygame.transform.scale(background, (WIDTH, HEIGHT))

clock = pygame.time.Clock()

def get_rotated_point(center, length, angle_deg):
    angle_rad = math.radians(angle_deg)
    x = center[0] + length * math.sin(angle_rad)
    y = center[1] - length * math.cos(angle_rad)
    return (int(x), int(y))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    now = datetime.datetime.now()
    seconds = now.second
    minutes = now.minute

    
    second_angle = (seconds / 60) * 360
    minute_angle = (minutes / 60) * 360

    screen.blit(background, (0, 0))

    sec_end = get_rotated_point(CENTER, 180, second_angle)
    pygame.draw.line(screen, (255, 0, 0), CENTER, sec_end, 4)

    min_end = get_rotated_point(CENTER, 120, minute_angle)
    pygame.draw.line(screen, (0, 0, 0), CENTER, min_end, 8)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
