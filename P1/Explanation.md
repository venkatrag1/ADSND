## Problem 1: LRU Cache

#### __Design__ 

There are two aspects of an LRU cache that need to be designed for. 

In order, for it to be an efficient cache, look-ups must be fast (O(1)). This suggests
that we need a HashMap. 

For it to keep track of the least recently used element,
to evict when adding new elements, we need to preserve the time order of modification. 
This indicates that we need some kind of a queue to preserve ordering.

Since, the act of getting and setting both cause an element to be considered the most recently used, 
we need a way to take an existing element and re-enqueue it again in the queue.
Thus, implementing this queue, using a doubly linked-list makes sense since we can
perform the order modification in O(1) time as long as we have a reference to the element itself.

Therefore, it makes sense to link the two data-structures like so- we could use the Hashmap to 
preserve a reference to the node itself, and the node would contain the actual value for that key.

We would also need a reference back to HashMap from the queue, for deleting the entry
when an element gets evicted from the cache. Therefore, in the queue node, we will maintain
the key apart from value itself, so that we have a reverse lookup in O(1) time as well.

Rather than delete the node itself, during eviction we simply overwrite the data value
of the least recently used node, to avoid making new nodes.


The overall space complexity is O(n) since, the HashMap and the Doubly Linked List used
for queue will both be of size n, where n is the capacity of the cache.



#### __get__  

**Time Complexity**: O(1)

**Space Complexity**: O(n) where n is size of cache

#### __set__  

**Time Complexity**: O(1)

**Space Complexity**: O(n) where n is size of cache


