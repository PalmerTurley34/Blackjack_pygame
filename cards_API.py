import pygame
import requests
import io
from constants import API_URL, CARD_WIDTH, CARD_HEIGHT


class Deck():
    def __init__(self, deck_id):
        self.deck_id = deck_id
        self.drawn_cards = []

    def draw(self, character):
        card = requests.get(f'{API_URL}{self.deck_id}/draw/?count=1').json()['cards'][0]
        requests.get(f'{API_URL}{self.deck_id}/pile/{character.name}/add/?cards={card["code"]}')
        r = requests.get(card['image']).content
        card_file = io.BytesIO(r)
        card_load = pygame.image.load(card_file)
        card_img = pygame.transform.scale(card_load, (CARD_WIDTH, CARD_HEIGHT))
        character.card_images.append(card_img)
        if card['value'] in {'KING', 'QUEEN', 'JACK', '0'}:
            character.card_values += 10
        elif card['value'] == 'ACE':
            character.has_ace = True
            if character.card_values <= 10:
                character.card_values += 11
            else:
                character.card_values += 1
        else:
            character.card_values += int(card['value'])

        
        

    def shuffle(self):
        requests.get(f'{API_URL}{self.deck_id}/shuffle/')

    def show_pile(self, character):
        return requests.get(f'{API_URL}{self.deck_id}/pile/{character.name}/list/').json()

class Player():
    def __init__(self, name):
        self.name = name
        self.card_images = []
        self.money = 500
        self.card_values = 0
        self.has_ace = False
        self.bid = 0
        



