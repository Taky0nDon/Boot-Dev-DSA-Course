from sys import argv

def get_median(nums: list[int|float]) -> int|float|None:
    if len(nums) == 0: return None
    number_of_items = len(nums)
    nums.sort()
    if number_of_items & 1:
        median = nums[number_of_items//2]
    else:
        mid1 = number_of_items//2
        mid2 = mid1 - 1
        median = (nums[mid1] + nums[mid2]) / 2
    return median

if __name__ == "__main__":
    nums = [ float(i) for i in argv[1:] ]
    median = get_median(nums)
    print(sorted(argv[1:]))
    print(f"{median:g}")
