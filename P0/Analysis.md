Notation
----
Let m be the number of records in texts.csv and n be the number of records in 
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
stored ahead of time, so the time complexity would've been O(n).
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

Task2
----

####Number spending longest time on phone in Sept 2016
**Time Complexity**: O(n) 

**Space Complexity**: O(n)

####Explanation
Since we're going through every record in the calls csv file exactly once, the 
time complexity is O(n). We incur two O(1) lookups at every record, to see if the
phone number has previously been added to the dictionary, and if so, we append 
the duration to it, else we set it to 0. At the end, we do a second pass through
the numbers, going through the dictionary, to find the max. So, 2n + n boils down
to O(n).

Space complexity is equal to O(n) since in the worst case, every number can be 
unique in the calls csv in which case, our dictionary size would be twice the 
number of records in calls csv file (since each record contains an incoming and
answering number). 

Task3
----

####Area codes and mobile prefixes called by people in Bangalore
**Time Complexity**: O(n)

**Space Complexity**: O(n)

####Percentage of calls from Fixed lines in Bangalore to Fixed lines in Bangalore 
**Time Complexity**: O(n) 

**Space Complexity**: O(1)

####Explanation

Radix sort in O(n) time

Task4
----

####First Record of Texts  
**Time Complexity**: O(1) 

**Space Complexity**: O(1)

####Explanation




  