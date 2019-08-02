## Problem 1: Square Root of Integer

#### __Design__ 

Since, the expected time complexity is O(log(n)), we know that 
we need to perform binary search. 

We know that the square root of a positive number has to lie between
0 and that number itself (incase of 0 and 1). 
The exit condition would be when we have found a number whose square matches with given number or when 
left and right have converged on a value, in which case we need to 
return the lowest number that worked before we exited. 

For this, we remember the last middle that we shot past whenever we decide to search 
to the right.


#### __sqrt__  

**Time Complexity**: O(log(n)) for a given number n

**Space Complexity**: O(1)


## Problem 2: Search in Rotated Sorted Array

#### __Design__ 

Since we're expected to find the start of rotation in O(log(n)) time, 
we know we need to use binary search.

We will modify the binary search exit criteria to handle duplicates (optional), but
the major change occurs in the criterion for deciding whether to search left or right.

Unlike binary search on a regular sorted, array we can't decide this based on comparing
middle element and target alone. 

There are two approaches to handling this- 
- Approach 1: We  can do two passes over the rotated array, finding the index of 
rotation first  using a regular binary search and then launching a second regular binary search on either the left or 
right side of rotation to find the target.
- Approach 2: We can instead do this in one pass, by first determining whether the 
rotation at each step is on the left or right side of the middle, and then seeing if
target is in range on the sorted side and searching there. If the target is not in range
of the sorted side, then we skip the sorted side and look on the other side which contains 
the rotation. This way, we still get O(log(n)) since we only keep one half of the input after
every step.

We will implement Approach 2 here. In the case of duplicates, we may be unable to determine
direction of rotation, so we might still have to search on both sides, but that case is not applicable
given our problem input bounds.


#### __search__  

**Time Complexity**: O(log(n)) where n is number of elements in the array

**Space Complexity**: O(1)

## Problem 3: Re-arrange Arrray

#### __Design__ 

Since the expected time complexity is O(n log(n)), we already have a hint that 
this involves some sorting routine.

Beyond that, since the two numbers can't differ by more than one digit, we need to 
distribute the digits almost equally between the two numbers.

To make each number as big as it can be, we need to have larger digits in higher order positions.

To make the sum as big as possible, the digits being added at each position need to be 
as big as possible.

Therefore we will begin by sorting the list in descending order and then push digits
alternately into the two numbers.

#### __rearrange__  

**Time Complexity**: O(n log (n)) where n is length of the list

**Space Complexity**: O(n) for the temp array in merge sort


## Problem 4: Dutch National Flag

#### __Design__ 

Since we are required to sort it in one-pass, we need to put every element we visit
in the current position immediately. 

We can use an approach similar to partition step of quick sort where we put all 
elements less than pivot on the left and all elements greater than pivot on the right
and elements equal to pivot in the middle.

Since we could have exactly one value that's less than pivot and one value that's 
greater than pivot if we choose the pivot as 1, we would have fully sorted our array
after one pass of comparisons.

We need two pointers to track the less than pivot bucket end and greater than pivot bucket start.

We step through every element using the current pointer, and whenever we find an element that
should on a bucket on the either side rather than the middle, we swap it out with the element at the 
growing end of the bucket and then grow the corresponding bucket by 1, and reassess the new value at current.




#### __sort_012__  

**Time Complexity**: O(n) where n is number of elements in list (One pass)

**Space Complexity**: O(1) since its inplace


## Problem 5: Trie Autocomplete

#### __Design__ 

For the implementation of a TrieNode, we use a dictionary to store TrieNodes of 
children, with the child character as the key. This way, we can string together 
words with common prefix, by branching off at the first character that is different.

We also use a boolean flag to indicate whether a word that was inserted ends at 
the given TrieNode.

The Trie object then simply stores the root TrieNode, and traverses character by 
character down from the root until it cannot find a character in the hierarchy 
which means that this word wasn't inserted into the Trie.

For autocomplete, we just need to recurse down all possible paths from the last
node that matches the prefix, until we have found all word ends, and return the list. 



#### __insert(Trie level)__  

**Time Complexity**: O(n) where n is number of characters in the word being inserted

**Space Complexity**: O(n)


#### __find__  

**Time Complexity**: O(n) 

**Space Complexity**: O(n)



#### __suffixes__  

**Time Complexity**: O(m) where m is sum of characters in all the suffixes, since each character will be visited once as part of travesal.
**Space Complexity**: O(k) where k is the length of the longest suffix, since that is the deepest our recursion will grow to.


## Problem 6: Min Max Unsorted Array

#### __Design__ 

We can solve this simply in one linear pass, with two variables one for min and one for max.
We can then compare every integer with min and max, and update the min and max accordingly.

However, over here we are doing two comparisons for every integer.

When we have only two elements, we only need to compare them against each other once,
to get both the min and max.

Building on this idea, we will use a divide and conquer approach which will break
our comparisons into comparison against two or less elements, by recursively splitting
into left and right half until we are left with only one or two elements.

Of course, when we do get the min and max back from the two halves, we will have two comparisons
for min and max, but since this will happen fewer than n times, so
we are still better off than the 2n complexity of simple linear sweep. 

#### __get_min_max__  

**Time Complexity**: O(n) where n is the number of ints in the list

**Space Complexity**: O(1)



