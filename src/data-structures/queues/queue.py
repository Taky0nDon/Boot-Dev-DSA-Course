class Queue:
    def __init__(self):
        self.items = []

    def push(self, item):
        """enqueue"""
        self.items.insert(0,item)

    def pop(self):
        """dequeue"""
        return self.items.pop() if self.items else None

    def peek(self):
        return self.items[-1] if self.items else None

    def size(self):
        return len(self.items)

if __name__ == "__main__":
    q = Queue()
    print(q.peek())
    q.push(1)
    q.push(3)
    print(q.peek())
    print(q.pop())
    print(q.peek())
    print(q.pop())
    print(q.peek())
