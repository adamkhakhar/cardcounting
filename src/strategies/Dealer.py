import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
sys.path.append(os.path.dirname(os.path.realpath(__file__)))
from shoe.Card import Card
from BaseStrategy import BaseStrategy
from utils.card_utils import compute_available_counts


class Dealer(BaseStrategy):
    def __init__(self):
        super().__init__(info="Dealer")

    def hit_or_pass(self) -> dict:
        available_counts = compute_available_counts(
            self.hand_num_aces, self.hand_count_other
        )
        best_count = max([cnt if cnt <= 21 else -1 for cnt in available_counts])
        return {"current_count": best_count, "hit": best_count < 17 and best_count > 0}
