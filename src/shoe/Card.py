from termcolor import colored
from typing import List


class Card:
    map_face_value_to_name = {11: "Jack", 12: "Queen", 13: "King", 14: "Ace"}
    map_suit_to_name = {0: "\u2663", 1: "\u2665", 2: "\u2666", 3: "\u2660"}
    suits = set([0, 1, 2, 3])
    values = set([2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14])

    def __init__(self, suit: int, value: int):
        assert suit in Card.suits
        assert value in Card.values
        self._suit = suit
        self._value = value
        self._playable_value = [min(10, value)]
        # ace
        if self._value == 14:
            self._playable_value.append(1)

    @property
    def plauable_value(self) -> List[int]:
        return self._playable_value

    @property
    def suit(self) -> int:
        return self._suit

    @property
    def value(self) -> int:
        return self._value

    def __str__(self):
        color_of_text = "red" if self._suit in [1, 2] else "black"
        value_str = (
            str(self._value)
            if self._value <= 10
            else Card.map_face_value_to_name[self._value]
        )
        return colored(
            f"{value_str}{Card.map_suit_to_name[self._suit]}", color_of_text, "on_white"
        )
