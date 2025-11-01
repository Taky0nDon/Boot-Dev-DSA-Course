# Merge sort is stable--it will preserve the order of duplicate items in the original list
from sys import argv
from random import randint
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

class foo:
    def __init__(self, id, val):
        self.id = id
        self.val = val
    def __str__(self):
        return f"id: {self.id}, val: {self.val}"
    def __repr__(self):
        return self.__str__()
    def __le__(self, other):
        return self.val <= other.val
    def __lt__(self, other):
        return self.val < other.val

if __name__ == "__main__":
    unsorted_list = list(int(e) for e in argv[1:])
    print(merge_sort(unsorted_list))
