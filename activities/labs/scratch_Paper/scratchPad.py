# Pizza area --------------------------------------------------------------------------------------------------------

# def print_pizza_area(pizza_diameter):
#     pi_val = 3.14159265
#     pizza_radius = pizza_diameter / 2.0
#     pizza_area = pi_val * pizza_radius * pizza_radius
#     print('{:.1f} inch pizza is {:.3f} inches squared'
#           .format(pizza_diameter, pizza_area))

# print_pizza_area(12.0)
# print_pizza_area(16.0)


# EOF error on input() testing vscode --------------------------------------------------------------------------------------------------------

# import io

# # EOF error on input()
# print('Enter your name:')
# x = input()
# print('Hello, ' + x)


# Prints face --------------------------------------------------------------------------------------------------------

# nose = '0'  # Looks a little like a nose
# user_value = '-'

# while user_value != 'q':
#     print(' {} {} '.format(user_value, user_value))  # Print eyes
#     print('  {}  '.format(nose))  # Print nose
#     print(user_value*5)  # Print mouth
#     print('\n')

#     # Get new character for eyes and mouth
#     user_input = input("Enter a character ('q' for quit): \n")
#     user_value = user_input[0]

# print('Goodbye.\n')


# Program that calculates savings and interest--------------------------------------------------------------------------------------------------------

# initial_savings = 5000
# interest_rate = 0.03

# print('Initial savings of ${}'.format(initial_savings))
# print('at {:.0f}% yearly interest.\n'.format(interest_rate*100))

# years = int(input('Enter years: '))
# print()

# savings = initial_savings
# i = 1  # Loop variable
# while i <= years:  # Loop condition
#     print(' Savings at beginning of year {}: ${:.2f}'.format(i, savings))
#     savings = savings + (savings*interest_rate)
#     i = i + 1  # Increment loop variable

# print('\n')


# 6.4.1 Loops --------------------------------------------------------------------------------------------------------
# print('Enter a number')
# target = int(input())
# print('Enter another number')
# n = int(input())

# while n <= target:
#     print(n * 2)
#     n += 1


# Loops with variables that count --------------------------------------
# print('Enter a number: ')
# target = int(input())
# print('Enter another number: ')
# n = int(input())
# step = 2
# while n <= target:
#     print('\n ...', n * 2)
#     n += step


# L6 countDown practice --------------------------------------------------------------------------------------------------------

# def countDown(first, last):
#     if first >= last:
#         # increment by -1
#         for i in range(first, last-1, -1):
#             print(i, end=", ")
#         print()
#     else:
#         # increment by -1
#         for i in range(last, first-1, -1):
#             print(i, end=", ")
#         print()


# # Get user input of two integers
# first = int(input("Enter an Integer: "))
# last = int(input("Enter another Integer: "))

# countDown(first, last)

# print('END...')


# 3.2.1 Challenge Activity  --------------------------------------------------------------------------------------------------------

# avg_sales = 0

# num_sales1 = int(input())
# num_sales2 = int(input())
# num_sales3 = int(input())


# avg_sales = (num_sales1 + num_sales2 + num_sales3) / 3


# print('Average sales: {:.2f}'.format(avg_sales))
# print('done')


# 3.2.2 Challenge Activity Sphere Volume --------------------------------------------------------------------------------------------------------

# Given sphere_radius and pi, compute the volume of a sphere and assign sphere_volume with the volume. Volume of sphere = (4.0 / 3.0) π r3

# Sample output with input: 1.0
# Sphere volume: 4.19

# pi = 3.14159
# sphere_volume = 0.0

# sphere_radius = float(input())

# ''' Your solution goes here '''
# sphere_volume = (4.0 / 3.0) * pi * sphere_radius ** 3

# print('Sphere volume: {:.2f}'.format(sphere_volume))

# print('done')



# 3.2.3 Challenge Activity: Acceleration of Gravity --------------------------------------------------------------------------------------------------------

# ''' Compute the approximate acceleration of gravity for an object above the earth's surface, assigning accel_gravity with the result. The expression for the acceleration of gravity is: (G * M) / (d^2), where G is the gravitational constant 6.673 x 10-11, M is the mass of the earth 5.98 x 1024 (in kg), and d is the distance in meters from the Earth's center (stored in variable dist_center).

# Sample output with input: 6.3782e6 (100 m above the Earth's surface at the equator)
# Acceleration of gravity: 9.81 '''

# G = 6.673e-11
# M = 5.98e24
# accel_gravity = 0.0

# dist_center = float(input())

# ''' Your solution goes here '''
# accel_gravity = (G * M) / dist_center ** 2

# print('Acceleration of gravity: {:.2f}'.format(accel_gravity))
# print('done')


# 3.3.2 Challenge Activity: Compute Change  --------------------------------------------------------------------------------------------------------

# ''' A cashier distributes change using the maximum number of five-dollar bills, followed by one-dollar bills. Write a single statement that assigns num_ones with the number of distributed one-dollar bills given amount_to_change. Hint: Use %.

# Sample output with input: 19
# Change for $ 19
# 3 five dollar bill(s) and 4 one dollar bill(s) '''


# amount_to_change = int(input())

# num_fives = amount_to_change // 5

# ''' Your solution goes here '''
# num_ones = amount_to_change - (num_fives * 5)

# print('Change for $', amount_to_change)
# print(num_fives, 'five dollar bill(s) and', num_ones, 'one dollar bill(s)')


# 3.4.2 Challenge Activity: Typecasting: Computing average owls per zoo  --------------------------------------------------------------------------------------------------------

# ''' Assign avg_owls with the average owls per zoo. Print avg_owls as an integer.

# Sample output for inputs: 1 2 4
# Average owls per zoo: 2 '''


# avg_owls = 0.0

# num_owls_zooA = int(input())
# num_owls_zooB = int(input())
# num_owls_zooC = int(input())

# ''' Your solution goes here '''
# avg_owls = (num_owls_zooA + num_owls_zooB + num_owls_zooC) / 3


# print('Average owls per zoo:', int(avg_owls))




# 3.4.3: Type casting: Reading and adding values.
#   --------------------------------------------------------------------------------------------------------

# ''' Assign total_owls with the sum of num_owls_A and num_owls_B.

# Sample output with inputs: 3 4
# Number of owls: 7 '''


# total_owls = 0

# num_owls_A = input()
# num_owls_B = input()

# ''' Your solution goes here '''
# total_owls = int(num_owls_A) + int(num_owls_B)


# print('Number of owls:', total_owls)



# 3.6.2: Basic function call.
#   --------------------------------------------------------------------------------------------------------

# ''' Complete the function definition to output the hours given minutes.

# Sample output with input: 210.0
# 3.5 '''

# def output_minutes_as_hours(orig_minutes):
    
#     ''' Your solution goes here '''
#     x = orig_minutes / 60
#     print(x)

# minutes = float(input())
# output_minutes_as_hours(minutes)



# 3.6.3: Function call with parameters: Converting measurements.
#    --------------------------------------------------------------------------------------------------------

# Define a function print_total_inches, with parameters num_feet and num_inches, that prints the total number of inches. Note: There are 12 inches in a foot.

# Sample output with inputs: 5 8
# Total inches: 68 


# def print_total_inches(num_feet, num_inches):
#     total_inches = (feet * 12) + num_inches
#     print('Total inches: ', total_inches)
# ''' Your solution goes here '''

# feet = int(input())
# inches = int(input())
# print_total_inches(feet, inches)


#    --------------------------------------------------------------------------------------------------------

# ''' zyDE 3.7.1: List argument modification.
# Address the FIXME comments. Move the respective code from the while-loop to the created function. The add_grade function has already been created.

# Note: split() and strip() are string methods further explained elsewhere. split() separates a string into tokens using any whitespace as the default separator. The tokens are returned in a list (i.e., 'a b c'.split() returns ['a', 'b', 'c']). strip() returns a copy of a string with leading and trailing whitespace removed. '''


# def add_grade(student_grades):
#     print('Entering grade. \n')
#     name, grade = input(grade_prompt).split()
#     student_grades[name] = grade

# # FIXME: Create delete_name function
# def delete_name():
#     print('Deleting grade.\n')
#     name = input(delete_prompt)
#     del student_grades[name]

# # FIXME: Create print_grades function
# def print_grades():
#     print('Printing grades.\n')
#     for name, grade in student_grades.items():
#         print(name, 'has a', grade)
    

# student_grades = {}  # Create an empty dict
# grade_prompt = "Enter name and grade (Ex. 'Bob A+'):\n"
# delete_prompt = "Enter name to delete:\n"
# menu_prompt = ("1. Add/modify student grade\n"
#                 "2. Delete student grade\n"
#                 "3. Print student grades\n"
#                 "4. Quit\n\n")

# command = input(menu_prompt).lower().strip()

# while command != '4':  # Exit when user enters '4'
#     if command == '1':
#         add_grade(student_grades)
#     elif command == '2':
#         # FIXME: Only call delete_name() here
#         delete_name()
#     elif command == '3':
#         # FIXME: Only call print_grades() here
#         print_grades()
#     else:
#         print('Unrecognized command.\n')

#     command = input().lower().strip()



# 3.7.1: Change order of elements in function list argument.--------------------------------------------------------------------------------------------------------

# def swap(values_list):
       
#     size = len(values_list) 
#     # Swapping  
#     temp = values_list[0] 
#     values_list[0] = values_list[size - 1] 
#     values_list[size - 1] = temp 
    
    
# ''' Your solution goes here '''

# values_list = input().split(',')  # Program receives comma-separated values like 5,4,12,19
# swap(values_list)




# values_list = input().split(',')  # Program receives comma-separated values like 5,4,12,19
# swap(values_list)

# print(values_list)



# 3.8.3: Function definition: Volume of a pyramid. --------------------------------------------------------------------------------------------------------

# ''' Define a function pyramid_volume with parameters base_length, base_width, and pyramid_height, that returns the volume of a pyramid with a rectangular base.

# Sample output with inputs: 4.5 2.1 3.0
# Volume for 4.5, 2.1, 3.0 is: 9.45
# Relevant geometry equations:
# Volume = base area x height x 1/3
# Base area = base length x base width. '''


# ''' Your solution goes here '''
# def pyramid_volume(base_length, base_width, pyramid_height):
    
#     base_area = base_length * base_width
#     volume = base_area * pyramid_height * (1/3)
    
#     return volume

# length = float(input())
# width = float(input())
# height = float(input())
# print('Volume for 4.5, 2.1, 3.0 is:', pyramid_volume(length, width, height))



""" Write a function so that the main program below can be replaced by the simpler code that calls function mph_and_minutes_to_miles(). Original main program: 

miles_per_hour = float(input())
minutes_traveled = float(input())
hours_traveled = minutes_traveled / 60.0
miles_traveled = hours_traveled * miles_per_hour

print('Miles: {:f}'.format(miles_traveled))


Sample output with inputs: 70.0 100.0
Miles: 116.666667
"""

def mph_and_minutes_to_miles(miles_per_hour, minutes_traveled):
    hours_traveled = minutes_traveled / 60.0
    miles_traveled = hours_traveled * miles_per_hour
    
# ''' Your solution goes here '''

miles_per_hour = float(input())
minutes_traveled = float(input())

print('Miles: {:f}'.format(mph_and_minutes_to_miles(miles_per_hour, minutes_traveled)))


print('done')
