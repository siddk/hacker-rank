"""
service_lane.py

Calvin is driving his favorite vehicle on the 101 freeway. He notices that the check engine light of his vehicle is on, and he wants to service it immediately to avoid any risks. Luckily, a service lane runs parallel to the highway. The length of the highway and the service lane is N units. The service lane consists of N segments of unit length, where each segment can have different widths.

Calvin can enter into and exit from any segment. Let’s call the entry segment as index i and the exit segment as index j. Assume that the exit segment lies after the entry segment(j>i) and i ≥ 0. Calvin has to pass through all segments from index i to indexj (both inclusive).
"""

first_line = raw_input()
n_t = map(lambda x: int(x), first_line.split())

n = n_t[0]
t = n_t[1]

width_array = raw_input()
width_array = map(lambda x: int(x), width_array.split())

cur_test_case = 0

while (cur_test_case < t):
    
