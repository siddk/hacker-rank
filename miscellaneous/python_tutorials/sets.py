"""
sets.py

You are given two sets of integers M and N and you have to print their symmetric difference in ascending order. The first line of input contains the value of M followed by M integers, and then N and N integers. Symmetric difference is the values that exist in M or N but not in both.
"""

m = input()
m_list = input()
n = input()
n_list = input()

m_list = m_list.split()
m_list = list(map(int, m_list))

n_list = n_list.split()
n_list = list(map(int, n_list))
