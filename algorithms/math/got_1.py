"""
got_1.py

King Robert has 7 kingdoms under his rule. He gets to know from Raven that the Dothraki are going to wage a war against him soon. But, he knows the Dothraki need to cross the narrow river to enter his dynasty. There is only one bridge that connects both sides of the river which is sealed by a huge door.

The king wants to lock the door, so that, the Dothraki can’t enter. But, to lock the door he needs a key that is an anagram of a certain palindrome string.

The king has a list of words. Help him figure out if any anagram of the words can be a palindrome or not?
"""

input_string = raw_input()

letter_list = []
letter_count = []

for letter in input_string:
    if letter in letter_list:
        letter_count[letter_list.index(letter)] += 1
    else:
        letter_list.append(letter)
        letter_count.append(1)
