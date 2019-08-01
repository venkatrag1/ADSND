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
