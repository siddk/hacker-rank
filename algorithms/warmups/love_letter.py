"""
love_letter.py

James got hold of a love letter that his friend Harry has written for his girlfriend. Being the prankster that James is, he decides to meddle with it. He changes all the words in the letter into palindromes. For any given string, he can only decrease the value of any one of the letters, for example, ‘d’ will become ‘c’, etc. This will count as one operation. (Also, he can decrease the value of letters only till he reaches ‘a’. ‘a’ cannot be further reduced to ‘z’) Find the minimum number of operations he needs to carry out to convert a given string into a palindrome.
"""

num_test_cases = input()
cur_test_case = 0

while (cur_test_case < num_test_case):
    cur_test_case += 1
