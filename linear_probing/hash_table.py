class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def hash_function(self, key):
        # A vary simple hash function (modulo)
        return hash(key) % self.size

    def insert(self, key, value):
        index = self.hash_function(key)

        # Linear probing for collision resolution
        while self.table[index] is not None:
            index = (index + 1) % self.size

        self.table[index] = (key, value)

    def get(self, key):
        index = self.hash_function(key)

        original_index = index  # Keep track of where we started (prevent infinite loop)
        while self.table[index] is not None:
            if self.table[index][0] == key:
                return self.table[index][1]
            index = (index + 1) % self.size

            if index == original_index:  # Means we've looped through the whole table
                return None

        return None

    def __str__(self):
        return str(self.table)
