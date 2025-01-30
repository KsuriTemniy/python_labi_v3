from typing import List, Dict, Set

def intersect_even_odd(numbers: List[int]) -> Set[int]:
    even = set(n for n in numbers if n % 2 == 0)
    odd = set(n for n in numbers if n % 2 != 0)
    return even.intersection(odd)