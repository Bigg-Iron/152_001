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

# num_guesses = int(input())
# user_guesses = []

# ''' Your solution goes here '''
# for index in range(num_guesses):
#     user_guesses.append(int(input()))
    
# print('user_guesses:', user_guesses)


"""10.3.2: Sum extra credit.
Assign sum_extra with the total extra credit received given list test_grades. Full credit is 100, so anything over 100 is extra credit. For the given program, sum_extra is 8 because 1 + 0 + 7 + 0 is 8.

Sample output for the given program with input: '101 83 107 90'
Sum extra: 8"""

user_input = input()
test_grades = list(map(int, user_input.split())) # contains test scores

sum_extra = -999 # Initialize 0 before your loop

''' Your solution goes here '''
sum_extra = 0
for grade in test_grades:
    if (grade > 100):
       sum_extra += grade - 100 

print('Sum extra:', sum_extra)

