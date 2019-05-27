Notation
----
Let n be the number of records in texts.csv and m be the number of records in 
calls.csv


Task0
----

####First Record of Texts  

**Time Complexity**: O(1) 

**Space Complexity**: O(1)


####Last Record of Calls  

**Time Complexity**: O(1)

**Space Complexity**: O(1)


####Explanation
For both the cases, the space complexity is O(1) since the storage needed
does not increase with input size.  

For the first record, the time complexity is O(1) since we can directly index into
the first element in the list.  

For the last record, in a C-style implementation of an array, the size would be
stored ahead of time, so the time complexity would've been O(m).
However, in python, the size of the list is stored and can be retrieved in O(1)
time, and therefore, O(-1) directly indexes into a known index leading the time
complexity to be O(1) in this case as well.

Task1
----

####Number of Unique Phone numbers  
**Time Complexity**: O(m + n) 

**Space Complexity**: O(m + n)

####Explanation

The space complexity is equal to the number of records in text and calls csv
files combined, since in the worst case, each record could have two unique 
phone numbers, leading to (2m + 2n), which boils down to O(m + n), ignoring
leading constants

Similarly time complexity is also equal to total number of records, because we
have to go through each record exactly once to insert it into our set, before doing
a O(1) length lookup of the set itself.

Task0
----

####First Record of Texts  
**Time Complexity**: O(1) 

**Space Complexity**: O(1)

####Explanation
Task0
----

####First Record of Texts  
**Time Complexity**: O(1) 

**Space Complexity**: O(1)

####Explanation

Task0
----

####First Record of Texts  
**Time Complexity**: O(1) 

**Space Complexity**: O(1)

####Explanation




  