# Challenge Activities 

"""  5.2.2: Basic if-else expression.
 Write an expression that will cause the following code to print "18 or less" if the value of user_age is 18 or less. Write only the expression.

Sample output with input: 17
18 or less 


user_age = int(input())
if user_age <= 18:
   print('18 or less')
else:
   print('Over 18')

"""


""" 5.2.3: Basic if-else.
Write an if-else statement for the following:
If user_tickets is less than 5, assign num_tickets with 1. Else, assign num_tickets with user_tickets.

Sample output with input: 3
Value of num_tickets: 1

"""


user_tickets = int(input())

''' Your solution goes here '''
if user_tickets < 5:
    num_tickets = 1
else:
    num_tickets = user_tickets

print('Value of num_tickets:', num_tickets)




print('...')
