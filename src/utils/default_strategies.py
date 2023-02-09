def map_hand_to_hit(
    player_num_aces: int, player_count_other: int, dealer_card: int
) -> bool:
    # player count adjust
    player_count_other += max(0, player_num_aces - 1)
    player_num_aces = min(1, player_num_aces)
    # dealer count adjust
    dealer_card = min(10, dealer_card) if dealer_card != 14 else 14

    assert player_num_aces in [0, 1]
    if player_num_aces == 0:
        # hard total
        # upper limit
        if player_count_other >= 17:
            return False
        elif player_count_other >= 13:
            if dealer_card <= 6:
                return False
            else:
                return True
        elif player_count_other == 12:
            if dealer_card in [4, 5, 6]:
                return False
            else:
                return True
        else:
            return True

    else:
        # soft total
        if player_count_other >= 8:
            return False
        elif player_count_other == 7:
            if dealer_card <= 8:
                return False
            else:
                return True
        else:
            return True


def count_to_bet(cnt: float) -> float:
    return 0.5 + cnt
