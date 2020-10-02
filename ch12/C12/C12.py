""" CHALLENGE ACTIVITY
12.1.1: Calling a recursive function.
Write a statement that calls the recursive function backwards_alphabet() with input starting_letter.

Sample output with input: 'f'
f
e
d
c
b
a """

def backwards_alphabet(curr_letter):
    if curr_letter == 'a':
        print(curr_letter)
    else:
        print(curr_letter)
        prev_letter = chr(ord(curr_letter) - 1)
        backwards_alphabet(prev_letter)

starting_letter = input()

''' Your solution goes here '''
backwards_alphabet(starting_letter)
