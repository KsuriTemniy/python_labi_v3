from typing import List, Dict, Set

def shortest_string_length(strings: List[str]) -> int:
    return min(len(s) for s in strings) if strings else 0