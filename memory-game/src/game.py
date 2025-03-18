import pygame
import random
import requests
import os
from io import BytesIO
from card import Card

class MemoryGame:
    def __init__(self, screen):
        self.screen = screen
        self.cards = []
        self.flipped_cards = []
        self.load_assets()
        self.create_cards()
        print("Assets loaded and cards created")  # 디버깅용 출력

    def load_assets(self):
        base_path = os.path.dirname(__file__)
        self.card_back = pygame.image.load(os.path.join(base_path, 'assets/card_back.png'))
        self.symbols = self.load_pokemon_images()

    def load_pokemon_images(self):
        response = requests.get('https://pokeapi.co/api/v2/pokemon?limit=8')
        data = response.json()
        symbols = []
        for pokemon in data['results']:
            pokemon_data = requests.get(pokemon['url']).json()
            image_url = pokemon_data['sprites']['front_default']
            image_response = requests.get(image_url)
            image = pygame.image.load(BytesIO(image_response.content))
            symbols.append(image)
        print("Pokemon images loaded")  # 디버깅용 출력
        return symbols

    def create_cards(self):
        positions = [(x, y) for x in range(0, 400, 100) for y in range(0, 400, 100)]
        random.shuffle(positions)
        symbols = self.symbols * 2
        random.shuffle(symbols)

        for position, symbol in zip(positions, symbols):
            card = Card(symbol, position, symbol, self.card_back)
            self.cards.append(card)
        print("Cards created")  # 디버깅용 출력

    def draw(self):
        for card in self.cards:
            card.draw(self.screen)
        print("Cards drawn")  # 디버깅용 출력

    def handle_click(self, position):
        print(f"Handling click at {position}")  # 디버깅용 출력
        for card in self.cards:
            if card.position[0] <= position[0] <= card.position[0] + 100 and card.position[1] <= position[1] <= card.position[1] + 100:
                if not card.is_flipped and not card.is_matched:
                    card.flip()
                    self.flipped_cards.append(card)
                    if len(self.flipped_cards) == 2:
                        self.check_match()
                    break

    def check_match(self):
        card1, card2 = self.flipped_cards
        if card1.symbol == card2.symbol:
            card1.is_matched = True
            card2.is_matched = True
        else:
            pygame.time.wait(1000)
            card1.flip()
            card2.flip()
        self.flipped_cards = []
        print("Match checked")  # 디버깅용 출력