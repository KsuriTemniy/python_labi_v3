from typing import List, Dict, Set

def remove_duplicates(items: List) -> List:
    return list(dict.fromkeys(items))