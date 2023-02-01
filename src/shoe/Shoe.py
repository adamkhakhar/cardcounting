import os
import sys
from typing import List
import random

sys.path.append(os.dirname(os.path.realpath(__file__)))

from Card import Card


class Shoe:
    def __init__(self, num_decks: int):
        self.num_decks = num_decks
        self._cards = []
        for _ in range(num_decks):
            self._cards += self.generate_deck()
        self._curr_index = 0
        self.reset()

    def generate_deck(self) -> List[Card]:
        curr_cards = []
        for suit in range(4):
            for value in range(2, 15):
                curr_cards.append(Card(suit, value))
        return curr_cards

    def reset(self):
        random.shuffle(self._cards)
        self._curr_index = 0

    def get_next_card(self, n=1) -> List[Card]:
        if self._curr_index + n >= len(self._cards):
            raise Exception("Out of cards in deck when asking for next card")
        else:
            curr_cards = []
            for _ in range(n):
                curr_cards.append(self._cards[self._curr_index])
                self._curr_index += 1
            return curr_cards
