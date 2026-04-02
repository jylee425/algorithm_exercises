class HashTable:
    def __init__(self, capacity=8):
        self.capacity = capacity
        self.table = [[] for _ in range(capacity)]
        self.size = 0

    def _hash(self, key):
        return len(str(key)) % self.capacity

    def put(self, key, value):
        hashed_key = self._hash(key)
        bucket = self.table[hashed_key]

        for i, (k, _) in enumerate(bucket):
            if k == key:  # update
                bucket[i] = (key, value)
                return

        bucket.append((key, value))  # new
        self.size += 1

    def get(self, key):
        hashed_key = self._hash(key)
        bucket = self.table[hashed_key]

        for k, v in bucket:
            if k == key:
                return v

        return None

    def remove(self, key):
        hashed_key = self._hash(key)
        bucket = self.table[hashed_key]

        for i, (k, _) in enumerate(bucket):
            if k == key:
                bucket.pop(i)
                self.size -= 1
                return True

        return False


ht = HashTable()
# 1
ht.put("apple", 3)
assert ht.get("apple") == 3

# 2
assert ht.get("banana") is None

# 3
ht.put("apple", 10)
assert ht.get("apple") == 10

# 4
assert ht.remove("apple") is True
assert ht.get("apple") is None

# 5 collision
ht.put("a", 1)
ht.put("b", 2)
ht.put("c", 3)
assert ht.get("a") == 1
assert ht.get("b") == 2
assert ht.get("c") == 3

# 6 collision + remove
assert ht.remove("b") is True
assert ht.get("a") == 1
assert ht.get("b") is None
assert ht.get("c") == 3
assert ht.size == 2
assert ht.remove("not-found") is False
assert ht.remove("b") is False

print("PASSED ALL TESTS")
