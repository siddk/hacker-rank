"""
manasa_stones.py

Manasa is out on a hike with friends. She finds a trail of stones with numbers on them. She starts following the trail and notices that two consecutive stones have a difference of either a or b. Legend has it that there is a treasure trove at the end of the trail and if Manasa can guess the value of the last stone, the treasure would be hers. Given that the number on the first stone was 0, find all the possible values for the number on the last stone.
"""

num_test_cases = input()

for case in xrange(num_test_cases):
    num_steps = input()
    a = input()
    b = input()

    if b < a: a, b = b, a
