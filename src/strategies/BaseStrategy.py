import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
from shoe.Card import Card


class BaseStrategy:
    def __init__(self, info=""):
        self.info = info
        self.hand_num_aces = 0
        self.hand_count_other = 0

    def receive_card(self, card: Card):
        if card.value == 14:
            self.hand_num_aces += 1
        else:
            self.hand_count_other += min(10, card.value)

    def peek_dealer_card(self, card: Card):
        pass

    def view_card(self, card: Card):
        pass

    def hit_or_pass(self) -> dict:
        pass

    def new_hand(self):
        self.hand_num_aces = 0
        self.hand_count_other = 0
        self.dealer_card = -1

    def new_shoe(self):
        self.new_hand()

    def place_bet(self) -> float:
        pass
