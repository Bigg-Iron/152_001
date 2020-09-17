# Nested Loops: Histogram
# num = 0
# while num >= 0:
#     num = int(input('Enter an integer (negative to quit):\n'))

#     if num >= 0:
#         print('Depicted graphically:')
#         for i in range(num):
#             print('*', end=' ')
#         print('\n')

# print('Goodbye.')


# 7.6.2: Continue Statements 

# empanada_cost = 3
# taco_cost = 4

# user_money = int(input('Enter money for meal: '))

# num_diners = int(input('How many people are eating: '))

# max_empanadas = user_money // empanada_cost
# max_tacos = user_money // taco_cost

# meal_cost = 0
# num_options = 0
# for num_tacos in range(max_tacos + 1):
#     for num_empanadas in range(max_empanadas + 1):

#         # Total items purchased must be equally divisible by number of diners
#         if (num_tacos + num_empanadas) % num_diners != 0:
#             continue

#         meal_cost = (num_empanadas * empanada_cost) + (num_tacos * taco_cost)

#         if meal_cost == user_money:
#             print('${} buys {} empanadas and {} tacos without change.'
#                   .format(meal_cost, num_empanadas, num_tacos))
#             num_options += 1

# if num_options == 0:
#     print('You cannot buy a meal without having change left over.')



'''
Nested Loops:
Program to print all 2-letter domain names.
Note that ord() and chr() convert between text and ASCII/ Unicode encodings.
ord('a') is 97. ord('b') is 98, and so on. chr(99) is 'c', etc.
'''
print('Two-letter domain names:')

letter1 = 'a'
letter2 = '?'
while letter1 <= 'z':  # Outer loop
    letter2 = 'a'
    while letter2 <= 'z':  # Inner loop
        print('{}{}.com'.format(letter1, letter2))
        letter2 = chr(ord(letter2) + 1)
    letter1 = chr(ord(letter1) + 1)

