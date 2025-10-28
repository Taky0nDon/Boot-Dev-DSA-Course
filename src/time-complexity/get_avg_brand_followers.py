def get_avg_brand_followers(all_handles: list[list[str]], brand_name: str) -> float:
    #O(n*m) n = number of list, m = average length of lists
    brand_followers = 0
    for followers in all_handles:
        for follower in followers:
            if brand_name in follower:
                brand_followers += 1
    return brand_followers / len(all_handles)
