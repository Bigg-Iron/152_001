""" 10.1.2: Modify a list.
Modify short_names by deleting the first element and changing the last element to Joe.

Sample output with input: 'Gertrude Sam Ann Joseph'
['Sam', 'Ann', 'Joe']
 """
 
# user_input = input()
# short_names = user_input.split()

# ''' Your solution goes here '''
# del short_names[0]
# del short_names[-1]
# short_names.append('Joe')
# print(short_names)


""" 10.2.1: Reverse sort of list.
Sort short_names in reverse alphabetic order.

Sample output with input: 'Jan Sam Ann Joe Tod'
['Tod', 'Sam', 'Joe', 'Jan', 'Ann'] """

# user_input = input()
# short_names = user_input.split()

# ''' Your solution goes here '''
# short_names.sort()
# short_names.reverse()
# print(short_names)

""" 10.3.1: Get user guesses.
Write a loop to populate the list user_guesses with a number of guesses. The variable num_guesses is the number of guesses the user will have, which is read first as an integer. Read integers one at a time using int(input()).

Sample output with input: '3 9 5 2'
user_guesses: [9, 5, 2] """

num_guesses = int(input())
user_guesses = []

''' Your solution goes here '''
for index in range(num_guesses):
    user_guesses.append(int(input()))
    
print('user_guesses:', user_guesses)
