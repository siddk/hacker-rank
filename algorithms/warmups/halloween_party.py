"""
halloween_party.py

Alex is attending a Halloween party with his girlfriend Silvia. At the party, Silvia spots a giant chocolate bar. If the chocolate can be served as only 1 x 1 sized pieces and Alex can cut the chocolate bar exactly K times, what is the maximum number of chocolate pieces Alex can cut and give Silvia?
"""

num_test_cases = input()
current_test_case = 0

while (current_test_case < num_test_cases):
    num_cuts = input()
    # Cut logic
    horizontal_cuts = num_cuts / 2
    vertical_cuts = num_cuts - horizontal_cuts
    print horizontal_cuts * vertical_cuts
    current_test_case += 1
