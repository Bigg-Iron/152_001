""" 
4.12 L4 - Lab 

Plan
For today's lab we are going to discuss functions, and practice scope and working with multiple return values.

Course Logistics Reminder
ZyBooks is the primary learning tool for this class. All course material originates here; readings, labs, and assignments. To complete labs and programs in zyBooks, write code in the large Lab Activity box at the bottom of the page. Most assignments require inputs to run, which are entered in the smaller box below labeled Enter program input (optional). To run code, there are two options available, Develop mode and Submit mode:

Develop mode is where code may be tested as many times as needed and is not graded.
Submit mode is used when code is ready to be graded. Starting in chapter 5, there will only be 10 submission attempts available, so it is encouraged that code is thoroughly tested in develop mode before being submitted for grading.
The purpose of the labs is to get guided programming practice. The skills taught in the labs will help develop practical experience on concepts discussed in readings and lectures. The content taught in labs will be used in assignments. Each mini-lab assignment will be graded.

CS152 is a fast-paced course. It is only 8 weeks and there will be a substantial amount of work. That said, the class is not intended to make life difficult -- if you feel yourself falling behind please reach out to a TA or the professor as soon as possible. They are there to help you learn!

Reading/Participation is due before class. Everything else is due at midnight the following day.

For the following sections, run the example code yourself to see their outputs. Here is a blank program to paste the code snippets into.

Scope
In the first week of this class, we had not learned functions yet so we just wrote our code wherever we wanted in the file. The lines we wrote were executed top to bottom. Our programs looked something like this:

firstName = input("Enter your first name?\n")
lastName = input("Enter your last name?\n")

fullName = firstName + " " + lastName

print("Your name is:" + fullName)


Recently we learned about functions. Our code changed structure to look more like this:

def getFullName():
    firstName = input("Enter your first name?\n")
    lastName = input("Enter your last name?\n")
    return firstName + " " + lastName


We noticed that now our code no longer runs top to bottom. The input statements don't execute until we call the function. To get the code to run, we have to write a main function to call getFullName. We did this so that if we wanted to get multiple fullNames we could simply call getFullName multiple times. A main might look something like this:

def main():
    name1 = getFullName()
    print("Your name is:" + name1)
    print("Your name is:" + getFullName())

if __name__ == "__main__":
    main()
    
    
You'll notice that if we tried to print out the variables firstName or lastName in main, we get an error. Try adding the following line under the first print statement, in main.

print("FirstName is: " + firstName)

This does not work because the variables firstName and lastName are only in the scope of the getFullName function. Every time you call getFullName, Python creates 2 new variables called firstName and lastName, and then every time you return from getFullName, Python destroys those variables.

Similarly the variable name1 in main can not be used in the function getFullName because name1 only exists in main.

This is called local scope. Any variable created in a function has scope local to that function.

In Python, there is also such thing called global scope. Any variable defined outside of a function is in the global scope. Variables in the global scope can be used by any function. To use a global variable, the global variable has to be defined in the local scope using the global keywords. If you do not use the global keyword then a local variable will be created instead. Example:

count = 4
print("Starting:",count)

def func1():
    global count
    count += 1
    print("Func1:", count)

def func2():
    global count
    count *= 2 + 3 # Multiplies count times 5
    print("Funct2:", count)

def func3():
    count = 100
    print("Func3:", count)

print("Count before")
func1()
func2()
func3()
print("Count after", count)
It is generally good practice to avoid using global variables. You should pass data between functions by using function parameters. The above code would be better written as:

def func1(input):
    input += 1
    print("Func1:", input)
    return input

def func2(count):
    count *= 2 + 3 # Multiplies count times 5
    print("Funct2:", count)
    return count

def func3():
    count = 100
    print("Func3:", count)

def main():
    count = 4
    print("Starting:",count)
    print("Count before")
    count = func1(count)
    count = func2(count)
    func3()
    print("Count after", count)

if __name__ == "__main__":
    main()
Notice we need to return the changed variable every time and update count with the new value. If count was a mutable type we could just change the variable in the function.

Multiple Return Value
In Python, functions only can return one value. However that one value can be a list or a tuple that can be unpacked and used as if the function returned multiple values. Example:

def orderRunners(runnerA, runnerB, runnerC, runnerD, runnerE):
    first = runnerD
    second_place_tie = [ runnerB, runnerA, runnerE ]
    fifth = runnerC
    return first, second_place_tie, fifth

def main()
     first, tie, last = orderRunners( "Ameni", "Josette", "Paul", "Dave", "Tre")
     print("Winner:", first)
     print("Last:", last)
     print("Tied:", tie)

if __name__ == "__main__":
    main()
Function Objects
In Python, functions are objects just like numbers, strings, lists, and dictionaries. You can pass them as values and assign them to variables.

f = 4
print(f)

def f(x):
    return 1/x

print(f(2))
print(f)

g = f
print(g(3))
print(g)

g = min
print(g([9,8,7]))

def c(p,l):
    return p(l)

print(c(g,[16,33,19]))
Keyword and Default Arguments
These topics are not used much in this class but they are an extremely powerful feature in Python. Make sure you are familiar these topics from the reading. They are fair game for exams.


------------------------------------------------------------------------

Lab Assignment
For this lab you will write the following 4 functions and a main:

getInput()
This function should take no parameters and return the following four values read from user input in the order listed below.

Input a color.
Input a number.
Input a second number.
Input a season.
The prompts for these inputs can be whatever you like.

printColor()
This function should take 1 parameter and return nothing. It should print out the sentence "Favorite color is parameter" where parameter is the color passed to the function.

addNumbers()
This function should take 2 number parameters and return their sum.

setGlobal()
This function should take 1 parameter and return nothing. This function should set the global variable favoriteSeason to the value of the parameter.

main()
This function should take no parameters and return nothing. This function should first call getInput() and unpack the four resulting variables. It should then call printColor with the first unpacked value. Then call addNumbers with the float of the second and third unpacked value. Then call setGlobal with the fourth unpacked value.

"""
 
# TODO: getInput()
def getInput():
# This function should take no parameters and return the following four values read from user input in the order listed below.
# Input a color.
    global color
    color = input('Input a color.\n')
# Input a number.
    global number1
    number1 =  input('Input a number.\n')
# Input a second number.
    global number2
    number2 = input('Input a second number.\n')
# Input a season.
    global favoriteSeason
    favoriteSeason = input('Input a season.\n')
# The prompts for these inputs can be whatever you like.
    print('\n')
    print('color:', color, '\n')
    print('number 1:', number1, '\n')
    print('number 2:', number2, '\n')
    print('season:', favoriteSeason, '\n')
# getInput()


# TODO: printColor()
# It should print out the sentence "Favorite color is parameter" where parameter is the color passed to the function.
# This function should take 1 parameter and return nothing.
def printColor(param1):
    print('Favorite color is', param1)
# printColor(input('what is your favorite color? \n'))



# TODO: addNumbers()
# This function should take 2 number parameters and return their sum.
def addNumbers(num1, num2):
    sum = int(num1) + int(num2)
    print(num1, '+', num2, '=', sum)

# addNumbers(input('num1: '), input('num2: '))



# TODO: setGlobal()
# This function should take 1 parameter and return nothing. 
# This function should set the global variable favoriteSeason to the value of the parameter.
def setGlobal(favoriteSeason):
    print('global set to:', favoriteSeason)
    



# TODO: main()
# This function should take no parameters and return nothing. 
# This function should first call getInput() and unpack the four resulting variables. 
# It should then call printColor with the first unpacked value. 
# Then call addNumbers with the float of the second and third unpacked value. 
# Then call setGlobal with the fourth unpacked value.
def main():
    getInput()
    printColor(param1 = color)
    addNumbers(number1, number2)
    setGlobal(favoriteSeason)
    
    
    

main()