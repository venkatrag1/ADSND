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


## Problem 2: File Recursion

#### __Design__ 

In the straighforward case, we handle files and directories encountered in 
current directory differently - checking files for suffix match and adding to result if matched,
and recursing on the directories to continue the same until no more sub-directories are 
encountered.

However, softlinks might cause us to have infinite loops, breaking away from a true
tree structure if a sub-directory contains a softlink back to its parent.

To handle this case, we convert all directories, including softlinks to their 
realpath, and store them in a `visited` set recursing only if not already added into the set.

Since we visit every node exactly once, the time complexity is linear to number of nodes (files, 
directories, soft-links) under current directory.

#### __find_files__  

**Time Complexity**: O(n) where n is number of files and subdirectories under a given path

**Space Complexity**: O(n) to maintain set of visited directories
