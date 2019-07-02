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

**Space Complexity**: O(n) to maintain set of visited directories and for recursion depth

## Problem 3: Huffman Coding

#### __Design__ 

The primary idea behind huffman coding is to assign codes with fewer digits to more
frequently occuring characters in a string. So, we begin by build a frequency map
of characters and their counts in the original string. 

We then make a HuffmanNode with each of these characters and their frequencies,  and push these into a min heap.

At every step, we pull two nodes with the least frequencies and merge them under a pseudo node, 
referred to as internal node which has no data but a frequency that's the combined frequencies of
the two nodes being merged. We make a HuffmanTree with this pseudo-node at the root, and the
two original nodes as its children. We push this tree into the heap, and continue pulling
mins from the heap until only one element is left which should be a tree (if its a HuffmanNode, 
-ie there is only one character in our string, we will create a dummy parent with this HuffmanNode as the only child).

Now we walk through every element in this HuffmanTree, adding a 0 every time we visit left and 1 every time we visit right, 
and we assign the accumulated code to the leaf node we encounter in that path.

Finally, we encode the original string using the code stored to the HuffmanNodes in the leaf of our tree.

To decode this string, we again walk through the tree, taking a left for 0 and right for 1, until we encounter
a leaf node. At this point, we replace the code so far with the leaf node character, reset back to root of the tree
and continue walking till we have decoded all the characters.

The time complexity is proportional to size of string that is being encoded/decoded, since we 
walk through every character.

The space complexity will be proportional to n^2 since there are n leaf nodes in our tree, which means
the geometric series with a = n, r = 1/2 and log(n) terms will sum to n^2.

#### __huffman_encoding__  

**Time Complexity**: O(n) where n is number of characters in the original string

**Space Complexity**: O(n^2)

#### __huffman_decoding__  

**Time Complexity**: O(k) where n is number of digits in encoded binary data

**Space Complexity**: O(n^2)

## Problem 4: Active Directory

#### __Design__ 

For every group, we check each user for match with the requested user, and we 
recursively do this for every sub-group. Since we could visit every user/group a maximum
of only once, while checking for match, time complexity is O(n). The space complexity is O(n)

#### __is_user_in_group__  

**Time Complexity**: O(n) where n is number of users + sub-groups in a group

**Space Complexity**: O(n)

## Problem 5: Block Chain

#### __Design__ 

Block-chain is formed by appending a new block to a list, that has as one of its
members a hash of the previous last block in the list, to build a chain of integrity.

The hash itself is formed by taking into account the previous hash along with current
block data and timestamp.

The time and space complexity are both proportional to the number of blocks being added.

The complexity of hash function is not considered here, which could depend on length of the data.

#### __append__  

**Time Complexity**: O(n) where n is number of blocks

**Space Complexity**: O(n)


## Problem 5: Union and Intersection

#### __Design__ 

Since, we need to allow for duplication of elements within a linked list, the best way to 
track matching elements would be to sort the two individual linked list, and walk through them
side by side.

We use merge sort to sort the two linked list and this operation takes O((m+n)log(m+n)) time
where m, n are number of elements in the two linked lists respectively.

This is the dominant operation, since once we have them sorted, we will just walk through elements from
both lists in linear time, comparing for match and adding them to the output for both union and intersection if match occurs.
If mismatch occurs, we only add the elements for the union case.



#### __union__  

**Time Complexity**: O((m+n)log(m+n)) where m, n are number of elements in the two linked lists respectively

**Space Complexity**: O(m+n)

#### __intersection__  

**Time Complexity**: O((m+n)log(m+n)) where m, n are number of elements in the two linked lists respectively

**Space Complexity**: O(m+n)
