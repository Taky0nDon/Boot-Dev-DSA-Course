# an = a1 * (r^(n-1))
# fitness followers: quadruples each month
# cosmetic: triples each month
# other: doubles each month
def get_follower_prediction(follower_count: int, influencer_type: str, num_months: int) -> int:
    influencer_types = {
            "fitness": 4,
            "cosmetic": 3,
            None: 2
            }
    factor = influencer_types[influencer_type]
#    match influencer_type:
#        case "fitness":
#            factor = 4
#        case "cosmetic":
#            factor = 3
#        case _:
#            factor = 2
    return round(follower_count*(factor**num_months), 8)

if __name__ == "__main__":
    tests = [
            [12, "cosmetic", 4],
            [10, "fitness", 1]
            ]
    for t in tests:
        print(t)
        print(get_follower_prediction(*t))
