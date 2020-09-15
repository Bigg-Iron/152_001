def countDown(first, last):
    if first >= last:
        for i in range(first, last-1, -1):
            print(i, end=' ')
    # pass
    print('\n')


# FIXME: oddNumbers(N)
def oddNumbers(N):
    n = []
    i = 1

    while i < N:
        n.append(i)
        i += 2
    print(n)


def reverse(s):
    str = ''
    for i in s:
        str = i + str
    return str
    # pass


def countInput():
    g = []
    i = 0
    while True:
        n = input('')
        i += 1
        if n != 'stop':
            g.append(n)
        else:
            return print(i)
    # pass


# Write some tests here to see if your code works
def main():

    # countDown(9, 3)
    # print(reverse('Chicken'))
    # countInput()
    # print(oddNumbers(8))


    # Do not modify the code below
if __name__ == '__main__':
    main()
