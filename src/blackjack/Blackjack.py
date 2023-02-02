import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
from shoe.Shoe import Shoe
from strategies.BaseStrategy import BaseStrategy
from utils.card_utils import compute_available_counts


class BlackJack:
    def __init__(
        self,
        shoe: Shoe,
        dealer_strategy: BaseStrategy,
        player_strategy: BaseStrategy,
        shoe_breakpoint=0.75,
        log=False,
    ):
        self.shoe = shoe
        self.dealer_strategy = dealer_strategy
        self.player_strategy = player_strategy
        assert shoe_breakpoint <= 1 and shoe_breakpoint > 0
        self.shoe_limit_card = shoe.num_cards_left() * (1 - shoe_breakpoint)
        self.log = log

    def execute_round(self):
        if self.log:
            print("[New Round]")
        if self.shoe.num_cards_left() <= self.shoe_limit_card:
            return None
        curr_round_data = {"player_hit": [], "dealer_hit": [], "player_win": None}
        # deal
        curr_round_data["dealer_cards"] = self.shoe.get_next_card(n=2)
        curr_round_data["player_cards"] = self.shoe.get_next_card(n=2)

        # check if dealer has 21
        if any([c.value == 14 for c in curr_round_data["dealer_cards"]]) and any(
            [c.value in [10, 11, 12, 13] for c in curr_round_data["dealer_cards"]]
        ):
            if self.log:
                print("Dealer Blackjack")
                print(" ".join([c.__str__() for c in curr_round_data["dealer_cards"]]))
            curr_round_data["player_win"] = False
            return curr_round_data

        # deal cards
        for agent, cards in [
            (self.dealer_strategy, curr_round_data["dealer_cards"]),
            (self.player_strategy, curr_round_data["player_cards"]),
        ]:
            agent.new_hand()
            for card in cards:
                agent.receive_card(card)
                agent.view_card(card)

        # show player dealer faceup card
        self.player_strategy.view_card(curr_round_data["dealer_cards"][0])

        if self.log:
            print("Dealer Face Up Card", curr_round_data["dealer_cards"][0].__str__())
            print(
                "Player Cards",
                " ".join([c.__str__() for c in curr_round_data["player_cards"]]),
            )

        # ask player to hit or not
        curr_round_data["player_hit"].append(self.player_strategy.hit_or_pass())
        while curr_round_data["player_hit"][-1]["hit"]:
            curr_round_data["player_cards"].append(self.shoe.get_next_card(n=1)[0])
            self.player_strategy.receive_card(curr_round_data["player_cards"][-1])
            self.player_strategy.view_card(curr_round_data["player_cards"][-1])
            if self.log:
                print(
                    "Player Hit:",
                    " ".join([c.__str__() for c in curr_round_data["player_cards"]]),
                )

            # check if bust
            player_available_counts = compute_available_counts(
                self.player_strategy.hand_num_aces,
                self.player_strategy.hand_count_other,
            )
            if min(player_available_counts) > 21:
                if self.log:
                    print("Player Bust")
                curr_round_data["player_win"] = False
                return curr_round_data
            elif min(player_available_counts) == 21:
                break
            else:
                curr_round_data["player_hit"].append(self.player_strategy.hit_or_pass())

        # if player does not bust, dealer's turn to hit
        curr_round_data["dealer_hit"].append(self.dealer_strategy.hit_or_pass())
        while curr_round_data["dealer_hit"][-1]["hit"]:
            curr_round_data["dealer_cards"].append(self.shoe.get_next_card(n=1)[0])
            self.dealer_strategy.receive_card(curr_round_data["dealer_cards"][-1])
            self.dealer_strategy.view_card(curr_round_data["dealer_cards"][-1])
            if self.log:
                print(
                    "Dealer Hit:",
                    " ".join([c.__str__() for c in curr_round_data["dealer_cards"]]),
                )

            # check if bust
            dealer_available_counts = compute_available_counts(
                self.dealer_strategy.hand_num_aces,
                self.dealer_strategy.hand_count_other,
            )
            if min(dealer_available_counts) > 21:
                if self.log:
                    print("Dealer Bust")
                curr_round_data["player_win"] = True
                return curr_round_data
            else:
                curr_round_data["dealer_hit"].append(self.dealer_strategy.hit_or_pass())

        # see who wins
        player_best = max(
            [
                cnt if cnt <= 21 else -1
                for cnt in compute_available_counts(
                    self.player_strategy.hand_num_aces,
                    self.player_strategy.hand_count_other,
                )
            ]
        )
        dealer_best = max(
            [
                cnt if cnt <= 21 else -1
                for cnt in compute_available_counts(
                    self.dealer_strategy.hand_num_aces,
                    self.dealer_strategy.hand_count_other,
                )
            ]
        )
        curr_round_data["player_win"] = (
            None if player_best == dealer_best else player_best > dealer_best
        )
        if self.log:
            print(
                f'Player {"Tie" if curr_round_data["player_win"] is None else "Win" if curr_round_data["player_win"] else "Lose"}'
            )
        return curr_round_data
