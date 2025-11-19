from node import Node


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_to_head(self, node: Node):
        if self.head is None:
            self.tail = node
        node.set_next(self.head)
        self.head = node

    def add_to_tail(self, node: Node):
        if self.head is not None:
            self.tail.set_next(node)
            self.tail = node
        else:
            self.head = node
            self.tail = self.head

    def remove_from_head(self):
        if self.head is None:
            return None
        old_head = self.head
        self.head = self.head.next
        old_head.next = None
        if self.head is None:
            self.tail = None
        return old_head

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next
        yield node

if __name__ == "__main__":
    l = LinkedList()
    l.add_to_tail(Node("hello"))
    print(l.head, l.tail)
    l.add_to_tail(Node("world"))
    print(l.head, l.tail)
    l.add_to_tail(Node("!"))
    print(l.head, l.tail)
    print("second item: ", l.head.next)

    for node in l:
        print(node, end="->")
    print("\n")
    for _ in range(3):
        l.remove_from_head()
        for node in l:
            print(node, end="->")
        print("\n")
    
