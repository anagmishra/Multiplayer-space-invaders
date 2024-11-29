import pygame
import os

pygame.font.init()

WIDTH = 900
HEIGHT = 500

WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("LET THE GAMES BEGIN")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

BORDER = pygame.Rect(445, 0, 10, HEIGHT)

HEALTH_FONT = pygame.font.SysFont('bauhaus93', 40)
WINNER_FONT = pygame.font.SysFont('bauhaus93', 100)

SPACESHIP_WIDTH = 55
SPACESHIP_HEIGHT = 40

YELLOW_HIT = pygame.USEREVENT + 1
RED_HIT = pygame.USEREVENT + 2

YELLOW_SPACESHIP_IMG = pygame.image.load(os.path.join('Pictures','yellow_spaceship.png'))
YELLOW_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(YELLOW_SPACESHIP_IMG, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 90)

RED_SPACESHIP_IMG = pygame.image.load(os.path.join('Pictures', 'red_spaceship.png'))
RED_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(RED_SPACESHIP_IMG, (SPACESHIP_WIDTH,SPACESHIP_HEIGHT)), 270)

SPACE = pygame.transform.scale(pygame.image.load(os.path.join('Pictures', 'space.png')), (WIDTH, HEIGHT))