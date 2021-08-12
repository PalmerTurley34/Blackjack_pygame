import requests
from constants import API_URL

deck_id = requests.get(f'{API_URL}new/shuffle/?deck_count=1').json()['deck_id']

class Deck():
    def __init__(self, deck_id):
        self.deck_id = deck_id
        self.drawn_cards = []

    def draw(self, character):
        card = requests.get(f'{API_URL}{self.deck_id}/draw/?count=1').json()['cards'][0]
        requests.get(f'{API_URL}{deck_id}/pile/{character.name}/add/?cards={card["code"]}')
        character.cards.append(card)
        
        

    def shuffle(self):
        requests.get(f'{API_URL}{self.deck_id}/shuffle/')

    def show_pile(self, character):
        return requests.get(f'{API_URL}{deck_id}/pile/{character.name}/list/').json()

class Player():
    def __init__(self, name):
        self.name = name
        self.cards = []

class Dealer():
    def __init__(self) -> None:
        self.name = 'dealer'
        self.cards = []
        



