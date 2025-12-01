import math


def prime_factors(n: int) -> list[int]:
    prime_factors = []
    while n % 2 == 0:
        n //= 2
        prime_factors.append(2)

    i = 3
    while i <= math.sqrt(n):
        while n % i == 0:
            n //= i
            prime_factors.append(i)
        i += 2

    if n > 2:
        prime_factors.append(n)

    return sorted(prime_factors)
