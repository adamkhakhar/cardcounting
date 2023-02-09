import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
sys.path.append(os.path.dirname(os.path.realpath(__file__)))
from shoe.Card import Card
from CountingStrategy import CountingStrategy


class HiOpt1(CountingStrategy):
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
        super().__init__(
            HiOpt1.map_value_to_count,
            count_to_bet,
            hand_to_hit,
            num_decks,
            info="HiOpt1",
        )
