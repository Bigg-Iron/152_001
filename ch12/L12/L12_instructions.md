# 12.12 L12 - Lab

Plan
This lab covers an introduction to recursion.

## What is Recursion?

Recursion is, simply put, a technique computer scientists use to solve problems which are described in terms of themselves: problems where the answer to the problem involves solving smaller versions of the same problem until we know the answer to the smallest problem. While coding, this equates to essentially calling a function within itself, creating a loop.

## Example

All recursive functions have a base case and a recursive case. A base case is a condition that indicates when to stop. A recursive case is a condition that calls the function again.

This example is going to demonstrate a recursive algorithm for simple multiplication. x is the starting number, n is how much to multiply it by. This function only works for positive numbers.

`multiply(x, n):`

Rules:

```python

n = 0: multiply(x, n) = 0
n = 1: multiply(x, n) = x
multiply(x, n) = x + multiply(x, n - 1)

```

Steps:

```python

Add base case(s):
def multiply(x, n):
    # base case(s)
    if (n == 0):
        return 0
    elif (n == 1):
        return x
Add recursive case:
def multiply(x, n):
    # base case(s)
    if (n == 0):
        return 0
    elif (n == 1):
        return x
    # recursive case
    else: # recursive case
        return x + multiply(x, n-1)
Check output:
print(multiply(3, 0))
print(multiply(3, 1))
print(multiply(3, 5))
```

## Lab 12

This lab should implement three separate recursive functions:

`factorial()`, `fib()`, and `exponent()`:

`factorial(n)` (calculates factorial)

```python

# Rules:
n = 1: factorial(n) = 1
n = 0: factorial(n) = 1
n < 0: factorial(n) = 0
factorial(n) = n * factorial(n-1)

# Examples:
factorial(1) = 1
factorial(0) = 1
factorial(-10) = 0
factorial(5) = 5 * 4 * 3 * 2 * 1 = 120
fib(n) # (calculates fibonacci sequence)

# Rules:
n <= 0: fib(n) = 0
n = 1 or n = 2: fib(n) = 1
fib(n) = fib(n-1) + fib(n-2)

# Examples:
fib(5) = 3 + 2
fib(2) = 1
fib(1) = 1
fib(-2) = 0
exponent(n) (calculates exponents)

# Rules:
n = 0: exponent(n) = 1
n < 0: exponent(n) = 0
exponent(n) = 2 * exponent(n-1)

# Examples:
exponent(-2) = 0
exponent(0) = 1
exponent(1) = 2
exponent(3) = 8

# Example input:
# Note: These values can be changed in main, they will not affect your code when submitted.
print(factorial(-2))
print(factorial(5))
print(exponent(4))
print(fib(7))

# Example output:
0
120
16
13

```
