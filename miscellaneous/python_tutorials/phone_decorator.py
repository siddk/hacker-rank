"""
phone_decorator.py

Given a series of numbers with optional extensions, sort them in ascending order, print them in desired format.
"""

total = input()
count = 0
record_list = []

while (count < total):
    phone_number = raw_input()
    record_list.append(int(phone_number[-10:]))
    count += 1

record_list = sorted(record_list)
