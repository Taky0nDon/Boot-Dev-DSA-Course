def verify_tsp(paths: list[list[int]], dist: int, actual_path: list[int]) -> bool:
    indexes = range(1, len(actual_path))
    return sum(paths[actual_path[i]][actual_path[i - 1]] for i in indexes) < dist
