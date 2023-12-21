# -*- coding: utf-8 -*-
__author__ = '刘志奇'
"""
贪吃蛇
"""

import pygame
import random

WIDTH, HEIGHT = 640, 480
FPS = 8
BLOCK_SIZE = 20

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()


class Snake:
    def __init__(self):
        self.body = [(WIDTH // 2, HEIGHT // 2)]
        self.direction = 'right'

    def move(self):
        x, y = self.body[0]
        if self.direction == 'up':
            y -= BLOCK_SIZE
        elif self.direction == 'down':
            y += BLOCK_SIZE
        elif self.direction == 'left':
            x -= BLOCK_SIZE
        elif self.direction == 'right':
            x += BLOCK_SIZE
        self.body.insert(0, (x, y))
        self.body.pop()

    def change_direction(self, new_direction):
        if new_direction == 'up' and self.direction != 'down':
            self.direction = new_direction
        elif new_direction == 'down' and self.direction != 'up':
            self.direction = new_direction
        elif new_direction == 'left' and self.direction != 'right':
            self.direction = new_direction
        elif new_direction == 'right' and self.direction != 'left':
            self.direction = new_direction

    def draw(self):
        for x, y in self.body:
            pygame.draw.rect(screen, WHITE, (x, y, BLOCK_SIZE, BLOCK_SIZE))


class Food:
    def __init__(self):
        self.position = self.generate_position()

    def generate_position(self):
        x = random.randint(0, (WIDTH - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE
        y = random.randint(0, (HEIGHT - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE
        return x, y

    def draw(self):
        x, y = self.position
        pygame.draw.rect(screen, RED, (x, y, BLOCK_SIZE, BLOCK_SIZE))


snake = Snake()
food = Food()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                snake.change_direction('up')
            elif event.key == pygame.K_DOWN:
                snake.change_direction('down')
            elif event.key == pygame.K_LEFT:
                snake.change_direction('left')
            elif event.key == pygame.K_RIGHT:
                snake.change_direction('right')

    snake.move()

    if snake.body[0] == food.position:
        snake.body.append((0, 0))
        food.position = food.generate_position()

    screen.fill(BLACK)
    snake.draw()
    food.draw()
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()