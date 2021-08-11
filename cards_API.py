import requests
from constants import API_URL, PLAYER

deck_id = requests.get(f'{API_URL}new/shuffle/?deck_count=1').json()['deck_id']

class Deck():
    def __init__(self, deck_id):
        self.deck_id = deck_id
        self.drawn_cards = []

    def draw(self, pile):
        card = requests.get(f'{API_URL}{self.deck_id}/draw/?count=1').json()['cards']
        requests.get(f'{API_URL}{deck_id}/pile/{pile}/add/?cards={card[0]["code"]}')
        return card[0]['code']
        

    def shuffle(self):
        requests.get(f'{API_URL}{self.deck_id}/shuffle/')

    def show_pile(self, pile):
        return requests.get(f'{API_URL}{deck_id}/pile/{pile}/list/').json()

class Player():
    def __init__(self, name):
        self.name = name
        self.cards = requests.get(f'{API_URL}{deck_id}/pile/player_cards/add/?cards=AS,2S')
    def add_cards(cards):
        pass



