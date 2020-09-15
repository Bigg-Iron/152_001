def countDown(first, last):
    if first >= last:
        for i in range(first, last-1, -1):
            print(i, end = ' ')
    # pass
    print('\n')


# FIXME: oddNumbers(N)
def oddNumbers(N):
    pass


def reverse(s):
    str = ''
    for i in s:
        str = i + str
    return str
    # pass

# FIXME: countInput()
def countInput():
    pass


# Write some tests here to see if your code works
def main():
    
    # countDown(9, 3)
    print(reverse('chicken'))

# Do not modify the code below
if __name__ == '__main__':
    main()
    