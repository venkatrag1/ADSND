import unittest

class CacheData(object):
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __str__(self):
        return "({}: {})".format(self.key, self.value)


class Node(object):
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DLLQueue(object):
    def __init__(self):
        self.num_elements = 0
        self.head = None
        self.tail = None

    def is_empty(self):
        return self.num_elements == 0

    def enqueue(self, data):
        node = Node(data)
        if self.is_empty():
            self.head = node
        else:
            # Enqueue at tail
            self.tail.next = node
            node.prev = self.tail
        # Enqueued node becomes new tail
        self.tail = node
        self.num_elements += 1
        return node

    def dequeue(self):
        if self.is_empty():
            return None
        # Dequeue node at head and update head to next element
        data = self.head.data
        self.head = self.head.next
        self.num_elements -= 1
        return data

    def re_enqueue(self, node):
        if not node.next:
            # already at tail/most-recent; nothing needs to be done
            return
        # Make prev of next, point to current prev
        node.next.prev = node.prev
        if node.prev:
            # Make next of prev, point to current next if prev exists
            node.prev.next = node.next
        else:
            # Element to be re-enqueued is at the head, so update head to next
            self.head = node.next
        # Put the removed node at the tail
        self.tail.next = node
        node.prev = self.tail
        node.next = None
        self.tail = node

    def update_head(self, new_data):
        # Throw away head by updating its data with the new data
        if self.is_empty():
            self.enqueue(new_data)
        else:
            self.head.data = new_data

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.data) + " -> "
            cur_head = cur_head.next
        return out_string

class LRU_Cache(object):

    def __init__(self, capacity):
        # Initialize class variables
        self.num_elements = 0
        self.capacity = capacity
        if capacity < 0:
            print("Cannot use negative capacity for LRU. Defaulting to empty cache")
            self.capacity = 0
        self.key_map = dict() # Stores the node pointer for a given key
        self.usage_queue = DLLQueue() # Emulates the timeline of modification - with most recent at tail and least recent at head

    def is_full(self):
        return self.num_elements == self.capacity

    def _get_node_for_key(self, key):
        node = self.key_map[key]
        if key != node.data.key: # Confirm that reverse lookup from node matches key_map lookup
            raise ValueError("key_map key {} and usage_queue key {} are out of sync".format(
               key, node.data.key))
        return node

    def _make_most_recent(self, node):
        # Move node to tail
        self.usage_queue.re_enqueue(node)

    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent.
        if key not in self.key_map:
            return -1
        node = self._get_node_for_key(key)
        # The act of getting, makes this node the most recent
        self._make_most_recent(node)
        return node.data.value

    def _update_node(self, node, value):
        node.data.value = value
        # Updating also makes the node, the most recent
        self._make_most_recent(node)

    def set(self, key, value):
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item.
        if key in self.key_map:
            # Already present, just update timestamp
            node = self._get_node_for_key(key)
            self._update_node(node, value)
        elif not self.is_full():
            # Not present, but have space in cache to add new node
            self.num_elements += 1
            data = CacheData(key, value)
            node = self.usage_queue.enqueue(data)
            self.key_map[key] = node
        else:
            # Not present and capacity full.
            if self.capacity == 0: # Capacity is zero so do nothing
                return
            # Update LRU node value at head and make it least recent by putting at tail
            node = self.usage_queue.head
            old_key = node.data.key
            data = CacheData(key, value)
            self.usage_queue.update_head(data)
            self._make_most_recent(self.usage_queue.head)
            del self.key_map[old_key] # Deleted old key from key_map and make the updated node, the value for the new key
            self.key_map[key] = node

    def __str__(self):
        return "Keymap: {}\nUsage Queue: {}".format(self.key_map, self.usage_queue)


class TestLRU(unittest.TestCase):
    def setUp(self):
        print("\n\n****{}****".format(self._testMethodName))

    def test_case1(self):
        our_cache = LRU_Cache(5)
        our_cache.set(1, 1);
        our_cache.set(2, 2);
        our_cache.set(3, 3);
        our_cache.set(4, 4);

        print(our_cache.get(1))  # returns 1
        print(our_cache.get(2))  # returns 2
        print(our_cache.get(9))  # returns -1 because 9 is not present in the cache

        our_cache.set(5, 5)
        our_cache.set(6, 6)

        print(our_cache.get(3))  # returns -1 because the cache reached it's capacity and 3 was the least recently used entry

    def test_case2_zero_capacity_cache(self):
        our_cache = LRU_Cache(0)
        our_cache.set(1, 1);
        our_cache.set(2, 2);
        our_cache.set(3, 3);
        our_cache.set(4, 4);

        print(our_cache.get(1))  # returns -1 since nothing got cached
        print(our_cache.get(2))  # returns -1 since nothing got cached
        print(our_cache.get(9))  # returns -1 because k9 is not present in the cache

    def test_case3_repeated_updates_to_a_key(self):
        our_cache = LRU_Cache(3)
        our_cache.set(1, 1);
        our_cache.set(2, 2);
        our_cache.set(3, 3);
        our_cache.set(2, 4);
        our_cache.set(2, 5);

        print(our_cache.get(2))  # returns 5 since k2 got updated
        print(our_cache.get(1))  # returns 1 since updates dint kick oldest node out

        our_cache.set(4, 16);
        print(our_cache.get(3))  # returns -1 because k3 was the least recently used

        our_cache.set(5, 25);
        print(our_cache.get(2)) # returns -1 since k2 gets kicked out
        print(our_cache.get(5)) # returns 25

if __name__ == '__main__':
    unittest.main()