def find_max(nums: list[int]) -> int:
    # O(n)
    max = -float("inf")
    for n in nums:
        if n > max:
            max = n
    return max
