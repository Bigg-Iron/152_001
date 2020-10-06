import math



''' Examples:
    SEE WRITEUP ABOVE
'''
def factorial(n):
    if n == 1 or n == 0:
        fact = 1
    elif n < 0:
        fact = 0 
    else:
        fact = n * factorial(n-1)
    return fact

''' Examples:
    SEE WRITEUP ABOVE
'''
def fib(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)

''' Examples:
    SEE WRITEUP ABOVE
'''
def exponent(n):

    return -1

def main():
    print(factorial(-2))
    print(factorial(5))
    print(exponent(4))
    print(fib(9))
    
if __name__ == "__main__":
    main()
