# A power set consists of all possible combinations of a given set of
# elements
def power_set(input_set: list[list]) -> list[list]:
    if not input_set:
        return [[]]
    all_subsets = [[]]
    for e in input_set:
        new_subsets = []
        for subset in all_subsets:
            new = subset + [e]
            new_subsets.append(new)
        all_subsets.extend(new_subsets)
    return all_subsets

def recursive_power_set(input_set: list[list]) -> list[list]:
    if not input_set:
        return [[]]
    subsets = []
    first = input_set[0]
    remaining = input_set[1:]
    remaining_subsets = recursive_power_set(remaining)
    for subset in remaining_subsets:
        subsets.append([first] + subset)
        subsets.append(subset)
    return subsets

if __name__ == "__main__":
    t = []
    for _ in range(4):
        print(power_set(t))
        print(recursive_power_set(t))
        t.append(_)
