from typing import List


def compute_available_counts(num_aces: int, count_other: int) -> List[int]:
    max_value = 11 * num_aces + max(0, num_aces - 1) + count_other
    min_value = 1 * num_aces + count_other
    return [min_value, max_value]
