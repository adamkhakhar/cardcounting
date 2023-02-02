import os
import sys
import code
import argparse

sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
from shoe.Shoe import Shoe
from strategies.Dealer import Dealer
from strategies.HiOpt1 import HiOpt1
from blackjack.Blackjack import BlackJack

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--log", help="log all execution", action="store_true")
    parser.add_argument(
        "-shoe_breakpoint", help="fraction of shoe dealt", default=0.75, type=float
    )
    parser.add_argument(
        "-num_decks", help="number of decks in shoe", default=6, type=int
    )

    args = parser.parse_args()

    shoe = Shoe(args.num_decks)
    dealer = Dealer()
    player = HiOpt1(True, args.num_decks)
    game = BlackJack(shoe, dealer, player, log=args.log)
    game.execute_round()
