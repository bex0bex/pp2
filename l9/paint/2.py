import pygame
import os















# Screen setup &&&
screen = pygame.display.set_mode((900, 700))
screen.fill((255, 255, 255))

os.chdir(r"C:\Users\user\Desktop\pp\l9\paint")
# Set window title&
pygame.display.set_caption('GFG Paint')

draw_on = False
last_pos = (0, 0)
radius = 5

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
LIGHTGREEN = (144, 238, 144)
GREEN = (102, 204, 0)
BLUE = (51, 51, 255)
BLACK = (0, 0, 0)
BROWM = (88, 57, 39)
color = BLACK  # Default color

# Color palette on screen
pygame.draw.rect(screen, RED, (0, 50, 20, 20))
pygame.draw.rect(screen, LIGHTGREEN, (0, 70, 20, 20))
pygame.draw.rect(screen, GREEN, (20, 50, 20, 20))
pygame.draw.rect(screen, BLUE, (20, 70, 20, 20))
pygame.draw.rect(screen, BLACK, (0, 90, 20, 20))
pygame.draw.rect(screen, BROWM, (20, 90, 20, 20))
erasor = pygame.transform.scale(pygame.image.load('png-clipart-drawing-eraser-computer-icons-eraser-angle-photography.png'), (40, 40))
screen.blit(erasor, [0, 110])

# Function to draw lines with rounded ends
def roundline(canvas, color, start, end, radius=1):
    Xaxis = end[0] - start[0]   
    Yaxis = end[1] - start[1]
    dist = max(abs(Xaxis), abs(Yaxis))
    for i in range(dist):
        x = int(start[0] + float(i) / dist * Xaxis)
        y = int(start[1] + float(i) / dist * Yaxis)
        pygame.draw.circle(canvas, color, (x, y), radius)

# Function to draw a square
def draw_square(surface, color, position, size):
    pygame.draw.rect(surface, color, (position[0], position[1], size, size))

# Function to draw a right triangle
def draw_right_triangle(surface, color, position, base, height):
    points = [(position[0], position[1]), 
              (position[0] + base, position[1]), 
              (position[0], position[1] - height)]
    pygame.draw.polygon(surface, color, points)

# Function to draw an equilateral triangle
def draw_equilateral_triangle(surface, color, position, side_length):
    height = (3 ** 0.5 / 2) * side_length  # Calculate height using Pythagoras
    points = [(position[0], position[1] - height),  # Top vertex
              (position[0] - side_length / 2, position[1] + height / 2),  # Bottom left
              (position[0] + side_length / 2, position[1] + height / 2)]  # Bottom right
    pygame.draw.polygon(surface, color, points)

# Function to draw a rhombus
def draw_rhombus(surface, color, position, size):
    points = [(position[0], position[1] - size),  # Top
              (position[0] + size, position[1]),  # Right
              (position[0], position[1] + size),  # Bottom
              (position[0] - size, position[1])]  # Left
    pygame.draw.polygon(surface, color, points)

try:
    while True:
        e = pygame.event.wait()

        if e.type == pygame.QUIT:
            raise StopIteration
        key = pygame.key.get_pressed()
        if e.type == pygame.MOUSEBUTTONDOWN:
            spot = pygame.mouse.get_pos()
            if spot[0] < 20 and 50 < spot[1] < 70:
                color = RED
            elif 20 < spot[0] < 40 and 50 < spot[1] < 70:
                color = GREEN
            elif spot[0] < 20 and 70 < spot[1] < 90:
                color = LIGHTGREEN
            elif 20 < spot[0] < 40 and 70 < spot[1] < 90:
                color = BLUE
            elif spot[0] < 20 and 90 < spot[1] < 110:
                color = BLACK
            elif 20 < spot[0] < 40 and 90 < spot[1] < 110:
                color = BROWM
            elif spot[0] < 40 and 110 < spot[1] < 150:
                color = WHITE

            if spot[0] > 60:
                pygame.draw.circle(screen, color, e.pos, radius)
            draw_on = True
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_w:
                radius += 20  # Increase the circle radius
            if e.key == pygame.K_s:
                radius -=20  # Decrease the circle radius

        if e.type == pygame.MOUSEBUTTONUP:
            draw_on = False
        
        if e.type == pygame.MOUSEMOTION:
            spot = pygame.mouse.get_pos()
            if draw_on and spot[0] > 60:
                pygame.draw.circle(screen, color, e.pos, radius)
                roundline(screen, color, e.pos, last_pos, radius)
            last_pos = e.pos

        if e.type == pygame.KEYDOWN:
            spot = pygame.mouse.get_pos()
            if spot:  # Checking that the mouse is within the window
                if e.key == pygame.K_r:  # Draw square when 'R' is pressed
                    rect_size = 100
                    draw_square(screen, color, spot, rect_size)
                elif e.key == pygame.K_t:  # Draw right triangle when 'T' is pressed
                    draw_right_triangle(screen, color, spot, 100, 100)
                elif e.key == pygame.K_e:  # Draw equilateral triangle when 'E' is pressed
                    draw_equilateral_triangle(screen, color, spot, 100)
                elif e.key == pygame.K_h:  # Draw rhombus when 'H' is pressed
                    draw_rhombus(screen, color, spot, 50)

        pygame.display.flip()

except StopIteration:
    pass

pygame.quit()
