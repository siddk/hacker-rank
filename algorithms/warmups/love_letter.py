"""
love_letter.py

James got hold of a love letter that his friend Harry has written for his girlfriend. Being the prankster that James is, he decides to meddle with it. He changes all the words in the letter into palindromes. For any given string, he can only decrease the value of any one of the letters, for example, ‘d’ will become ‘c’, etc. This will count as one operation. (Also, he can decrease the value of letters only till he reaches ‘a’. ‘a’ cannot be further reduced to ‘z’) Find the minimum number of operations he needs to carry out to convert a given string into a palindrome.
"""

def find_palindrome(target_string):
    length = len(target_string)
    front = ""
    back = ""
    if (length % 2 == 0):
        front = target_string[:length/2]
        back = target_string[length/2:]
    else:
        front = target_string[:length/2]
        back = target_string[length/2 + 1:]

    #Reverse back, to do side by side comparison with front string
    back = back[::-1]
    num_changes = 0

    for index in xrange(len(front)):
        temp_changes = abs(ord(back[index]) - ord(front[index]))
        num_changes += temp_changes

    print num_changes



num_test_cases = input()
cur_test_case = 0

while (cur_test_case < num_test_cases):
    target_string = raw_input()
    find_palindrome(target_string)
    cur_test_case += 1
