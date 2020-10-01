# 6.7 A6 Program

**Assignment:**
This assignment should use while loops to:

- Gather an unknown amount of grades from the user, stopping when the user enters a negative value.
- Print the grades received.
- Calculate and print the average, maximum value, and minimum value.

> [!CAUTION]
> NOTE: DO NOT USE FOR LOOPS OR BUILT-IN LIST FUNCTIONS (except for len() and append()).

**Here are the specifications for the functions you will be writing:**

- `get_grades()`
  - Iterate with a while loop to put all positive user inputs into a list called grades until encountering a negative value
  - Return the list of grades
  
- `print_grades(grades)`
  - Takes one parameter, grades, as a list
  - Prints the grades each on a separate line. It should not print in list format.

- `average(grades)`
  - Takes one parameter, grades, as a list
  - Calculates the average of all the values in grades. If grades is empty, average should be zero.
  - Return the average as a float

- `maximum(grades)`
  - Takes one parameter, grades, as a list
  - Find the maximum grade in grades. If grades is empty, maximum should be zero.
  - Return the maximum grade as a float

- `minimum(grades)`
  - Takes one parameter, grades, as a list
  - Finds the minimum grade in grades. If grades is empty, minimum should be zero.
  - Return the minimum grade as a float

**Example input:**

``` python
55.0
83.0
92.0
27.0
-1.0
```

**Example output:**

``` python
Enter grade:
Enter grade:
Enter grade:
Enter grade:
Enter grade:
55.0
83.0
92.0
27.0
Average: 64.25
Max: 92.0
Min: 27.0
```
