''' 6.2.2: Basic while loop with user input.
Write an expression that executes the loop body as long as the user enters a non-negative number.

Note: If the submitted code has an infinite loop, the system will stop running the code after a few seconds and report "Program end never reached." The system doesn't print the test case that caused the reported message.

Sample outputs with inputs: 9 5 2 -1
Body
Body
Body
Done.
'''

# user_num = int(input())
# while user_num >= 0:
#   print('Body')
#   user_num = int(input())

# print('Done.')


''' 6.2.3: Basic while loop expression.
Write a while loop that repeats while user_num ≥ 1. In each loop iteration, divide user_num by 2, then print user_num.

Sample output with input: 20
10.0
5.0
2.5
1.25
0.625


Note: If the submitted code has an infinite loop, the system will stop running the code after a few seconds and report "Program end never reached." The system doesn't print the test case that caused the reported message. '''

# user_num = int(input())
# while user_num >= 1:
#     user_num = user_num / 2
#     print(user_num)



''' 6.3.2: Bidding example.
Write an expression that continues to bid until the user enters 'n'.

Sample output with inputs: 'y' 'y' 'n'
I'll bid $7!
Continue bidding? I'll bid $15!
Continue bidding? I'll bid $23!
Continue bidding?  '''

# import random
# random.seed(5)

# keep_going = '-'
# next_bid = 0

# while keep_going != 'n':
#    next_bid = next_bid + random.randint(1, 10)
#    print('I\'ll bid ${}!'.format(next_bid))
#    print('Continue bidding?', end=' ')
#    keep_going = input()
   

''' 6.3.3: While loop: Insect growth.
Given positive integer num_insects, write a while loop that prints, then doubles, num_insects each iteration. Print values ≤ 100. Follow each number with a space.

Sample output with input: 8
8 16 32 64 '''


num_insects = int(input()) # Must be >= 1

while num_insects > 0 and num_insects <= 100:
    print(num_insects, end = ' ')
    num_insects = num_insects * 2

    

