import pygame
from constants import *

pygame.init()

pygame.display.set_caption('Blackjack')

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    pygame.draw.rect(screen, 'green', pygame.Rect(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.flip()
            