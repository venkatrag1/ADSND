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
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""
def get_unique_counts():
    """
    Description: This function returns number of unique telephone numbers
    in both text and call csv files together

    Arguments:
        None

    Returns:
        length of set of telephone numbers encountered in incoming and answering
        fields of both csv.
    """
    telephone_numbers = set()
    for text in texts:
        incoming_number, answering_number, time = text
        telephone_numbers.update([str(incoming_number), str(answering_number)])
    for call in calls:
        incoming_number, answering_number, time, during = call
        telephone_numbers.update([str(incoming_number), str(answering_number)])
    return len(telephone_numbers)

#print(len(texts), len(calls))
print("There are <{count}> different telephone numbers in the records.".format(
      count=get_unique_counts()))