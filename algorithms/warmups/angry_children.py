"""
angry_children.py

Bill Gates is on one of his philanthropic journeys to a village in Utopia. He has N packets of candies and would like to distribute one packet to each of the K children in the village (each packet may contain different number of candies). To avoid any fighting among the children, he would like to pick K out of N packets, such that unfairness is minimized.

Suppose the K packets have (x1, x2, x3,….xk) candies in them, where xi denotes the number of candies in the ith packet, then we define unfairness as

max(x1,x2,…xk) - min(x1,x2,…xk)

where max denotes the highest value amongst the elements, and min denotes the least value amongst the elements. Can you figure out the minimum unfairness and print it?
"""

n = input()
k = input()

candies = [input() for _ in range(0,n)]

#If list of candies is sorted, then solution set will be a set of consecutive elements
candies.sort()

min_diff = "x"
start_index = 0
end_index = k-1

while end_index < n:
    cur_fairness = candies[end_index] - candies[start_index]
    if min_diff == "x": min_diff = cur_fairness
    elif cur_fairness < min_diff: min_diff = cur_fairness

    start_index += 1
    end_index += 1

print min_diff
