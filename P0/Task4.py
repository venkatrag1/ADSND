"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

telephone_numbers = set()
possible_telemarketers = set()

for text in texts:
    # Add numbers that receive or send texts to set
    incoming_number, answering_number, time = text
    telephone_numbers.update([str(incoming_number), str(answering_number)])

for call in calls:
    # Add only numbers that received calls to set
    incoming_number, answering_number, time, during = call
    telephone_numbers.add(str(answering_number))

for call in calls:
    # Second pass through calls - iterate through incoming numbers and mark
    # as telemarketer if not in our set
    incoming_number, answering_number, time, during = call
    if incoming_number not in telephone_numbers:
        possible_telemarketers.add(incoming_number)

print("These numbers could be telemarketers: ")
[print(number) for number in sorted(list(possible_telemarketers))]



