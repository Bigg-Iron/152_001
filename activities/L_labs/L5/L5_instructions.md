# 5.11 L5 - Lab

Plan
Today's lab covers conditional expressions and the if statement.

Boolean Operators
The last lab covered operators used on floats and integers. This lab is going to look at operators on booleans. There are three boolean operators: not, and, and or.

not: Negates the value of a boolean. True becomes False and False becomes True.

print(not True)   <--- False
print(not False)  <--- True
and: Returns True if neither of the values are False.

print(True and False)    <--- False
print(True and True)     <--- True
print(False and False)   <--- False
or: Returns True if one or both of the values are True.

print(True or False)     <--- True
print(True or True)      <--- True
print(False or False)    <--- False
Operators that Return Booleans
It is not often in programming that we use expressions with boolean constants. We more regularly use operators whose return value is boolean. The boolean operators we are going to use most in this class are in, ==, !=, <, >, <=, >=.

in: Returns True if a list, tuple, string, etc. contains the specified value. Returns False otherwise.

print("a" in "Does this sentence use the letter a?")   <--- True
print(12 in [1,2,3,4,5,6,7,8,9,0])   <--- False

student_grades = {"Lin": 32, "Ameni": 93, "Kam": 97, "Lian": 95} 
print("Lin" in student_grades)       <--- True
print(95 in student_grades)          <--- True
Equal ( == ): Returns True if the values are the same.

print("Apple" == "Pear")     <--- False
print(12 == 12.0)            <--- True
Not equal ( != ): Returns True if the values are not the same.

print("Apple" != "Pear")      <--- True
Less than / greater than ( < / > ): Same as in math, returns True or False.

print(1 < 3 < 4)    <-- True
print(1 > 3 > 4)    <-- False
print(1 < 1)     <-- False
Less than or equal to / greater than or equal to( <= / >= ): Same as math, returns True or False.

print(1 <= 3 <= 4)  <-- True
print(1 >= 3 >= 4)  <-- False
print(1 >= 1)   <-- True
If statements
So far, the programs written in this class can't make decisions. In programming, we have a concept called conditional execution of code. This just means making a decision if we want to run some code.

if 12 < 0:
    print('Hello, I understand Math')
print('Done')
Notice that the if statement asks the question is 12 less then 0?, then if that statement is true then it runs the code in the body. Otherwise it skips the body.

The body of an if statement is the code that follows the if statement that is indented in by some amount of white space. This can be any amount of white space you desire as long as you remain consistent. It is common to use four spaces to indent.The body can have as many statements as you'd like.

age = int(input('Enter your age:\n'))
if age >= 15:
    print('You are allowed to drive.')
    print('Congrats!')
If Else
Sometimes we want to run some code or run some other but not both. This is done using the else statement.

age = int(input("Enter your age:\n"))
permission = ''
if age >= 15: 
    permission = "allowed"
else:
    permission = "not allowed"
print("You are", permission, "to drive")
Notice here else gets executed if the if is False

If Elif Else
Programmers often want to have a bunch of different conditions checked. This is done with the elif statement.

grade = float(input("Enter your grade:\n"))
if grade > 90.5:
    print("A")
elif grade > 80.5:
    print("B")
elif grade > 70.5:
    print("C")
elif grade > 60.5:
    print("D")
else:
    print("F")
Nested if
Sometimes we want to check a condition and then check some other sub conditions, this can be done using a nested if.

age = 18
if age < 18:
    print("You are not an adult")
    if age > 10:
          print("You are a teenager")
    if age < 3:
          print("You are a toddler")
else:
   print("You are an adult")
Notice this can also be done like this:

if age < 18 and age > 10:
    print("You are not an adult")
    print("You are a teenager")
elif age < 18 and age < 3:
    print("You are not an adult")
    print("You are a toddler")
else:
    print("You are an adult")
Lab Assignment
This lab's goal is to write a program that plays rock, paper, scissors.

The rules:

scissors win paper
paper win rock
rock win scissors
You'll notice the beginnings of the code have already been provided. Take a look at main and try to understand what the program is doing and what the provided code does.

This program should:

Prompt the human player to enter their selection: "rock, paper, or scissors?"
Print the outcome of the game, returning win, lose, or draw from player1's perspective.
if player1 is scissors and player2 is rock, the outcome is scissors lose rock.
Here are the specifications for the functions you will be writing:

human_player()

Takes no parameters.
Prompts the user to input rock, paper, or scissors?
Returns the user's selection as a string.
outcome(player1, player2)

Takes two parameters, player1 and player2, both are strings
Determines the result of the game using if, elif, and/or else statements. There are several different ways to go about this, do whatever you feel is best.
Returns win, lose, or draw as a string
Input Example 1:
Note: While testing in develop mode, don't forget to provide the program with input values in the smaller box below.

scissors
Output Example 1:
rock, paper, or scissors?
scissors draw scissors
Input Example 2:
paper
Output Example 2:
rock, paper, or scissors?
paper lose scissors
When testing your code, the computer_player/player2 will always choose scissors. This is by design.

Interesting but not crucial to understand explanation: When you are testing your code you'll notice that it always returns scissors. This is because of the seed function we call in main. Seeds make random number generators choose the same sequence of random number every time. We have set the seed for you so that when we test your output against ours it will always pick the same thing. If you'd like to actually play this game you can remove the seed function from main and it will pick random choices. Make sure you put the seed(42) back in to get full points.