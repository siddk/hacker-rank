"""
sub_max.py

Find the second largest number in a list.
"""

len_list = int(input())
str_list = raw_input()

str_list = map(lambda x: int(x), str_list.split())

cur_max = max(str_list)

#Check for duplicates
while(True):
    str_list.remove(cur_max)
    if max(str_list) == cur_max:
        continue
    else:
        break

print max(str_list)
