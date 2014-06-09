"""
filling_jars.py

Animesh has N empty candy jars, numbered from 1 to N, with infinite capacity. He performs M operations. Each operation is described by 3 integers a, b and k. Here, a and b are index of the jars, and k is the number of candies to be added inside each jar whose index lies between a and b (both inclusive). Can you tell the average number of candies after M operations?
"""

n_m = raw_input().split()
n_m = map(lambda x: int(x), n_m)
n = n_m[0]
m = n_m[1]

big_sum = 0

for operation in xrange(m):
    operate = raw_input().split()
    operate = map(lambda x: int(x), operate)

    for index in xrange(operate[0]-1, operate[1]):
        big_sum += operate[2]

print int(big_sum/n)
