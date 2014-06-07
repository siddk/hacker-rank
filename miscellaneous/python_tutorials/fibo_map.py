"""
fibo_map.py

Given a number N, generate a list of the first N fibonacci numbers, then print the list, with each element cubed.
"""

number = int(input())
count = 0
fibo_list = []

while (count < number):
    if count == 0:
        fibo_list.append(0)
        count += 1
    elif count == 1:
        fibo_list.append(1)
        count += 1
    else:
        fibo_list.append(fibo_list[count-1] + fibo_list[count-2])

print fibo_list
