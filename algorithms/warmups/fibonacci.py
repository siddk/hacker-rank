"""
fibonacci.py

You are given an integer, N. Find out if the number is an element of fibonacci series.

The first few elements of fibonacci series are 0,1,1,2,3,5,8,13…. A fibonacci series is one where every element is a sum of the previous two elements in the series. The first two elements are 0 and 1.

Formally:

fib0 = 0
fib1 = 1
fibn = fibn-1 + fibn-2 ∀ n > 1
"""

#NOTE: I learned earlier in math that a number is only a fibonacci number if 5n^2 + 4 or 5n^2 - 4 is a perfect square, so check for this to get a somewhat optimal solution time.

num_test_cases = input()

for case in xrange(num_test_case):
    n = input()
