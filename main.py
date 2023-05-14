import pygame
import sys
import random

pygame.init()
clock = pygame.time.Clock()

# Screen
screen_width = 1280
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Rider')

rider = pygame.image.load('assets/rider.png')

surface = pygame.Surface((50, 50))

obstacle_disk = pygame.image.load('assets/obstacle_disk.png')

bg_img = pygame.image.load('assets/bg.png')
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.flip()
    clock.tick(60)