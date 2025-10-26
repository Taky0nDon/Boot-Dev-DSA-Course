# estimated spread = average_audience_follower * (num_followers ^ 1.2)
def get_estimated_followers(audience_followers: list[int]) -> int:
    num_followers = len(audience_followers)
    if num_followers == 0: return 0
    average_audience_followers = sum(audience_followers)/num_followers
    return average_audience_followers * (num_followers ** 1.2)
if __name__ == "__main__":
    tests = [
            [7, 4, 3, 100, 765, 2344, 1, 2, 32],
            [],
            [10, 200, 3000, 5000, 4],
            [12, 12, 12]
            ]
    for t in tests:
        print(f"test: {t}")
        print(get_estimated_followers(t))
