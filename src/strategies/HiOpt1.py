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

    def __init__(self, count_to_bet, hand_to_hit, num_decks: int):
        super().__init__(info="HiOpt1")
        self.num_decks = num_decks
        self.running_count = 0
        self.remaining_cards = 52 * num_decks
        self.count_to_bet = count_to_bet
        self.hand_to_hit = hand_to_hit
        self.dealer_card = -1

    def view_card(self, card: Card):
        self.running_count += HiOpt1.map_value_to_count[card.value]
        self.remaining_cards -= 1

    def peek_dealer_card(self, card: Card):
        self.view_card(card)
        self.dealer_card = card.value

    def hit_or_pass(self) -> dict:
        return {
            "current_count": {
                "hand_num_aces": self.hand_num_aces,
                "hand_count_other": self.hand_count_other,
            },
            "hit": self.hand_to_hit(
                self.hand_num_aces, self.hand_count_other, self.dealer_card
            ),
        }

    def place_bet(self) -> float:
        current_count = self.running_count / self.remaining_cards
        return self.count_to_bet(current_count)
