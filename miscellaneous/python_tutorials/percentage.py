"""
percentage.py

The user enters an integer n followed by names and marks for the n students. You are required to save the record in a dictionary data type. The user then enters the name of a student and you are required to print the average percentage marks obtained by that student, correct to two decimal places
"""

n = input()

i = 0
record_dict = {}
while i < n:
    record = raw_input()
    record = record.split()

    name = record[0]
    marks = record[1:]
    marks = map(float, marks)

    average = sum(marks) / 3
    record_dict[name] = average
    i += 1 #iterate

target = raw_input()
print "%.2f" % record_dict[target]
