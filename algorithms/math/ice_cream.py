# """
# ice_cream.py

# Sunny and Johnny together have M dollars which they intend to use at the ice cream parlour. Among N flavors
# available, they have to choose two distinct flavors whose cost equals M. Given a list of cost of N flavors,
# output the indices of two items whose sum equals M. The cost of a flavor (ci) will be no more than 10000.
#"""

if __name__ == "__main__":

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

        solution_set = []

        for i in valid_indices:
            for j in valid_indices[valid_indices.index(i) + 1:]:
                if (cost_list[i] + cost_list[j] == money):
                    solution_set.append((i + 1, j + 1))

        for sol_tuple in solution_set:
            print sol_tuple[0], sol_tuple[1]
