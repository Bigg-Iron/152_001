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



user_tickets = int(input())

''' Your solution goes here '''
if user_tickets < 5:
    num_tickets = 1
else:
    num_tickets = user_tickets

print('Value of num_tickets:', num_tickets)

"""




""" 5.2.4: Multi-branch if-else statements: Print century.

Write an if-else statement with multiple branches.
If year is 2101 or later, print "Distant future" (without quotes). Otherwise, if year is 2001 or greater, print "21st century". Otherwise, if year is 1901 or greater, print "20th century". Else (1900 or earlier), print "Long ago".

Sample output with input: 1776
Long ago

 """

year = int(input())

# ''' Your solution goes here '''
if year >= 2101:
    print('Distant future')
    
elif year >= 2001:
    print('21st century')
    
elif year >= 1901:
    print('20th century')
    
else:
    print('Long ago')


print('...')
