from math import log
def log_scale(data: list[int], base: int) -> list[float]:
    return [log(d, base) for d in data]
