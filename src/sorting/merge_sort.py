# Merge sort is stable--it will preserve the order of duplicate items in the original list
def merge_sort(nums: list[int]) -> list[int]:
    if len(nums) < 2:
        return nums

    mid = len(nums)//2
    sorted_left_side = merge_sort(nums[0:mid])
    sorted_right_side = merge_sort(nums[mid:len(nums)])

    return merge(sorted_left_side, sorted_right_side)


def merge(list1: list[int], list2: list[int]) -> list[int]:
    res = []
    i = j = 0

    while i<len(list1) and j<len(list2):
        if list1[i] <= list2[j]:
            res.append(list1[i])
            i += 1
        else:
            res.append(list2[j])
            j += 1

    while i<len(list1): 
        res.append(list1[i])
        i+=1

    while j<len(list2):
        res.append(list2[j])
        j+=1

    return res

if __name__ == "__main__":
    tests = [
            [3, 2, 1],
            [5, 4, 3, 2, 1],
            [1, 8, 4, 3, 9, 10, 0],
            [14,11,12],
            [1,0]
            ]
    for t in tests:
        print(merge_sort(t))
