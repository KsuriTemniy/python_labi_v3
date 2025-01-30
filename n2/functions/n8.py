from typing import List, Dict, Set

def most_a_string(strings: List[str]) -> str:
    return max(strings, key=lambda s: s.count('a')) if strings else ""