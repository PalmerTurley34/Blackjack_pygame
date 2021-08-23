# imports
import pygame
from constants import *
from cards_API import *
from buttons import *
from game_font import *

# initialize pygame
pygame.init()
pygame.display.set_caption('Blackjack')
clock = pygame.time.Clock()

# set up the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.draw.rect(screen, 'white', pygame.Rect(0, 400, 500, 500))

# initialize the buttons
button = pygame.image.load(button_file)
button_img = pygame.transform.scale(button, (BUTTON_WIDTH, BUTTON_HEIGHT))
screen.blit(button_img, (hit_me[0], hit_me[1]))
screen.blit(button_img, (stay[0], stay[1]))
screen.blit(button_img, (new_deal[0], new_deal[1]))
screen.blit(button_img, (bid_25[0], bid_25[1]))
screen.blit(button_img, (bid_50[0], bid_50[1]))
screen.blit(button_img, (bid_100[0], bid_100[1]))

# put text on the buttons
screen.blit(hit_me_text, (hit_me[0]+15, hit_me[1]+15))
screen.blit(stay_text, (stay[0]+23, stay[1]+15))
screen.blit(new_deal_text, (new_deal[0]+8, new_deal[1]+15))
screen.blit(bid_25_text, (bid_25[0]+13, bid_25[1]+15))
screen.blit(bid_50_text, (bid_50[0]+13, bid_50[1]+15))
screen.blit(bid_100_text, (bid_100[0]+8, bid_100[1]+15))

# load the image for the back of the cards
card_back = pygame.image.load('card back red.png')
card_back_img = pygame.transform.scale(card_back, (CARD_WIDTH, CARD_HEIGHT))

# initialize the deck and players
deck_id = requests.get(f'{API_URL}new/shuffle/?deck_count=1').json()['deck_id']
deck = Deck(deck_id)
player = Player('Palmer')
dealer = Player('Dealer')

# functions to use in the game loop
# puts the amount of money you have on the screen
def blit_chips():
    num_money = game_font.render(f'${player.money}', 1, 'green')
    screen.blit(num_money, (350, 300))
# puts your current bid on the screen
def blit_bid():
    bid = game_font.render(f'${player.bid}', 1, 'white')
    screen.blit(player_bid, (300, 150))
    screen.blit(bid, (350, 175))
# function for putting the game instructions on the screen
def blit_instructions(instruction):
    pygame.draw.rect(screen, 'black', pygame.Rect(0, 0, 500, 100))
    text_rect = instruction.get_rect(center=(SCREEN_WIDTH/2, 50))
    screen.blit(instruction, text_rect)

# reset the screen
def reset_screen():
    pygame.draw.rect(screen, 'black', pygame.Rect(0, 0, 500, 400))
    screen.blit(dealer_hand, (0, 150))
    screen.blit(player_hand, (0, 275))
    screen.blit(player_money, (300, 275))
    blit_chips()
# shuffles and deals the cards
def deal_cards():
    deck.shuffle()
    deck.draw(dealer)
    screen.blit(card_back_img, (0, 175))
    deck.draw(player)
    screen.blit(player.card_images[0], (0, 300))
    deck.draw(dealer)
    screen.blit(dealer.card_images[1], (60, 175))
    deck.draw(player)
    screen.blit(player.card_images[1], (60, 300))

blit_instructions(game_start)

while True:
    # keeps track of where the mouse is positioned
    mouse = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
# NEW DEAL
            if new_deal[0] <= mouse[0] <= new_deal[0] + BUTTON_WIDTH and new_deal[1] <= mouse[1] <= new_deal[1] + BUTTON_HEIGHT and new_deal_active:
                # reset the game
                reset_screen()
                player.card_images = []
                dealer.card_images = []
                player.card_values = 0
                dealer.card_values = 0
                player.has_ace = False
                dealer.has_ace = False
                # change active buttons and instructions
                blit_instructions(place_bid)
                new_deal_active = False
                bid_25_active = True
                bid_50_active = True
                bid_100_active = True            
# HIT ME
            elif hit_me[0] <= mouse[0] <= hit_me[0] + BUTTON_WIDTH and hit_me[1] <= mouse[1] <= hit_me[1] + BUTTON_HEIGHT and hit_me_active:
                deck.draw(player)
                i = len(player.card_images) - 1
                screen.blit(player.card_images[i], (i*60, 300))
                if player.card_values > 21 and player.has_ace:
                    player.card_values -= 10
                    player.has_ace = False
                elif player.card_values > 21 and player.has_ace == False:
                    hit_me_active = False
                    stay_active = False
                    player.money -= player.bid
                    blit_instructions(bust)
                    new_deal_active = True             
# STAY
            elif stay[0] <= mouse[0] <= stay[0] + BUTTON_WIDTH and stay[1] <= mouse[1] <= stay[1] + BUTTON_HEIGHT and stay_active:
                hit_me_active = False
                stay_active = False
                screen.blit(dealer.card_images[0], (0, 175))
                while dealer.card_values < 17:
                    deck.draw(dealer)
                    i = len(dealer.card_images) - 1
                    screen.blit(dealer.card_images[i], (i*60, 175))
                    if dealer.card_values > 21 and dealer.has_ace:
                        dealer.has_ace = False
                        dealer.card_values -= 10
                if dealer.card_values >= player.card_values and dealer.card_values < 21:
                    blit_instructions(lose)
                    player.money -= player.bid
                else:
                    blit_instructions(win)
                    player.money += player.bid
                new_deal_active = True
# BID 25
            elif bid_25[0] <= mouse[0] <= bid_25[0] + BUTTON_WIDTH and bid_25[1] <= mouse[1] <= bid_25[1] + BUTTON_HEIGHT and bid_25_active:
                # set the bid and deal
                player.bid = 25
                blit_bid()
                deal_cards()
                # change active buttons and instuctions
                bid_25_active = False
                bid_50_active = False
                bid_100_active = False
                hit_me_active = True
                stay_active = True
                blit_instructions(stay_or_hit_me)
# BID 50
            elif bid_50[0] <= mouse[0] <= bid_50[0] + BUTTON_WIDTH and bid_50[1] <= mouse[1] <= bid_50[1] + BUTTON_HEIGHT and bid_50_active:
                # set the bid and deal
                player.bid = 50
                blit_bid()
                deal_cards()
                # change active buttons and instuctions
                bid_25_active = False
                bid_50_active = False
                bid_100_active = False
                hit_me_active = True
                stay_active = True
                blit_instructions(stay_or_hit_me)
# BID 100
            elif bid_100[0] <= mouse[0] <= bid_100[0] + BUTTON_WIDTH and bid_100[1] <= mouse[1] <= bid_100[1] + BUTTON_HEIGHT and bid_100_active:
                # set the bid and deal
                player.bid = 100
                blit_bid()
                deal_cards()
                # change active buttons and instuctions
                bid_25_active = False
                bid_50_active = False
                bid_100_active = False
                hit_me_active = True
                stay_active = True
                blit_instructions(stay_or_hit_me)



    pygame.display.update()
    clock.tick(60)
            