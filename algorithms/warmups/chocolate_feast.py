"""
chocolate_feast.py

Little Bob loves chocolates, and goes to the store with $N money in his pocket. The price of each chocolate is $C. The store offers a discount: for every M wrappers he gives the store, he’ll get one chocolate for free. How many chocolates does Bob get to eat?
"""

num_test_cases = input()

for case in range(num_test_cases):
    N, C, M = [int(x) for x in raw_input().split(' ')]
    num_chocolates = 0

    num_chocolates += N / C
    num_wrappers = N / C

    while(num_wrappers > 0):
        if num_wrappers >= M:
            num_chocolates += num_wrappers / M
            num_wrappers -= num_wrappers / M
        else:
            break
    print num_chocolates
