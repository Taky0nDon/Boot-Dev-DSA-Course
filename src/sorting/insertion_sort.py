from random import randint
# O(n^2) in the average case. When data is already "mostly sorted"
# and the data set is small. 
# Iterate over each index from left to right.
# Lookback algo. i=j=1.
# compare e[j] and e[j-1]. move on if in order. if not in order
# swap. repeat with j until in order or you reach j = 1 again.
#
def insertion_sort(data: list[int]) -> list[int]:
    for i in range(len(data)):
        j = i
        while data[j] < data[j - 1] and j > 0:
            data[j], data[j-1] = data[j-1], data[j]
            j -= 1
    return data

if __name__ == "__main__":
    for test in range(5):
        t = [randint(0,100) for _ in range(10)]
        print(f"Original: {t}")
        sorted = insertion_sort(t)
        print(f"sorted: {sorted}")
