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

user_num = int(input())
while user_num >= 1:
    user_num = user_num / 2
    print(user_num)

