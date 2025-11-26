def exponential_growth(initial_followers: int,
                       growth_factor: int,
                       days: int) -> list[int]:
    result = [initial_followers]
    for day in range(days):
        result.append(result[-1] * growth_factor)
    return result

if __name__ == "__main__":
    print(exponential_growth(10, 2, 4))
