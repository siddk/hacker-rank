"""
mobile_number.py

Given an integer N, and N phone numbers, print YES or NO to tell if it is a valid number or not.

A valid number starts with either 7, 8, or 9, and is 10 digits long.
"""

n = input()

for i in range(n):
    number = raw_input()
    if number.isdigit():
        number = int(number)
        if (len(str(number)) == 10) and (int(str(number)[0]) in [7,8,9]):
            print "YES"
        else:
            print "NO"
    else:
        print "NO"
