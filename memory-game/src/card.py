import pygame

class Card:
    def __init__(self, symbol, position, image, back_image):
        self.symbol = symbol
        self.position = position
        self.image = image
        self.back_image = back_image
        self.is_flipped = False
        self.is_matched = False

    def draw(self, screen):
        if self.is_flipped or self.is_matched:
            screen.blit(self.image, self.position)
        else:
            screen.blit(self.back_image, self.position)

    def flip(self):
        self.is_flipped = not self.is_flipped