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
            # print("receiving card", str(card))
            # print("orig hand count other", self.hand_count_other)
            self.hand_count_other += min(10, card.value)
            # print("after hand count other", self.hand_count_other)

    def view_card(self, card: Card):
        pass

    def hit_or_pass(self) -> dict:
        pass

    def new_hand(self):
        self.hand_num_aces = 0
        self.hand_count_other = 0
