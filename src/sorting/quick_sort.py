# Divide and conquer
# Order (n *log n) space. o(1) complexity
# can degenerate into O(n**2) if biggest or smallest element is
# chosen as pivot
# pivot number. arbitrary use last
# i = -1
# j = 0
# compare j and pivot. if j > pivot incremenet i
# if j < pivot 1. incremenet i, 2. swap i and j
# swap i + 1 with pivot
# pivot is now in final position. recursively repeat on each side of pivot
# reduce worst case chance by 1. shuffling input lift
# 2. find median of sample of data (n = 3) from partition
# unstable
def quick_sort(data: list[int], low: int, high: int) -> list[int]:
    if low < high:
        pivot_index = partition(data, low, high)
        print(f"{pivot_index=}")
        quick_sort(data, low, pivot_index - 1)
        quick_sort(data, pivot_index + 1, high)

def partition(data: list[int], low: int, high: int):
    pivot = data[high]
    print(f"{pivot=}")
    i = low
    for j in range(low, high):
        print(f"{i=} {j=}")
        if data[j] < pivot:
            data[i], data[j] = data[j], data[i]
            print(data)
            i += 1
    data[i], data[high] = data[high], data[i]
    return i

if __name__ == "__main__":
    t = [_ for _ in range(10,-1,-1)]
    print(t)
    print(quick_sort(t, 0, len(t) -1 ))
