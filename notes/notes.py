# Activities


"""
 4.1.1: Functions: Factoring out a unit-conversion calculation.
 Write a function so that the main program below can be replaced by the simpler code that calls function mph_and_minutes_to_miles(). Original main program: 

miles_per_hour = float(input())
minutes_traveled = float(input())
hours_traveled = minutes_traveled / 60.0
miles_traveled = hours_traveled * miles_per_hour

print('Miles: {:f}'.format(miles_traveled))


Sample output with inputs: 70.0 100.0
Miles: 116.666667
"""

# def mph_and_minutes_to_miles(miles_per_hour, minutes_traveled):
#     hours_traveled = minutes_traveled / 60.0
#     miles_traveled = hours_traveled * miles_per_hour

#     return miles_traveled
    
    


# miles_per_hour = float(input())
# minutes_traveled = float(input())

# print('Miles: {:f}'.format(mph_and_minutes_to_miles(miles_per_hour, minutes_traveled)))


""" Challenge Activity 4.5.2: Return number of pennies in total.
Write a function number_of_pennies() that returns the total number of pennies given a number of dollars and (optionally) a number of pennies.

Sample output with inputs: 5 6 4
506
400 """

# def number_of_pennies(dollars, pennies=0):
    
#     total_pennies = (dollars * 100) + pennies
#     return total_pennies
# ''' Your solution goes here '''

# print(number_of_pennies(int(input()), int(input()))) # Both dollars and pennies
# print(number_of_pennies(int(input())))               # Dollars only



""" Challenge Activity 4.5.3: Default parameters: Calculate splitting a check between diners.
Write a split_check function that returns the amount that each diner must pay to cover the cost of the meal.

The function has 4 parameters:

bill: The amount of the bill.
people: The number of diners to split the bill between.
tax_percentage: The extra tax percentage to add to the bill.
tip_percentage: The extra tip percentage to add to the bill.
The tax or tip percentages are optional and may not be given when calling split_check. Use default parameter values of 0.15 (15%) for tip_percentage, and 0.09 (9%) for tax_percentage.

Sample output with inputs: 25 2

Cost per diner: 15.5
Sample output with inputs: 100 2 0.075 0.21

Cost per diner: 64.25 """



# # FIXME: Write the split_check function. HINT: Calculate the amount of tip and tax,
# # add to the bill total, then divide by the number of diners.
# def split_check(bill, people, tax_percentage = 0.09, tip_percentage = 0.15):
    
#     # print(bill, people, tax_percentage, tip_percentage)
#     subtotal = (bill * tax_percentage) + bill
#     total = (subtotal * tip_percentage) + subtotal
#     bill = total / people
#     return bill

# ''' Your solution goes here '''

# bill = float(input())
# people = int(input())

# # Cost per diner at the default tax and tip percentages
# print('Cost per diner:', split_check(bill, people))

# bill = float(input())
# people = int(input())
# new_tax_percentage = float(input())
# new_tip_percentage = float(input())

# # Cost per diner at different tax and tip percentages
# print('Cost per diner:', split_check(bill, people, new_tax_percentage, new_tip_percentage))



# print('done')


x = 0
y = 5
z = 10
while x < y:
    if x == z:
        print('x == z')
        break
    x += 1 
else:
    print('x == y')
