def find_minimum(nums):
    minimum = float("inf")
    if not nums: return None
    for num in nums:
        if num < minimum:
            minimum = num
    return minimum
