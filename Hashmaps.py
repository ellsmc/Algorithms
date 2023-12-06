class HashTable:
    def __init__(self, size) -> None:
        self.size = size
        self.hash_table = self.create_buckets()

    def create_buckets(self):
        return [[] for _ in range(self.size)]
    
    def set_value(self, key, value):
        """
        Inserts or updates value
        """
        # get index from key using hash func
        hashed_key = hash(key) % self.size
        # get bucket at index
        bucket = self.hash_table[hashed_key]
        found_key = False
        for index, record in enumerate(bucket):
            record_key, record_value = record
            # check for overlapping keys
            if record_key== key:
                found_key = True
                break

        # If key overlap update the key value
        if found_key:
            bucket[index] = (key, value)
        # else append the new key-value pair to the bucket
        else:
            bucket.append((key, value))

    def get_value(self, key):
        hashed_key = hash(key) % self.size
        bucket = self.hash_table[hashed_key]
        found_key = False
        for index, record in enumerate(bucket):
            record_key, record_value = record
            if record_key == key:
                found_key = True
                break
        if found_key:
            return record_value
        else:
            return "No record found"
    
    def delete_value(self, key):
        hashed_key = hash(key) % self.size
        bucket = self.hash_table[hashed_key]
        found_key = False
        for index, record in enumerate(bucket):
            record_key, record_value = record
            if record_key == key:
                found_key = True
                break
        if found_key:
            bucket.pop(index)
        return
    
    # Print items of hash map
    def __str__(self):
        return "".join(str(item) for item in self.hash_table)
    
hash_table = HashTable(50)

# insert some values
hash_table.set_value('gfg@example.com', 'some value')
print(hash_table)
print()
 
hash_table.set_value('portal@example.com', 'some other value')
print(hash_table)
print()
 
# search/access a record with key
print(hash_table.get_value('portal@example.com'))
print()
 
# delete or remove a value
hash_table.delete_value('portal@example.com')
print(hash_table)