def num_possible_orders(num_posts: int) -> int:
    """ Return number of possible orders in which a backlog consisting of num_posts
    posts could be published."""
    p = 1
    for n in range(1, num_posts+1):
        p *= n
    return p

if __name__ == "__main__":
    tests = [
            [2],
            [5],
            ]
    for t in tests:
        print(num_possible_orders(*t))
