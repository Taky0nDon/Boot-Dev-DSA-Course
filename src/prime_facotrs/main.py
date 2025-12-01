import math


def prime_factors(n: int) -> list[int]:
    result = []
    while n % 2 == 0:
        n //= 2
        result.append(2)

    i = 3
    while i <= math.sqrt(n):
        print(n, i, n%i)
        print(result)
        while n % i == 0:
            result.append(i)
            n //= i
        i += 2

    if n > 2:
        result.append(int(n))

    return sorted(result)
print(prime_factors(100))
print(prime_factors(14))
print(prime_factors(7*13*23*31*1075*1075268818387))
