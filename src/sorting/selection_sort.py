from random import randint
def selection_sort(nums: list[int]) -> list[int]:
    for i in range(len(nums)):
        smallest_idx = i
        for j in range(i+1, len(nums)):
            if nums[j] < nums[smallest_idx]:
                smallest_idx = j
        nums[i], nums[smallest_idx] = nums[smallest_idx], nums[i]
    return nums

if __name__ == "__main__":
    for test in range(4):
        t = [randint(0,10) for n in range(10)]
        print(f"testing {t}")
        print(f"{selection_sort(t)}")

