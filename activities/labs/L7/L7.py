def sum_list(l):
    if len(l) == 0:
        total = float(0)
        return total
    else:
        total = float(0)
        for s in l:
            total += s

    return total


def every_other(start, end):

    list = []
    if start < end:
        for item in range(start, end+1, 2):
            if item <= end:
                list.append(item)
        return list
    elif start > end:
        return list


def count(item, container):
    pass


def compare_strings(string1, string2):
    pass


def print_grid(rows, cols):
    pass

# Test your code in main


def main():
    print(sum_list([2, 4, 5.5, 9, -10]))
    print(every_other(1, 10))
    print(every_other(4, 8))
    print(every_other(8, 2))
    print(count('a', 'banana'))
    print(count(8, [4, 6, 8, 80, 2, 8]))
    print(compare_strings("Orange", "orange"))
    print(compare_strings("App", 'Application'))
    print_grid(4, 4)
    print_grid(2, 8)


# Do not change the code below
if "__main__" == __name__:
    main()
