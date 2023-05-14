import pygame
import time
import math

TRACK = pygame.image.load("track.png")

TRACK_BORDER = pygame.image.load("track-border.jpg")

RED_CAR = pygame.image.load("red-car.png")
GREEN_CAR = pygame.image.load("green-car.png")

WIDTH = TRACK.get_width()
HEIGHT = TRACK.get_height()
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))