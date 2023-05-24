import pygame
import time
import math

from functions import resize_image
from functions import rotate_image

TRACK = pygame.image.load("assets/track.png")
TRACK_BORDER = pygame.image.load("assets/track-border.png")
RED_CAR = resize_image(pygame.image.load("assets/red-car.png"), 0.5)
BLUE_CAR = resize_image(pygame.image.load("assets/blue-car.png"), 0.5)
WIDTH = TRACK.get_width()
HEIGHT = TRACK.get_height()
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Rider")
IMAGES = [(TRACK, (0, 0)), ((TRACK_BORDER), (0, 0))]


class Cars:

    def __init__(self, max_vel, rotation_vel):
        self.img = self.IMG
        self.x,self.y = self.POSITION
        self.max_vel = max_vel
        self.rotation_vel = rotation_vel
        self.vel = 0
        self.angle = 0
        self.acceleration = 0.03

    def rotate(self, left=False, right=False):
        if left:
            self.angle += self.rotation_vel
        elif right:
            self.angle -= self.rotation_vel

    def move(self):
        self.vel = min(self.vel + self.acceleration, self.max_vel)
        self.move_direction()
    
    def move_back(self):
        self.vel = max(self.vel - self.acceleration * 2, -self.max_vel/2.5)
        self.move_direction()
        
    def move_direction(self):
        self.x = self.x + self.vel * math.cos(math.radians(-self.angle))
        self.y = self.y + self.vel * math.sin(math.radians(-self.angle))


    def slow_down(self):
        self.vel = max(self.vel - self.acceleration / 2.1, 0)
        self.move_direction()


    def draw(self, screen):
        rotate_image(screen, self.img, (self.x, self.y), self.angle)


class PLayerRedCar(Cars):
    x = 200
    y = 525
    IMG = RED_CAR
    POSITION = (x, y)

class PlayerBlueCar(Cars):
    x = 200
    y = 485
    IMG = BLUE_CAR
    POSITION = (x, y)

clock = pygame.time.Clock()

def draw(screen, images, player1_car, player2_car):
    for img, pos in images:
        screen.blit(img, pos)

    player1_car.draw(screen)
    player2_car.draw(screen)
    pygame.display.update()

player1_car = PLayerRedCar(4, 4)
player2_car = PlayerBlueCar(4, 4)



while True:
    clock.tick(60)

    moving1 = False
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_LEFT]:
        player1_car.rotate(left=True)
    if pressed[pygame.K_RIGHT]:
        player1_car.rotate(right=True)
    if pressed[pygame.K_UP]:
        player1_car.move()
        moving1 = True
    if pressed[pygame.K_DOWN]:
        player1_car.move_back()
        moving1 = True

    if moving1 == False:
        player1_car.slow_down()


    moving2 = False
    if pressed[pygame.K_a]:
        player2_car.rotate(left=True)
    if pressed[pygame.K_d]:
        player2_car.rotate(right=True)
    if pressed[pygame.K_w]:
        player2_car.move()
        moving2 = True
    
    if moving2 == False:
        player2_car.slow_down()

    draw(SCREEN, IMAGES, player1_car, player2_car)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
