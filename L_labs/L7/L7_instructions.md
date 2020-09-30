# 7.11 L7 - Lab

Plan
This lab covers data types in Python. (Strings, Integers, Floating Point, Boolean, Lists, and Dictionaries)

**Lab Assignment**
This program consists of 5 functions that do different things and do not relate to each other. Each one uses a for loop (or two) to complete its task.

> [!NOTE]
> DO NOT USE BUILT-IN LIST FUNCTIONS OR WHILE LOOPS TO COMPLETE THIS ASSIGNMENT (except len() and append())

**Here are the specifications for the functions you will be writing:**

- **`sum_list(l)`**

  - Takes one parameter, l, a list of numeric types
  - Loops over the list and calculates the sum of all the numbers in the list
  - Returns the sum as a float
  - Example:

    ```python
    print(sum_list([1, 2.0, 16]))  # Prints 19.0
    ```

- **`every_other(start, end)`**

  - Takes two parameters, start and end, both ints
  - Creates a list containing every other number from start to end (including end when possible).
  - This function should only accept values going forward
  - Returns the list
  - Example:

    ```python
    print(every_other(1,10)) # Prints [ 1,3,5,7,9 ]  (notice 10 is not included because #10 is not in every other)
    print(every_other(4,8))  # Prints [ 4,6,8 ]
    print(every_other(8,2))  # Prints [  ]
    ```

- **`count(item, container)`**

  - Takes two parameters, item and container (the container could be a string, list or even a dictionary.)
  - Loops over the container element by element and counts the number of times the item is found in that container
  - Returns the total number of items found in the container as an int
  - Example:

  ```python
   print(count('a',"banana"))               # Prints 3
   print(count(8, [ 4, 6, 8, 80, 2, 8 ]))   # Prints 2 Notice 80 is not 8
   print(count(1.2,{1.2:"a"})               # Prints 1 as there is one key with value 1.2
  ```

- **`compare_strings(string1, string2)`**

  - Takes two parameters, string1 and string2
  - Checks if the strings are exactly the same.
  - You should loop over one string checking if its characters match the characters in the other string. Do not use `string1 == string2` we are practicing using loops. Hint: Make sure the strings are the same length before you start looping!
  - Returns a boolean value (True if they match, False otherwise)
  - Example:

  ```python
   print(compare_strings("diamond", "diamond"))  # Returns True
   print(compare_strings("Orange", "orange"))    # Returns False
   print(compare_strings("App", "Application"))  # Returns False
  ```

- **`print_grid(rows,cols)`**

  - Takes two parameters, rows and cols, both ints
  - Prints a grid of hashtags (#) where rows is the height and cols is the length
  - Example:

  ```python
  print_grid(4,4)
  ####
  ####
  ####
  ####
  ```

  ```python
  print_grid(2,8)
  ########
  ########
  ```

`main()`
Use the given main to test your functions. You can change it to test with different inputs, you won't be graded on main.
