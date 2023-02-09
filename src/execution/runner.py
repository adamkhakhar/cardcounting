import os
import sys
import code
import argparse
import numpy as np

sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
from shoe.Shoe import Shoe
from strategies.HiOpt1 import HiOpt1

# from strategies.HiOpt2 import HiOpt2
from blackjack.Blackjack import BlackJack
from utils.default_strategies import map_hand_to_hit, count_to_bet

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--log", help="log all execution", action="store_true")
    parser.add_argument(
        "-shoe_breakpoint", help="fraction of shoe dealt", default=0.75, type=float
    )
    parser.add_argument(
        "-num_decks", help="number of decks in shoe", default=6, type=int
    )
    parser.add_argument(
        "-num_shoes", help="number of shoes to simulate", default=1, type=int
    )

    args = parser.parse_args()

    shoe = Shoe(args.num_decks)
    player = HiOpt1(count_to_bet, map_hand_to_hit, args.num_decks)
    game = BlackJack(shoe, player, log=args.log)
    save_data = []
    for _ in range(args.num_shoes):
        shoe.reset()
        player.new_shoe()
        round_data = game.play_entire_shoe()
        for round in round_data:
            if round["player_win"] is None:
                save_data.append(0)
            elif round["player_win"]:
                save_data.append(
                    round["bet"]
                    if not round["player_blackjack"]
                    else 1.5 * round["bet"]
                )
            else:
                save_data.append(-1 * round["bet"])
    print(save_data)
    print(np.mean(save_data))
    print(np.sum(save_data))
