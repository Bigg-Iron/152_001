# For loops
# channels = {
#     'MTV': 35,
#     'CNN': 28,
#     'FOX': 11,
#     'NBC': 4,
#     'CBS': 12
# }

# for c in channels:
#     print('{} is on channel {}'.format(c, channels[c]))

''' 7.2.2: For loop: Printing a list
Write an expression to print each price in stock_prices.

Sample output with inputs: 34.62 76.30 85.05
$ 34.62
$ 76.30
$ 85.05 '''

# NOTE: The following statement converts the input into a list container
# stock_prices = input().split()

# for price in stock_prices:
#     print('$', price)


''' 7.2.3: For loop: Printing a dictionary
Write a for loop to print each contact in contact_emails.

Sample output with inputs: 'Alf' 'alf1@hmail.com'
mike.filt@bmail.com is Mike Filt
s.reyn@email.com is Sue Reyn
narty042@nmail.com is Nate Arty
alf1@hmail.com is Alf '''

# contact_emails = {
#     'Sue Reyn' : 's.reyn@email.com',
#     'Mike Filt': 'mike.filt@bmail.com',
#     'Nate Arty': 'narty042@nmail.com'
# }

# new_contact = input()
# new_email = input()
# contact_emails[new_contact] = new_email

# ''' Your solution goes here '''
# for contact in contact_emails:
#     print('{} is {}'.format(contact_emails[contact], contact))



''' 7.5.1: Nested loops: Print rectangle
Given the number of rows and the number of columns, write nested loops to print a rectangle.

Sample output with inputs: 2 3
* * * 
* * * 
'''

# num_rows = int(input())
# num_cols = int(input())

# for i in range(num_rows):
#     for i in range(num_cols):
#         print('*', end=' ')
#     print()


''' 7.5.2: Nested loops: Print seats.
Given num_rows and num_cols, print a list of all seats in a theater. Rows are numbered, columns lettered, as in 1A or 3E. Print a space after each seat.

Sample output with inputs: 2 3
1A 1B 1C 2A 2B 2C  '''




''' 7.6.2: Simon says.
"Simon Says" is a memory game where "Simon" outputs a sequence of 10 characters (R, G, B, Y) and the user must repeat the sequence. Create a for loop that compares the two strings. For each match, add one point to user_score. Upon a mismatch, end the game.

Sample output with inputs: 'RRGBRYYBGY' 'RRGBBRYBGY'
User score: 4 '''

user_score = 0
simon_pattern = input()
user_pattern  = input()

''' Your solution goes here '''
for s in simon_pattern:
    if s == user_pattern[user_score]:
        user_score+=1
    else:
        break
 
print(user_score)

