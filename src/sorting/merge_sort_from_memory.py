from sys import argv
from operator import ge, le
def merge(left: list[int], right: list[int], descending: bool) -> list[int]:
    if descending:
        op = ge
    else:
        op = le
    i = 0
    j = 0
    merged = []
    while i < len(left) and j < len(right):
        print(f"{left[i]=}, {right[j]=}")
        print(op)
        if op(left[i], right[j]):
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
            
    while i < len(left):
        merged.append(left[i])
        i += 1
    
    while j < len(right):
        merged.append(right[j])
        j += 1
    
    return merged
    
def merge_sort(nums: list[int], descending: bool) -> list[int]:
    if len(nums) < 2:
        return nums

    middle = len(nums) // 2
    left = merge_sort(nums[0:middle], descending)
    right = merge_sort(nums[middle:], descending)
    print(f"{left=}")
    print(f"{right=}")

    return merge(left, right, descending)

if __name__ == "__main__":
    if "-D" in argv:
        descending = True
        list_start = argv.index("-D") + 1
    else:
        list_start = 1
        descending = False
    to_sort = [int(a) for a in argv[list_start:]]
    print(f"{to_sort}")
    sorted_maybe = merge_sort(to_sort, descending)
    print(sorted_maybe)
