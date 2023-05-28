import pygame
import time
import math

from imagesHandling import resize_image, rotate_image

TRACK = pygame.image.load("assets/track.png")
TRACK_BORDER = pygame.image.load("assets/track-border.png")
FINISH_LINE = pygame.image.load("assets/finish-line.png")
FINISH_LINE_MASK = pygame.mask.from_surface(FINISH_LINE)
TRACK_BORDER_MASK = pygame.mask.from_surface(TRACK_BORDER)
IMAGES = [(TRACK, (0, 0)), (FINISH_LINE, (250, 464))]

CLOCK = pygame.time.Clock()

RED_CAR = resize_image(pygame.image.load("assets/red-car.png"), 0.5)
BLUE_CAR = resize_image(pygame.image.load("assets/blue-car.png"), 0.5)

WIDTH = TRACK.get_width()
HEIGHT = TRACK.get_height()
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Rider")

SCORING_TIMEOUT = 840
FONT_PATH = "assets/SHOWG.ttf"


class Cars:

    def __init__(self, max_vel, rotation_vel):
        self.img = self.IMG
        self.x, self.y = self.POSITION
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

    def collision(self, mask, x=0, y=0):
        car_mask = pygame.mask.from_surface(self.img)
        offset = (round(self.x - x), round(self.y - y))
        point_of_intersection = mask.overlap(car_mask, offset)
        return point_of_intersection

    def bounce_back(self):
        self.vel = -self.vel / 2
        self.move()


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


def draw(screen, images, player1_car, player2_car, player1_score, player2_score, font):
    for img, pos in images:
        screen.blit(img, pos)

    player1_car.draw(screen)
    player2_car.draw(screen)

    text_score_1 = font.render('RED CAR SCORE: ' + str(player1_score), True, (255, 255, 255))
    textRect_score_1 = text_score_1.get_rect()
    textRect_score_1.center = (678, 140)

    text_score_2 = font.render('BLUE CAR SCORE: ' + str(player2_score), True, (255, 255, 255))
    textRect_score_2 = text_score_2.get_rect()
    textRect_score_2.center = (678, 160)

    screen.blit(text_score_1, textRect_score_1)
    screen.blit(text_score_2, textRect_score_2)

    pygame.display.update()

def draw_winning(screen, player1_score, player2_score, winning_font):
    if player1_score == 3:
        text_winning_1 = winning_font.render('RED CAR WINS!', True, (255, 255, 255))
        textRect_winning_1 = text_winning_1.get_rect()
        textRect_winning_1.center = (WIDTH / 2, HEIGHT / 2)
        screen.blit(text_winning_1, textRect_winning_1)
        pygame.display.update()
        time.sleep(5)
        pygame.quit()
    if player2_score == 3:
        text_winning_2 = winning_font.render('BLUE CAR WINS!', True, (255, 255, 255))
        textRect_winning_2 = text_winning_2.get_rect()
        textRect_winning_2.center = (WIDTH / 2, HEIGHT / 2)
        screen.blit(text_winning_2, textRect_winning_2)
        pygame.display.update()
        time.sleep(5)
        pygame.quit()

player1_car = PLayerRedCar(4, 4)
player2_car = PlayerBlueCar(4, 4)

player1_score = 0
player2_score = 0

player1_scoring_timeout = 0
player2_scoring_timeout = 0

pygame.init()
font = pygame.font.Font(FONT_PATH, 15)
winning_font = pygame.font.Font(FONT_PATH, 50)

while True:

    CLOCK.tick(60)
    draw(SCREEN, IMAGES, player1_car, player2_car, player1_score, player2_score, font)

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
    if pressed[pygame.K_s]:
        player2_car.move_back()
        moving2 = True
    if moving2 == False:
        player2_car.slow_down()

    if player1_car.collision(TRACK_BORDER_MASK, 0, 0) != None:
        player1_car.bounce_back()
        print("Player 1 crashed")

    if player2_car.collision(TRACK_BORDER_MASK, 0, 0) != None:
        player2_car.bounce_back()
        print("Player 2 crashed")

    player1_scoring_timeout += 1
    if player1_car.collision(FINISH_LINE_MASK, 250, 464) != None:
        if player1_scoring_timeout >= SCORING_TIMEOUT:
            player1_score += 1
            print("Player 1 score: ", player1_score)
            player1_scoring_timeout = 0

    player2_scoring_timeout += 1
    if player2_car.collision(FINISH_LINE_MASK, 250, 464) != None:
        if player2_scoring_timeout >= SCORING_TIMEOUT:
            player2_score += 1
            print("Player 2 score: ", player2_score)
            player2_scoring_timeout = 0

    draw_winning(SCREEN, player1_score, player2_score, winning_font)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
