"""Design a HashMap without using any built-in hash table libraries.

Implement the MyHashMap class:

MyHashMap() initializes the object with an empty map.
void put(int key, int value) inserts a (key, value) pair into the HashMap. If the key already exists in the map, update the corresponding value.
int get(int key) returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key.
void remove(key) removes the key and its corresponding value if the map contains the mapping for the key.
 

Example 1:

Input
["MyHashMap", "put", "put", "get", "get", "put", "get", "remove", "get"]
[[], [1, 1], [2, 2], [1], [3], [2, 1], [2], [2], [2]]
Output
[null, null, null, 1, -1, null, 1, null, -1]

Explanation
MyHashMap myHashMap = new MyHashMap();
myHashMap.put(1, 1); // The map is now [[1,1]]
myHashMap.put(2, 2); // The map is now [[1,1], [2,2]]
myHashMap.get(1);    // return 1, The map is now [[1,1], [2,2]]
myHashMap.get(3);    // return -1 (i.e., not found), The map is now [[1,1], [2,2]]
myHashMap.put(2, 1); // The map is now [[1,1], [2,1]] (i.e., update the existing value)
myHashMap.get(2);    // return 1, The map is now [[1,1], [2,1]]
myHashMap.remove(2); // remove the mapping for 2, The map is now [[1,1]]
myHashMap.get(2);    // return -1 (i.e., not found), The map is now [[1,1]]
"""


class MyHashMap:

    def __init__(self):
        self.buckets_cnt = 10 ** 3
        self.buckets = [[None] for _ in range(self.buckets_cnt)]
    
    def hash_func(self, key):
        return hash(key) % self.buckets_cnt

    def put(self, key: int, value: int) -> None:
        key_hash = self.hash_func(key)
        for ix, val in enumerate(self.buckets[key_hash]):
            if val is not None and val[0] == key:
                self.buckets[key_hash][ix] = (key, value)
                return
        self.buckets[key_hash].append((key, value))
    
    def get(self, key: int) -> int:
        key_hash = self.hash_func(key)
        for val in self.buckets[key_hash]:
            if val is not None and val[0] == key:
                return val[1]
        return -1

    def remove(self, key: int) -> None:
        key_hash = self.hash_func(key)
        for ix, val in enumerate(self.buckets[key_hash]):
            if val is not None and val[0] == key:
                self.buckets[key_hash][ix] = None


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
