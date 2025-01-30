from typing import List, Dict, Set

def get_primes(n: int) -> List[int]:
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    ans = []
    for p in range(2, int(n ** 0.5) + 1):
        if is_prime[p]:
            for i in range(p * p, n + 1, p):
                is_prime[i] = False

    for p in range(2, n + 1):
        if is_prime[p]:
            ans.append(p)
    return ans