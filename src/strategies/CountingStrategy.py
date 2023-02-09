import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
sys.path.append(os.path.dirname(os.path.realpath(__file__)))
from shoe.Card import Card
from BaseStrategy import BaseStrategy


class CountingStrategy(BaseStrategy):
    def __init__(
        self,
        map_value_to_count,
        count_to_bet,
        hand_to_hit,
        num_decks: int,
        info="CountingStrategy",
    ):
        super().__init__(info=info)
        self.num_decks = num_decks
        self.running_count = 0
        self.ace_count = 0
        self.remaining_cards = 52 * num_decks
        self.count_to_bet = count_to_bet
        self.hand_to_hit = hand_to_hit
        self.dealer_card = -1
        self.map_value_to_count = map_value_to_count

    def view_card(self, card: Card):
        if card.value == 14:
            self.ace_count += 1
        self.running_count += self.map_value_to_count[card.value]
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

    def new_shoe(self):
        self.running_count = 0
        self.remaining_cards = 52 * self.num_decks
        self.dealer_card = -1
        self.ace_count = 0
