def binary_search(target: int, arr: list[int]) -> bool:
    n = len(arr)
    low = 0
    high = n - 1
    while low <= high:
        median = (low + high) //2
        item = arr[median]
        if item == target:
            return True
        elif item < target:
            low = median + 1
        else:
            high = median - 1
    return False


