"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

telephone_numbers_time_map = dict()

for call in calls:
    incoming_number, answering_number, time, during = call
    date = time.split(' ')[0]
    month, year = date.split('-')[1], date.split('-')[2]
    if month != '09' and year != '2016':
        continue
    telephone_numbers_time_map[incoming_number] = telephone_numbers_time_map.get(incoming_number, 0) + int(during)
    telephone_numbers_time_map[answering_number] = telephone_numbers_time_map.get(answering_number, 0) + int(during)

telephone_number = None
total_time = -1
for number, call_duration in telephone_numbers_time_map.items():
    if call_duration > total_time:
        total_time = call_duration
        telephone_number = number

print("<{telephone_number}> spent the longest time, <{total_time}> seconds, on the phone during September 2016.".format(
    telephone_number=telephone_number,
    total_time=total_time
))


