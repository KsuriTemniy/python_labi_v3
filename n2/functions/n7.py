from typing import List, Dict, Set

def inverse_dict(n: int) -> Dict[int, float]:
    return {i: 1/i for i in range(1, n + 1)}