from typing import List, Dict, Set

def sum_positive(numbers: List[int]) -> int:
    return sum(n for n in numbers if n > 0)