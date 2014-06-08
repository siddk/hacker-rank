"""
utopian_tree.py

The Utopian tree goes through 2 cycles of growth every year. The first growth cycle of the tree is during the monsoon season when it doubles in height. The second growth cycle is during the summer when it increases in height by 1 meter. If a new Utopian tree sapling of height 1 meter is planted just before the onset of the monsoon season, can you find the height of the tree after N cycles?
"""

def get_height(cycles):
    height = 1
    cur_cycle = 0

    while (cur_cycle < cycles):
        if (cur_cycle % 2 == 0):
            height *= 2
            cur_cycle += 1
        else:
            height += 1
    print height

num_test_cases = input()
current_case = 0

while (current_case < num_test_cases):
    num_cycles = input()
    get_height(num_cycles)
    current_case += 1
