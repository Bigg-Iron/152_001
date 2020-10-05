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

# def backwards_alphabet(curr_letter):
#     if curr_letter == 'a':
#         print(curr_letter)
#     else:
#         print(curr_letter)
#         prev_letter = chr(ord(curr_letter) - 1)
#         backwards_alphabet(prev_letter)

# starting_letter = input()

# ''' Your solution goes here '''
# backwards_alphabet(starting_letter)


''' 12.2.1: Recursive function: Writing the base case.
Add an if branch to complete double_pennies()'s base case.

Sample output with inputs: 1 10
Number of pennies after 10 days: 1024


Note: If the submitted code has an infinite loop, the system will stop running the code after a few seconds, and report "Program end never reached." The system doesn't print the test case that caused the reported message.
'''

# Returns number of pennies if pennies are doubled num_days times
def double_pennies(num_pennies, num_days):
    total_pennies = 0

    ''' Your solution goes here '''
    if num_days == 0:
        total_pennies = num_pennies

    else:
        total_pennies = double_pennies((num_pennies * 2), (num_days - 1))

    return total_pennies

# Program computes pennies if you have 1 penny today,
# 2 pennies after one day, 4 after two days, and so on
starting_pennies = int(input())
user_days = int(input())

print('Number of pennies after', user_days, 'days: ', end="")
