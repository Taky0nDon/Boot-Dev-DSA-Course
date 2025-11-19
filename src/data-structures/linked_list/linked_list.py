class Node:
    def __init__(self, item):
        self.val = item
        self.next = None

    def set_next(self, node: Node):
        self.next = node

    def __repr__(self):
        return self.val
