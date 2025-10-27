import math

def get_influencer_score(num_followers: int, average_engagement_percentage:float) -> float:
    return average_engagement_percentage * math.log(num_followers, 2)

if __name__ == "__main__":
    tests = [
            [40000, 0.3]
            ]

    for t in tests:
        print(round(get_influencer_score(*t)))
