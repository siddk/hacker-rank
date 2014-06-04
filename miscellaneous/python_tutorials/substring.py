"""
substring.py

Find the number of occurences of a substring in a string.

Input:
String to be searched
Substring

Output:
Number of occurences
"""

search_string = raw_input()
substring = raw_input()

count = 0
index = 0

while index < len(search_string):
    index = search_string.find(substring, index)
    if index == -1: break
    count++
    index += len(substring) - 1

print count
