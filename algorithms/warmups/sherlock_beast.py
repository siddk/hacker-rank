"""
sherlock_beast.py

Sherlock Holmes is getting paranoid about Professor Moriarty, his archenemy. All his efforts to subdue Moriarty have been in vain. These days Sherlock is working on a problem with Dr. Watson. Watson mentioned that the CIA has been facing weird problems with their supercomputer, ‘The Beast’, recently.

This afternoon, Sherlock received a note from Moriarty, saying that he has infected ‘The Beast’ with a virus. Moreover, the note had the number N printed on it. After doing some calculations, Sherlock figured out that the key to remove the virus is the largest ‘Decent’ Number having N digits.

A ‘Decent’ Number has -
1. Only 3 and 5 as its digits.
2. Number of times 3 appears is divisible by 5.
3. Number of times 5 appears is divisible by 3.

Meanwhile, the counter to destruction of ‘The Beast’ is running very fast. Can you save ‘The Beast’, and find the key before Sherlock?
"""

num_test_cases = input()

for case in xrange(num_test_cases):
    num_digits = input()
    temp = num_digits
    num_fives = 0
    num_threes = 0

    while(temp > 0):
        if (temp % 3 == 0):
            num_fives = temp
            break;
        temp -= 5

    if (temp < 0) or ((num_digits - num_fives) % 5 != 0):
        print "-1"

    else:
        num_threes = num_digits - num_fives
