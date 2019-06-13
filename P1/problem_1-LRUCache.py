class CacheData(object):
    def __init__(self, key, value):
        self.key = key
        self.value = value


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
        if not self.tail:
            self.head = node
        else:
            self.tail.next = node
            node.prev = self.tail
        self.tail = node
        self.num_elements += 1
        # Modify enqueue to return reference to recently enqueued node. This is
        # thread-safe compared to looking up the tail element separately.
        return node

    def dequeue(self):
        if self.is_empty():
            return None
        data = self.head.data
        self.head = self.head.next
        self.num_elements -= 1
        return data

    def re_enqueue(self, node):
        if not node.next:
            # already at tail/most-recent; nothing needs to be done
            return
        node.next.prev = node.prev
        if node.prev:
            node.prev.next = node.next
        else:
            self.head = node.next
        self.tail.next = node
        node.prev = self.tail
        node.next = None
        self.tail = node

    def update_head(self, new_data):
        if self.is_empty():
            self.enqueue(new_data)
        else:
            self.head.data = new_data

class LRU_Cache(object):

    def __init__(self, capacity):
        # Initialize class variables
        self.num_elements = 0
        self.capacity = capacity
        self.key_map = dict()
        self.usage_queue = DLLQueue()

    def is_full(self):
        return self.num_elements == self.capacity

    def _get_node_for_key(self, key):
        node = self.key_map[key]
        if key != node.data.key:
            raise ValueError("key_map key {} and usage_queue key {} are out of sync".format(
               key, node.data.key))
        return node

    def _make_most_recent(self, node):
        self.usage_queue.re_enqueue(node)

    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent.
        if key not in self.key_map:
            return -1
        node = self._get_node_for_key(key)
        self._make_most_recent(node)
        return node.data.value

    def _update_node(self, node, value):
        node.data.value = value
        self._make_most_recent(node)

    def set(self, key, value):
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item.
        if key in self.key_map:
            node = self._get_node_for_key(key)
            self._update_value(node, value)
        elif not self.is_full():
            self.num_elements += 1
            data = CacheData(key, value)
            node = self.usage_queue.enqueue(data)
            self.key_map[key] = node
        else:
            # Update LRU node value and make it least recent
            # Atomic
            node = self.usage_queue.head
            old_key = node.data.key
            data = CacheData(key, value)
            self.usage_queue.update_head(data)
            self._make_most_recent(self.usage_queue.head)
            del self.key_map[old_key]
            self.key_map[key] = node
            # End atomic


our_cache = LRU_Cache(5)

our_cache.set(1, 1);
our_cache.set(2, 2);
our_cache.set(3, 3);
our_cache.set(4, 4);


print(our_cache.get(1))      # returns 1
print(our_cache.get(2))      # returns 2
print(our_cache.get(9))     # returns -1 because 9 is not present in the cache

our_cache.set(5, 5)
our_cache.set(6, 6)

print(our_cache.get(3))      # returns -1 because the cache reached it's capacity and 3 was the least recently used entry
