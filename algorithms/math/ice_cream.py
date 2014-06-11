"""
ice_cream.py

Sunny and Johnny together have M dollars which they intend to use at the ice cream parlour. Among N flavors available, they have to choose two distinct flavors whose cost equals M. Given a list of cost of N flavors, output the indices of two items whose sum equals M. The cost of a flavor (ci) will be no more than 10000.
"""

num_test_cases = input()

for case in xrange(num_test_cases):
    money = input()
    num_flavors = input()
    costs = raw_input().split()

    valid_indices = []
    cost_list = []
    index_count = 0

    for price in costs:
        price = int(price)
        if price < money:
            valid_indices.append(index_count)
            cost_list.append(price)
        else:
            cost_list.append(price)

        index_count += 1
