from random import randint
from red_black_trees import RedBlackTree

def test(values):
    for val in values:
        print(f"Inserting {val}")
        rbt.insert(val)
    print(rbt)


if __name__ == "__main__":
    rbt = RedBlackTree()
    test(_ for _ in range(1,8))
    num_of_values = randint(0,10)
    values = [ randint(0,100) for _ in range(num_of_values+1) ]
    rbt.insert(10)
    print(rbt)
