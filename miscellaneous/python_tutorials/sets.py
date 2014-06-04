"""
sets.py

You are given two sets of integers M and N and you have to print their symmetric difference in ascending order. The first line of input contains the value of M followed by M integers, and then N and N integers. Symmetric difference is the values that exist in M or N but not in both.
"""

m = input()
m_lis = raw_input()
n = input()
n_lis = raw_input()

m_list = m_lis.split()
m_list = list(map(int, m_list))

n_list = n_lis.split()
n_list = list(map(int, n_list))

m_set = set(m_list)
n_set = set(n_list)

intersect = m_set.intersection(n_set)

for i in intersect:
    m_set.remove(i)
    n_set.remove(i)

union = m_set.union(n_set)

for i in sorted(union):
    print i
