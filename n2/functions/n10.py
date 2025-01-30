from typing import List, Dict, Set

def sum_odd_numbers(n: int) -> int:
    return sum(i for i in range(1, n + 1, 2))