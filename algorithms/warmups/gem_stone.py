"""
gem_stone.py

John has discovered various rocks. Each rock is composed of various elements, and each element is represented by a lowercase latin letter from ‘a’ to ‘z’. An element can be present multiple times in a rock. An element is called a ‘gem-element’ if it occurs at least once in each of the rocks.

Given the list of rocks with their compositions, you have to print how many different kinds of gem-elements he has.
"""

num_test_cases = input()
cur_case = 0
intersection_set = set()

while (cur_case < num_test_cases):
    if (cur_case == 0):
        gem = raw_input()
        for element in gem:
            intersection_set.add(element)
        cur_case += 1
    else:
        gem = raw_input()
        cur_set = set()
        for element in gem:
            cur_set.add(element)
        intersection_set = intersection_set.intersection(cur_set)
        cur_case += 1
#Print answer
print len(intersection_set)
