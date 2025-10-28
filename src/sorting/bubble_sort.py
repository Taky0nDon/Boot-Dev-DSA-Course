def bubble_sort(nums: list[int]) -> list[int]:
    swapping = True
    while swapping:
        swapping = False
        for i in range(1, len(nums)):
            if nums[i] < nums[i-1]:
                nums[i-1], nums[i] = nums[i], nums[i-1]
                swapping = True
    return nums


if __name__ == "__main__":
    tests = [
            [1, 8, 4, 3, 9, 10, 0]
            ]
    for t in tests:
        print(bubble_sort(t))
