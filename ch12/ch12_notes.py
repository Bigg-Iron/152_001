# Week 7 access code 153 674
""" Figure 12.3.1: Fibonacci sequence step-by-step. 

Output the Fibonacci sequence step-by-step.
Fibonacci sequence starts as:
0 1 1 2 3 5 8 13 21 ... in which the first
two numbers are 0 and 1 and each additional
number is the sum of the previous two numbers """

# def fibonacci(v1, v2, run_cnt):
#     print(v1, '+', v2, '=', v1+v2)

#     if run_cnt <= 1:  # Base case:
#                       # Ran for user's number of steps
#         pass  # Do nothing
#     else:             # Recursive case
#         fibonacci(v2, v1+v2, run_cnt-1)


# print ('This program outputs the\n'
#        'Fibonacci sequence step-by-step,\n'
#        'starting after the first 0 and 1.\n')

# run_for = int(input('How many steps would you like?'))

# fibonacci(0, 1, run_for)


""" Figure 12.5.2: Recursively searching a sorted list. """

# def find(lst, item, low, high):
#     """
#     Finds index of string in list of strings, else -1.
#     Searches only the index range low to high
#     Note: Upper/Lower case characters matter
#     """
#     range_size = (high - low) + 1
#     mid = (high + low) // 2

#     if item == lst[mid]:  # Base case 1: Found at mid
#         pos = mid
#     elif range_size == 1:  # Base case 2: Not found
#         pos = -1
#     else:  # Recursive search: Search lower or upper half
#         if item < lst[mid]:  # Search lower half
#             pos = find(lst, item, low, mid)
#         else:  # Search upper half
#             pos = find(lst, item, mid+1, high)

#     return pos

# attendees = []

# attendees.append('Adams, Mary')
# attendees.append('Carver, Michael')
# attendees.append('Domer, Hugo')
# attendees.append('Fredericks, Carlo')
# attendees.append('Li, Jie')

# name = input("Enter person's name: Last, First: ")
# pos = find(attendees, name, 0, len(attendees)-1)

# if pos >= 0:
#     print('Found at position {}.'.format(pos))
# else:
#     print('Not found.')



""" Figure 12.5.1: A recursive function find() carrying out a binary search algorithm. """

def find(low, high):
    mid = (high + low) // 2  # Midpoint of low..high
    answer  = input('Is it {}? (l/h/y): '.format(mid))

    if (answer != 'l') and (answer != 'h'):  # Base case
        print('Got it!')
    else:
        if answer == 'l':
            find(low, mid)
        else:
            find(mid+1, high)

print('Choose a number from 0 to 100.')
print('Answer with:')
print('   l (your num is lower)')
print('   h (your num is higher)')
print(' any other key (guess is right).')

find(0, 100)
