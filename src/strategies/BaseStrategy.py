import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
from shoe.Card import Card


class BaseStrategy:
    def __init__(self, info=""):
        self.info = info

    def view_card(self, card: Card):
        pass

    def hit_or_pass(self) -> dict:
        pass

    def next_hand(self):
        pass
