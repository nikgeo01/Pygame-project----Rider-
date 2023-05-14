import pygame
import time
import math

from functions import resize_image
from functions import rotate_image

TRACK = pygame.image.load("assets/track.png")

TRACK_BORDER = pygame.image.load("assets/track-border.png")

RED_CAR = resize_image(pygame.image.load("assets/red-car.png"), 0.5)
GREEN_CAR = resize_image(pygame.image.load("assets/green-car.png"), 0.5)

WIDTH = TRACK.get_width()
HEIGHT = TRACK.get_height()
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Rider")


class Cars:

    def __init__(self, max_vel, rotation_vel):
        self.img = self.IMG
        self.max_vel = max_vel
        self.rotation_vel = rotation_vel
        self.vel = 0
        self.angle = -90

    def rotate(self, left=False, right=False):
        if left:
            self.angle += self.rotation_vel
        elif right:
            self.angle -= self.rotation_vel

    def draw(self, screen):
        rotate_image(screen, self.img, (200, 485), self.angle)

class PLayerRedCar(Cars):
    IMG = RED_CAR

clock = pygame.time.Clock()
images = [(TRACK, (0, 0)), ((TRACK_BORDER), (0, 0))]

def draw(screen, images, player_car):
    for img, pos in images:
        screen.blit(img, pos)

    player_car.draw(screen)
    pygame.display.update()


player_car = PLayerRedCar(4, 4)

while True:
    clock.tick(60)
    
    draw(SCREEN, images, player_car)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()