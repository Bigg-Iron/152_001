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

num_rows = int(input())
num_cols = int(input())

for i in range(num_rows):
    for i in range(num_cols):
        print('*', end=' ')
    print()


''' 7.5.2: Nested loops: Print seats.
Given num_rows and num_cols, print a list of all seats in a theater. Rows are numbered, columns lettered, as in 1A or 3E. Print a space after each seat.

Sample output with inputs: 2 3
1A 1B 1C 2A 2B 2C  '''




''' 7.6.2: Simon says.
"Simon Says" is a memory game where "Simon" outputs a sequence of 10 characters (R, G, B, Y) and the user must repeat the sequence. Create a for loop that compares the two strings. For each match, add one point to user_score. Upon a mismatch, end the game.

Sample output with inputs: 'RRGBRYYBGY' 'RRGBBRYBGY'
User score: 4 '''

# user_score = 0
# simon_pattern = input()
# user_pattern  = input()

# ''' Your solution goes here '''
# for s in simon_pattern:
#     if s == user_pattern[user_score]:
#         user_score+=1
#     else:
#         break
 
# print(user_score)


''' 7.7.1: Loop Else 
Guess the output '''
# result = 1
# n = 3
# while n > -2:
#     print(n, end=' ')
#     result *= 3
#     n -= 1
# else:
#     print('\ {}'.format(result))
# print('done')

# -----------------------------------------------------

# result = 0
# n = 2
# while n > -5:
#     print(n, end=' ')
#     result -= 4
#     if result < -15:
#         print('*')
#         break
#     n -= 1
# else:
#     print('/ {}'.format(result))
# print('done')

# result = 0
# for n in range(4):
#     print(n, end=' ')
#     result += 4
# else:
#     print('| {}'.format(result))
# print('done')

# -----------------------------------------------------

# stop = -15
# total = 0
# for number in [7, 3, 7, 6, 2, 6]:
#     print(number, end=' ')
#     total -= number
#     if total < stop:
#         print('@')
#         break
# else:
#     print('| {}'.format(total))
# print('done')



''' 7.8.1: Output of functions with branches/loops. '''

# def print_message(message):
#     if len(message) > 6:
#         print('too long')
#     else:
#         print(message)

# print_message('Thank you so much!')
# print_message('Hi!')


# -----------------------------------------------------

# def compute(numbers):
#     result = 1
#     for num in numbers:
#         result *= num + 3
#     return result

# values = [5, 7, 6]
# computed_value = compute(values)
# print(computed_value)

# -----------------------------------------------------

# def get_numbers():
#     user_input = input()
#     values = []
#     for token in user_input.split():
#         values.append(int(token))
#     return values

# def print_selected_numbers():
#     numbers = get_numbers()
#     for number in numbers:
#         if number <= 2:
#             print(number)

# print_selected_numbers()


# -----------------------------------------------------

''' 
7.8.2: Function with branch: Popcorn.

Define function print_popcorn_time() with parameter bag_ounces. If bag_ounces is less than 3, print "Too small". If greater than 10, print "Too large". Otherwise, compute and print 6 * bag_ounces followed by "seconds". End with a newline.

Sample output with input: 7
42 seconds '''

# def print_popcorn_time(bag_ounces):
#     if bag_ounces < 3:
#         print("Too small")
#     elif bag_ounces > 10:
#         print("Too large")
#     else:
#         s = (6 * bag_ounces)
#         print('{} seconds'.format(s))
        
# ''' Your solution goes here '''

# user_ounces = int(input())
# print_popcorn_time(user_ounces)


''' 7.8.3: Function with loop: Shampoo.
Write a function shampoo_instructions() with parameter num_cycles. If num_cycles is less than 1, print "Too few.". If more than 4, print "Too many.". Else, print "N : Lather and rinse." num_cycles times, where N is the cycle number, followed by "Done.".

Sample output with input: 2
1 : Lather and rinse.
2 : Lather and rinse.
Done.
 
Hint: Define and use a loop variable. '''

# def shampoo_instructions(num_cycles):
#     i = 1
#     if num_cycles < 1:
#         print('Too few.')
#     elif num_cycles > 4:
#         print('Too many.')
#     else:
#         while i <= num_cycles:
#             print('{} : Lather and rinse.'.format(i))
#             i += 1
#         print('Done.')
        

# user_cycles = int(input())
# shampoo_instructions(user_cycles)


