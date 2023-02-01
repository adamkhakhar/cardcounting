import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
sys.path.append(os.path.dirname(os.path.realpath(__file__)))
from shoe.Card import Card
from BaseStrategy import BaseStrategy


class HiOpt1(BaseStrategy):
    map_value_to_count = {
        2: 0,
        7: 0,
        8: 0,
        9: 0,
        14: 0,
        3: 1,
        4: 1,
        5: 1,
        6: 1,
        10: -1,
        11: -1,
        12: -1,
        13: -1,
    }

    def __init__(self, default_hit_pass_behavior: bool, num_decks: int):
        super().__init__(info="HiOpt1")
        self.default_hit_pass_behavior = default_hit_pass_behavior
        self.num_decks = num_decks
        self.running_count = 0
        self.remaining_cards = 52 * num_decks

    def view_card(self, card: Card):
        self.running_count += HiOpt1.map_value_to_count[card.value]
        self.remaining_cards -= 1

    def hit_or_pass(self) -> dict:
        current_count = self.running_count / self.remaining_cards
        return {"current_count": current_count, "hit": self.default_hit_pass_behavior}
