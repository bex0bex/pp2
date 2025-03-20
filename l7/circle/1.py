import pygame
pygame.init()
WIDTH, HEIGHT = 500, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Moving Ball")
WHITE = (255, 255, 255)
RED = (255, 0, 0)
ball_x, ball_y = WIDTH // 2, HEIGHT // 2
radius = 25
speed = 20  
running = True
while running:
    pygame.time.delay(50)  
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed() 
    if keys[pygame.K_LEFT] and ball_x - radius - speed >= 0:
        ball_x -= speed
    if keys[pygame.K_RIGHT] and ball_x + radius + speed <= WIDTH:
        ball_x += speed
    if keys[pygame.K_UP] and ball_y - radius - speed >= 0:
        ball_y -= speed
    if keys[pygame.K_DOWN] and ball_y + radius + speed <= HEIGHT:
        ball_y += speed
    screen.fill(WHITE)
    pygame.draw.circle(screen, RED, (ball_x, ball_y), radius)
    pygame.display.update()

pygame.quit()
