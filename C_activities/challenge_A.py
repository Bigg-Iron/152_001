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

 """


""" 5.3.2: Multiple if statements: Printing car features.
Write multiple if statements. If car_year is 1969 or earlier, print "Few safety features." If 1970 or later, print "Probably has seat belts." If 1990 or later, print "Probably has antilock brakes." If 2000 or later, print "Probably has airbags." End each phrase with a period and a newline.

Sample output for input: 1995
Probably has seat belts.
Probably has antilock brakes.


car_year = int(input())

''' Your solution goes here '''
if car_year <= 1969:
    print('Few safety features.\n')
    
if car_year >= 1970:
    print('Probably has seat belts.')
    
if car_year >= 1990:
    print('Probably has antilock brakes.')
    
if car_year >= 2000:
    print('Probably has airbags.\n')
    
"""


""" 5.4.1: Indentation: Fix the program.

Retype the below code. Fix the indentation as necessary to make the program work.
    if 'New York' in temperatures:
        if temperatures['New York'] > 90:
        print('The city is melting!')
        else:
            print('The temperature in New York is', temperatures['New York'])
else:
        print('The temperature in New York is unknown.')
Sample output with input: 105

The city is melting!

temperatures = {
    'Seattle': 56.5,
    'New York': float(input()),
    'Kansas City': 81.9,
    'Los Angeles': 76.5
}

''' Your solution goes here '''
if 'New York' in temperatures:
    if temperatures['New York'] > 90:
        print('The city is melting!')
    else:
        print('The temperature in New York is', temperatures['New York'])

else:
    print('The temperature in New York is unknown.')

"""



""" 5.5.2: Relational operators.

Write an expression that will print "Dollar or more" if the value of num_cents is at least a dollar (100 cents is a dollar).

Sample output with input: 109
Dollar or more

num_cents = int(input())
if num_cents >= 100:
    print('Dollar or more')
else:
    print('not a dollar')
 """
 
 
""" 5.5.3: If-else expression: Operator chaining.

Write an expression that will print "in high school" if the value of user_grade is between 9 and 12 (inclusive).

Sample output with input: 10
in high school


user_grade = int(input())
if 9 <= user_grade <= 12:
    print('in high school')
else:
    print('not in high school')
 """



""" 5.6.2: Boolean operators: Detect specific values.
Write an expression using Boolean operators that prints "Special number" if special_num is -99, 0, or 44.

Sample output with input: 17
Not special number 


special_num = int(input())

if special_num == -99 or special_num == 0 or special_num == 44:
    print('Special number')
else:
    print('Not special number')
"""



""" 5.6.3: Boolean operators: Combining test conditions.

Write an expression using Boolean operators that prints "Eligible" if user_age is greater than 17 and not equal to 25.

Sample output with input: 17
Ineligible

user_age = int(input())

if user_age > 17 and user_age != 25:
    print('Eligible')
else:
    print('Ineligible')
"""



""" 5.6.4: Boolean operators: Branching using Boolean variables.
Write an expression that prints 'You must be rich!' if the variables young and famous are both True.

Sample output with inputs: 'True' 'True'
You must be rich! 


young = (input() == 'True')
famous = (input() == 'True')

if young and famous:
    print('You must be rich!')
else:
    print('There is always the lottery...')
"""



""" 5.7.2: Boolean operators: Detect specific values.

Write an expression using membership operators that prints "Special number" if special_num is one of the special numbers stored in the list special_list = [-99, 0, or 44].

Sample output with input: 17
Not special number


special_list = [-99, 0, 44]
special_num = int(input())

if special_num in special_list:
    print('Special number')
else:
    print('Not special number')
"""



""" 5.9.2: Conditional expression: Print negative or non-negative.

Create a conditional expression that evaluates to string "negative" if user_val is less than 0, and "non-negative" otherwise.

Sample output with input: -9
-9 is negative """


# user_val = int(input())

# cond_str = "negative" if user_val < 0 else "non-negative"

# print(user_val, 'is', cond_str)
 
 

""" 5.9.3: Conditional expression: Conditional assignment.

Using a conditional expression, write a statement that increments num_users if update_direction is 3, otherwise decrements num_users.

Sample output with inputs: 8 3
New value is: 9 """



num_users = int(input())
update_direction = int(input())

num_users = num_users + 1 if update_direction == 3 else num_users - 1

print('New value is:', num_users)



print('...')
