import pygame
from constants import *
from cards_API import *

pygame.init()

pygame.display.set_caption('Blackjack')
clock = pygame.time.Clock()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

while True:
    mouse = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if 0 <= mouse[0] <= 50 and 0 <= mouse[1] <= 50:
                pygame.quit()

    pygame.draw.rect(screen, 'green', pygame.Rect(0, 0, 50, 50))

# initiate the deck and players
    deck_id = requests.get(f'{API_URL}new/shuffle/?deck_count=1').json()['deck_id']
    deck = Deck(deck_id)
    player = Player('Palmer')
    dealer = Dealer()


    pygame.display.update()
    clock.tick(60)
            