from user import User
class HashMap:
    def key_to_index(self, key: str) -> int:
        hash = sum(ord(c) for c in key)
        index = hash % len(self.hashmap)
        return index

    def insert(self, key: str, value: object) -> None:
        index = self.key_to_index(key)
        kv_pair = key, value
        self.hashmap[index] = kv_pair

    def get(self, key: str) -> object:
        index = self.key_to_index(key)
        kv_pair = self.hashmap[index]
        if kv_pair is None:
            raise Exception("sorry, key not found")
        return kv_pair[1]


    # don't touch below this line

    def __init__(self, size):
        self.hashmap = [None for i in range(size)]

    def __repr__(self):
        buckets = []
        for v in self.hashmap:
            if v != None:
                buckets.append(v)
        return str(buckets)

