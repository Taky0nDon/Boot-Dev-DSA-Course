# Reduce fibonacci finder from exponential to polynomial time
def exponential_fib(n: int) -> int:
    if n <= 1:
        return n
    return exponential_fib(n-1) + exponential_fib(n-2)

def polynomial_fib(n: int) -> int:
    if n < 0: raise ValueError("n must be at least 0")
    if n <= 1: return n
    result = 0
    a = 0
    b = 1
    for i in range(n-1):
        result = a + b
        a = b
        b = result
    return result

if __name__ == "__main__":
    for n in range(0,10):
        print(exponential_fib(n))
        print(polynomial_fib(n))

