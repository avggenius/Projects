import pygame
import sys
import random
pygame.init()
WIDTH, HEIGHT = 400, 400
GRID_SIZE = 20
GRID_WIDTH = WIDTH // GRID_SIZE
GRID_HEIGHT = HEIGHT // GRID_SIZE
SNAKE_SPEED = 10
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")
snake = [(5, 5)]
snake_direction = RIGHT
apple = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))
clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and snake_direction != DOWN:
        snake_direction = UP
    elif keys[pygame.K_DOWN] and snake_direction != UP:
        snake_direction = DOWN
    elif keys[pygame.K_LEFT] and snake_direction != RIGHT:
        snake_direction = LEFT
    elif keys[pygame.K_RIGHT] and snake_direction != LEFT:
        snake_direction = RIGHT
    new_head = (snake[0][0] + snake_direction[0], snake[0][1] + snake_direction[1])
    snake.insert(0, new_head)
    if snake[0] == apple:
        apple = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))
    else:
        snake.pop()
    if (
        snake[0][0] < 0
        or snake[0][0] >= GRID_WIDTH
        or snake[0][1] < 0
        or snake[0][1] >= GRID_HEIGHT
    ):
        pygame.quit()
        sys.exit()
    if len(snake) > 1 and snake[0] in snake[1:]:
        pygame.quit()
        sys.exit()
    screen.fill(WHITE)
    for segment in snake:
        pygame.draw.rect(
            screen, GREEN, (segment[0] * GRID_SIZE, segment[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE)
        )
    pygame.draw.rect(
        screen, RED, (apple[0] * GRID_SIZE, apple[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE)
    )
    pygame.display.flip()
    clock.tick(SNAKE_SPEED)
